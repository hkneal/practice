import asyncio
from flask import Flask, jsonify
import httpx

app = Flask(__name__)

async def fetch_data(url):
    """Asynchronously fetches data from a given URL."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

@app.route("/")
def home():
    return '<h1>Hello Welcome to Testing with Flask REST API Async!<h1/>'

@app.route("/fetch_multiple_apis")
async def fetch_multiple_apis():
    """
    Asynchronously fetches data from two external APIs concurrently
    and combines the results.
    """
    api_url_1 = "https://jsonplaceholder.typicode.com/todos/1"  # Example API 1
    api_url_2 = "https://jsonplaceholder.typicode.com/posts/1"  # Example API 2

    try:
        # Use asyncio.gather to run multiple awaitable tasks concurrently
        data1, data2 = await asyncio.gather(
            fetch_data(api_url_1),
            fetch_data(api_url_2)
        )
        return jsonify({
            "api_data_1": data1,
            "api_data_2": data2
        })
    except httpx.RequestError as e:
        return jsonify({"error": f"API request failed: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)