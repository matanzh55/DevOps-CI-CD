-- init.sql
CREATE TABLE IF NOT EXISTS completed_games (
    id SERIAL PRIMARY KEY,
    board JSON NOT NULL,
    winner VARCHAR(10),
    finished_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
