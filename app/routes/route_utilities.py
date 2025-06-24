from ..db import db
from flask import abort, make_response

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"message": f"{cls.__name__} {model_id} is invalid"}
        abort(make_response(response, 400))
    # this_id = "board_id" if cls == "Board" else "card_id"
    # query = db.select(cls.where(cls.id == model_id))
    # query = db.select(Board).where(Board.board_id == board_id)
    # if cls == "Card":
    #     query = db.select(cls).where(cls.card_id == model_id)
    # if cls == "Board":
    #     query = db.select(cls).where(cls.board_id == model_id)

    # query = db.select(cls).where(cls.board_id == model_id) if cls == "Board" else db.select(cls).where(cls.card_id == model_id)
    query = db.select(cls).where(cls.board_id == model_id)
    model = db.session.scalar(query) 
    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404)) 
    return model

def create_model(cls, model_data):
    try:
        new_model = cls.make_new(model_data)
    except KeyError as error:
        response = {"message": f"invalid {cls.__name__}: missing {error.args[0]}"}
        abort(make_response(response, 400))
    db.session.add(new_model)
    db.session.commit()
    return new_model.to_dict(), 201