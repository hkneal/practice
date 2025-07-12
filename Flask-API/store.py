from flask import Flask, jsonify, request


app = Flask(__name__)


stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/")
def home():
    return "<h1>Welcome to the Stores APP!</h1>"


@app.get("/stores")
def get_stores():
    # return jsonify({"stores": stores})
    return {"stores": stores}

@app.get("/store/<string:name>")
def get_a_store(name):
    for store in stores:
        if store["name"] == name:
            return {"store": store}
    return {"Error Message": "The store is not found"}, 404

@app.post("/store")
def create_new_store():
    try:
        new_store = request.get_json()
        stores.append(new_store)
        return new_store, 201
    except Exception as e:
        return jsonify({"Error Message": f"An unexpected error occurred: {e}"}), 500

@app.put("/store/<string:name>")
def add_item(name):
    new_item = request.get_json()
    for store in stores:
        if store["name"] == name:
            store["items"].append(new_item)
            return {"stores": stores}, 201
    return {"Error Message": "The store is not found"}, 404


@app.delete("/store/<name>")
def delete_a_store(name):
    try:
        for ind, dic in enumerate(stores):
            if dic["name"] == name:
                stores.pop(ind)
                return {"stores": stores}
        else:
            return {"Error": "Store Not Found"}, 404
    except KeyError as e:
        return jsonify({"Error": str(e),
                        "Message": "The Store {name} is not in this DB"}), 404


if __name__ == '__main__':
    app.run(debug=True)