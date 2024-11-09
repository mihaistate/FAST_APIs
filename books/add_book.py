import requests

url = "http://127.0.0.1:8000/books/"
book_data = {
    "id": 1,
    "title": "Test Book",
    "author": "Author",
    "year": 2021
}

response = requests.post(url, json=book_data)
print(response.json())