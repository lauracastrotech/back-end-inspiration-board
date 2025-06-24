from flask import Blueprint, abort, request, Response, make_response
from app.models.Card import Card
from app.routes.route_utilities import validate_model
from ..db import db

cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")