import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores


blp = Blueprint("stores", __name__, description="Operation on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")

    def put(self, store_id):
        REQUIRED = ["name"]
        store_data = request.get_json()
        if not all(required_value in store_data for required_value in REQUIRED):
            abort(400, message="Bad Request. price, and name must be included.")

        try:
            store = stores[store_id]
            store |= store_data

            return store

        except KeyError:
            abort(404, message="Store not found.")

@blp.route("/store")
class Store(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(400, message="Bad Request. Ensure 'name' is included.")

        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="Store already exists.")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store

        return store, 201