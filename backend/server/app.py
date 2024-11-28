from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sys
sys.path.append('../')
import grpc
import inventory_pb2
import inventory_pb2_grpc
import os

app = Flask(__name__)
CORS(app)

grpc_channel = grpc.insecure_channel('localhost:5000')
grpc_stub = inventory_pb2_grpc.InventoryServiceStub(grpc_channel)

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/src/'))
app.template_folder = template_dir

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addItem", methods=['GET', 'POST'])
def add_item():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        data = request.json
        item_request = inventory_pb2.Item(
            id=data['id'],
            name=data['name'],
            category=data['category'],
            location=data['location'],
            expiry_date=data['expiry_date'],
            price=data['price']
        )
        response = grpc_stub.AddItem(item_request)
        return jsonify({"message": "Item added successfully"})


@app.route("/allItems")
def get_all_items():
    response = grpc_stub.GetAllItems(inventory_pb2.Empty())
    item_list = [{"id": item.id, "name": item.name, "category": item.category, "location": item.location, "expiry_date": item.expiry_date, "price": item.price} for item in response.items]
    return jsonify({"items": item_list})

@app.route("/item/<item_id>")
def get_item(item_id):
    response = grpc_stub.GetItem(inventory_pb2.ItemId(id=item_id))
    if response.id:
        item_data = {"id": response.id, "name": response.name, "category": response.category, "location": response.location, "expiry_date": response.expiry_date, "price": response.price}
        return jsonify(item_data)
    else:
        return jsonify({"message": "Item not found"}), 404
    
@app.route("/updateItem/<item_id>", methods=['PUT'])
def update_item(item_id):
    data = request.json
    item_request = inventory_pb2.Item(
        id=item_id,
        name=data['name'],
        category=data['category'],
        location=data['location'],
        expiry_date=data['expiry_date'],
        price=data['price']
    )
    response = grpc_stub.UpdateItem(item_request)
    return jsonify({"message": "Item updated successfully"})


@app.route("/deleteItem/<item_id>", methods=['DELETE'])
def delete_item(item_id):
    response = grpc_stub.DeleteItem(inventory_pb2.ItemId(id=item_id))
    return jsonify({"message": "Item deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
