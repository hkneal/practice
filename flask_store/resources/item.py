import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items, stores


blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    def put(self, item_id):
        REQUIRED = ["price", "name"]
        item_data = request.get_json()
        if not all(required_value in item_data for required_value in REQUIRED):
            abort(400, message="Bad Request. price, and name must be included.")

        try:
            item = items[item_id]
            item |= item_data

            return item

        except KeyError:
            abort(404, message="Item not found.")

@blp.route("/item")
class Item(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
        REQUIRED = ["price", "store_id", "name"]
        item_data = request.get_json()
        if not all(required_value in item_data for required_value in REQUIRED):
            abort(400, message="Bad Request. price, store_id, and name must be included.")

        for item in items.values():
            if(
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exists.")

        if item_data["store_id"] not in stores:
            abort(404, message="Store not found.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id":item_id}
        items[item_id] = item
        return item, 201
