from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from sqlalchemy.orm import relationship
from models.BaseModel import EntityMeta
from models.BookAuthorAssociation import book_author_association

class Author(EntityMeta):
    __tablename__ = "authors"

    id = Column(Integer)
    name = Column(String(16), nullable=False)
    books = relationship("Book", lazy="dynamic", secondary=book_author_association)

    PrimaryKeyConstraint(id)
    
    def normalize(self):
        return {
            "id": self.id,
            "name": self.name
        }

