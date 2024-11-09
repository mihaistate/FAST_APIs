from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    
books = []

@app.post("/books/", response_model=Book)
def add_book(book:Book):
    books.append(book)
    return book


@app.get("/books/", response_model=List[Book])
def get_books():
    return books

@app.get("/book/{book_id}/", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404,detail="Book not found")

@app.put("/book/{book_id}/", response_model=Book)
def update_book(book_id: int, updated_book:Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/book/{book_id}/")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
