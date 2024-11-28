import grpc
import sys
sys.path.append('../')
import logging
import pymongo
from concurrent import futures
import inventory_pb2
import inventory_pb2_grpc

class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["InventoryManagement"]
        self.collection = self.db["ItemList"]
        logging.info("Connected to MongoDB")

    def AddItem(self, request, context):
        logging.info("Received AddItem request: %s", request)
        item_data = {
            "id": request.id,
            "name": request.name,
            "category": request.category,
            "location": request.location,
            "expiry_date": request.expiry_date,
            "price": request.price
        }
        self.collection.insert_one(item_data)
        return request

    def GetAllItems(self, request, context):
        logging.info("Received GetAllItems request")
        item_list = []
        for item_data in self.collection.find():
            item = inventory_pb2.Item(
                id=item_data["id"],
                name=item_data["name"],
                category=item_data["category"],
                location=item_data["location"],
                expiry_date=item_data["expiry_date"],
                price=item_data["price"]
            )
            item_list.append(item)
        return inventory_pb2.ItemList(items=item_list)
    
    def GetItem(self, request, context):
        logging.info("Received GetItem request for item ID: %s", request.id)
        item_data = self.collection.find_one({"id": request.id})
        if item_data:
            item = inventory_pb2.Item(
                id=item_data["id"],
                name=item_data["name"],
                category=item_data["category"],
                location=item_data["location"],
                expiry_date=item_data["expiry_date"],
                price=item_data["price"]
            )
            return item
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Item not found")
            return inventory_pb2.Item()
        
    def UpdateItem(self, request, context):
        logging.info("Received UpdateItem request for item ID: %s", request.id)
        item_data = self.collection.find_one({"id": request.id})
        if item_data:
            updated_item_data = {
                "id": request.id,
                "name": request.name,
                "category": request.category,
                "location": request.location,
                "expiry_date": request.expiry_date,
                "price": request.price
            }
            self.collection.update_one({"id": request.id}, {"$set": updated_item_data})
            return inventory_pb2.Empty() 
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Item not found")
            return inventory_pb2.Empty()

    def DeleteItem(self, request, context):
        logging.info("Received DeleteItem request for item ID: %s", request.id)
        result = self.collection.delete_one({"id": request.id})
        if result.deleted_count > 0:
            return inventory_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Item not found")
            return inventory_pb2.Empty()

def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    logging.info("Listening on port 5000")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
