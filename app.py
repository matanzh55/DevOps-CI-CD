# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from game_logic import TicTacToe
from bot import bot_move
import os
import json
import psycopg2
from typing import Optional

app = Flask(__name__, template_folder="templates")
CORS(app)  # allow local UI to call API if served separately

# Single in-memory game instance for simplicity. For multi-game, use Redis/session.
game = TicTacToe()

# Optional: store finished games in Postgres (local docker postgres)
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")

def get_db_conn():
    return psycopg2.connect(host=DB_HOST, port=DB_PORT,
                            dbname=DB_NAME, user=DB_USER, password=DB_PASS)

def save_finished_game(board, winner: Optional[str]):
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO completed_games (board, winner) VALUES (%s, %s)",
            (json.dumps(board), winner)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception:
        # Keep app resilient in demo: log for debugging but do not crash
        import logging
        logging.exception("Failed to save game to DB")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/new", methods=["POST"])
def new_game():
    global game
    game = TicTacToe()
    return jsonify({"board": game.board, "player": game.current_player})

@app.route("/api/move", methods=["POST"])
def human_move():
    global game
    payload = request.get_json() or {}
    pos = payload.get("position")
    # validate pos is an int and valid
    if not isinstance(pos, int):
        return jsonify({"error": "position must be integer 0..8"}), 400

    if not game.make_move(pos, "X"):
        return jsonify({"error": "Invalid move"}), 400

    # if human ended the game
    if game.winner:
        save_finished_game(game.board, game.winner)
        board = game.board.copy()
        winner = game.winner
        return jsonify({"board": board, "winner": winner})

    # Bot turn
    bot_pos = bot_move(game.board)
    if bot_pos is not None:
        game.make_move(bot_pos, "O")

    # If bot finished the game
    if game.winner:
        save_finished_game(game.board, game.winner)

    return jsonify({"board": game.board, "winner": game.winner})

@app.route("/games")
def show_games():
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, board, winner FROM completed_games ORDER BY id DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Convert the rows into a dict structure
        games = [{"id": r[0], "board": r[1], "winner": r[2]} for r in rows]

        return render_template("games.html", games=games)

    except Exception:
        import logging
        logging.exception("Failed to fetch games from DB")
        return "Error fetching games", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
