from flask import Blueprint, Response, make_response
from app.models.card import Card
from app.routes.route_utilities import validate_model
from ..db import db

cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@cards_bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return Response(status=204, mimetype="application/json")

@cards_bp.put("/<card_id>")
def update_card_likes(card_id):
    card = validate_model(Card, card_id)
    card.likes += 1
    db.session.commit()
    return Response(status=204, mimetype="application/json")