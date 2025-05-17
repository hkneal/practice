from fastapi import FastAPI
import httpx

app = FastAPI()
URLstr = "https://pokeapi.co/api/v2/pokemon/"

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_books_by_category(category: str):
    book_lst = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book_lst.append(book)
    return book_lst

@app.get("/books/{book_author}/")
async def read_books_by_author_and_category(book_author: str, category: str):
    book_lst = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            if book.get('category').casefold() == category.casefold():
                book_lst.append(book)
    return book_lst

@app.get("/get-external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(URLstr)
        data = response.json()
        print(type(data))
        print(data)
        return data.get("results")[-1]