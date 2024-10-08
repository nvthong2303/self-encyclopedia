from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from sqlalchemy.orm import relationship

from models.BaseModel import EntityMeta
from models.BookAuthorAssociation import book_author_association


class Book(EntityMeta):
    __tablename__ = "books"

    id = Column(Integer)
    name = Column(String(40), nullable=False)
    authors = relationship("Author", lazy="dynamic", secondary=book_author_association)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
