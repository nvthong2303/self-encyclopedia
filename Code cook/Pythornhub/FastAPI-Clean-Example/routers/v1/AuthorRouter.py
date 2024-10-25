from typing import List, Optional
from fastapi import APIRouter, Depends, status

from schemas.pydantic.AuthorSchema import (
    AuthorSchema,
    AuthorPostRequestSchema
)
from schemas.pydantic.BookSchema import BookSchema
from services.AuthorService import AuthorService

AuthorRouter = APIRouter(prefix="/authors", tags=["Authors"])

@AuthorRouter.get("/", response_model=List[AuthorSchema])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    authorService: AuthorService = Depends()
):
    return [
        author.normalize()
        for author in authorService.list(
            name, pageSize, startIndex
        )
    ]
    
@AuthorRouter.post("/", response_model=AuthorSchema, status_code=status.HTTP_201_CREATED)
def create(
    author: AuthorPostRequestSchema,
    authorService: AuthorService = Depends()
):
    return authorService.create(author)

@AuthorRouter.get("/{author_id}", response_model=AuthorSchema)
def get(id: int, authorService: AuthorService = Depends()):
    return authorService.get(id).normalize()

@AuthorRouter.patch("/{id}", response_model=AuthorSchema)
def update(
    id: int,
    author: AuthorPostRequestSchema,
    authorService: AuthorService = Depends()
):
    return authorService.update(id, author).normalize()

@AuthorRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    authorService: AuthorService = Depends()
):
    return authorService.delete(id)

@AuthorRouter.get("/{author_id}/books/", response_model=List[BookSchema])
def get_books(
    id: int, authorService: AuthorService = Depends()
):
    return [
        book.normalize()
        for book in authorService.get_books(id)
    ]

