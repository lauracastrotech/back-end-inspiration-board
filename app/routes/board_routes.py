from flask import Blueprint, request
from app.models.board import Board
from app.models.card import Card
from ..db import db
from .route_utilities import validate_model, create_model

boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

@boards_bp.get("")
def get_all_boards():
    query = db.select(Board).order_by(Board.board_id)
    boards = db.session.scalars(query)
    boards_response = []
    for board in boards:
        boards_response.append(board.to_dict())
    return boards_response

@boards_bp.get("/<board_id>")
def get_one_board(board_id):
    # query = db.select(Board).where(Board.board_id == board_id)
    # board = db.session.scalar(query)
    board = validate_model(Board, board_id)
    boards_response = board.to_dict()
    #use validate function
    return boards_response

@boards_bp.post("")
def make_new_board():
    request_body = request.get_json()
    return create_model(Board, request_body)

@boards_bp.post("/<board_id>/cards")
def make_new_card(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    # new_card = Card.make_new(request_body)
    # db.session.add(new_card)
    # db.session.commit()
    # return new_card.to_dict(), 201
    return create_model(Card, request_body)


@boards_bp.get("/<board_id>/cards")
def get_card(board_id):
    board = validate_model(Board, board_id)
    cards_list = []
    for card in board.cards:
        cards_list.append(card.to_dict())
    return cards_list