from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class Card(db.Model):
    card_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int] = mapped_column(default=0)
    board_id: Mapped[int] = mapped_column(ForeignKey("board.board_id"))
    board: Mapped["Board"] = relationship(back_populates="cards")

    def to_dict(self):
        card_dict = {
            "id": self.card_id, 
                     "message": self.message, 
                     "likes_count": self.likes_count,
                     "board_id": self.board_id}
        return card_dict
    
    @classmethod
    def make_new(cls, dict):
        new_card = Card(message=dict["message"], board_id=dict["board_id"])
        return new_card