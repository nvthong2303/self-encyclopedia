from typing import List, Optional

from fastapi import APIRouter, Depends, status

from schemas.pydantic.AuthorSchema import AuthorSchema
from schemas.pydantic.BookSchema import (
    BookSchema,
    BookPostRequestSchema,
    BookAuthorPostRequestSchema
)
from services.BookService import BookService

BookRouter = APIRouter(prefix="/books", tags=["Books"])

@BookRouter.get("/", response_model=List[BookSchema])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    bookService: BookService = Depends()
):
    return [
        book.normalize()
        for book in bookService.list(
            name, pageSize, startIndex
        )
    ]

@BookRouter.post("/", response_model=BookSchema, status_code=status.HTTP_201_CREATED)
def create(
    book: BookPostRequestSchema,
    bookService: BookService = Depends()
):
    return bookService.create(book)

@BookRouter.get("/{book_id}", response_model=BookSchema)
def get(id: int, bookService: BookService = Depends()):
    return bookService.get(id).normalize()

@BookRouter.patch("/{id}", response_model=BookSchema)
def update(
    id: int,
    book: BookPostRequestSchema,
    bookService: BookService = Depends()
):
    return bookService.update(id, book).normalize()

@BookRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    bookService: BookService = Depends()
):
    bookService.delete(id)

@BookRouter.get("/{book_id}/author", response_model=AuthorSchema)
def get_authors(
    book_id: int,
    bookService: BookService = Depends()
):
    return [
        author.normalize()
        for author in bookService.get_authors(book_id)
    ]

@BookRouter.post("/{book_id}/author", response_model=AuthorSchema)
def add_author(
    book_id: int,
    bookService: BookService = Depends(),
):
    return bookService.add_author(book_id).normalize()


@BookRouter.delete("/{book_id}/author/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_author(
    book_id: int,
    author_id: int,
    bookService: BookService = Depends()
):
    return [
        author.normalize()
        for author in bookService.remove_author(book_id, author_id)
    ]
