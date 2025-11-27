# tests/test_api.py
import pytest
import json
from app import app

@pytest.fixture
def client(monkeypatch):
    # monkeypatch DB saving to avoid real DB dependency
    monkeypatch.setattr('app.save_finished_game', lambda *a, **k: None)
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_new_game(client):
    res = client.post("/api/new")
    assert res.status_code == 200
    data = res.get_json()
    assert "board" in data
    assert len(data["board"]) == 9

def test_invalid_move(client):
    client.post("/api/new")
    res = client.post("/api/move", data=json.dumps({"position": 9}), content_type='application/json')
    assert res.status_code == 400

def test_game_flow(client):
    client.post("/api/new")
    # valid move
    res = client.post("/api/move", data=json.dumps({"position": 0}), content_type='application/json')
    assert res.status_code == 200
    data = res.get_json()
    assert "board" in data
