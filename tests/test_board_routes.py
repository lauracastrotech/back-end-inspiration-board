import pytest
from app.models.Board import Board
# from flask import request
from app.db import db


#get_all_boards tests
def test_get_all_boards_with_no_boards(client):
    print("Board is:", Board)
    print("Board type is:", type(Board))
    response = client.get("/boards")

    assert response.status_code == 200
    assert response.get_json() == []


def test_get_all_boards_with_one_board(client, one_board):
    response = client.get("/boards")
    # response_body = request.get_json()

    assert response.status_code == 200
    assert response.get_json() == [{"id": 1, "title": "First Board", "owner": "First Owner"}]
    assert len(response.get_json()) == 1

def test_get_all_boards_with_many_boards(client, many_boards):
    response = client.get("/boards")

    assert response.status_code == 200
    assert response.get_json() == [{"id": 1, "title": "First Board", "owner": "First Owner"}, 
                                   {"id": 2, "title": "Second Board", "owner": "Betty"},
                                   {"id": 3, "title": "Third Board", "owner": "Charlie"},
                                   {"id": 4, "title": "Fourth Board", "owner": "Debbie"},
                                   {"id": 5, "title": "Fifth Board", "owner": "Eddie"},
                                   ]
    assert len(response.get_json()) == 5

def test_get_one_board_returns_specific_board_of_many(client, many_boards):
    response = client.get("/boards/2")

    assert response.status_code == 200
    assert response.get_json() == {"id": 2, "title": "Second Board", "owner": "Betty"}
    
def test_get_one_board_returns_another_board_of_many(client, many_boards):
    response = client.get("/boards/4")

    assert response.status_code == 200
    assert response.get_json() == {"id": 4, "title": "Fourth Board", "owner": "Debbie"}

def test_get_one_board_invalid_id(client, many_boards):
    response = client.get("/boards/one")

    assert response.status_code == 400
    assert response.get_json() == {"message": "Board one is invalid"}

def test_get_one_board_nonexistent_id_of_many(client, many_boards):
    response = client.get("/boards/17")

    assert response.status_code == 404
    assert response.get_json() == {"message": "Board 17 not found"}

def test_get_one_board_nonexistent_id_of_none(client):
    response = client.get("/boards/1")

    assert response.status_code == 404
    assert response.get_json() == {"message": "Board 1 not found"}

def test_make_new_board(client):
    response = client.post("/boards", json={"title": "Shire", "owner": "Frodo"})

    assert response.status_code == 201
    assert response.get_json() == {"id": 1, "title": "Shire", "owner": "Frodo"}

def test_make_new_card(client, one_board, one_card):
    response = client.post("/boards/1/cards", json={"message": "new message", "board_id": 1})

    assert response.status_code == 201
    assert response.get_json() == {"message": "new message","board_id": 1}    