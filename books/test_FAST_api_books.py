from fastapi.testclient import TestClient
from FAST_api_books import app, Book

client = TestClient(app)

def test_add_book():
    response = client.post("/books/", json={"id": 1, "title": "Test Book", "author": "Author", "year": "2021"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Book", "author": "Author", "year": 2021}
    
def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert response.json() == [{"id":1, "title": "Test Book", "author": "Author", "year": 2021}]
        
def test_get_book():
    response = client.get("/book/1")
    assert  response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Book", "author": "Author", "year": 2021}
            
def test_update_book():
    response = client.put("/book/1/", json={"id": 1, "title": "Updated Book", "author": "Author", "year": 2021})
    assert response.status_code ==200
    assert response.json() == {"id": 1, "title": "Updated Book", "author": "Author", "year": 2021}
   

def test_delete_book():
    response = client.delete("/book/1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted"}  