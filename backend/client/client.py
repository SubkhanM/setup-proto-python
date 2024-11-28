import grpc
import sys
sys.path.append('../')
import inventory_pb2
import inventory_pb2_grpc

def create_item(stub):
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    category = input("Enter item category: ")
    location = input("Enter item location: ")
    expiry_date = input("Enter item expiry date (format: YYYY-MM-DD): ")
    price = int(input("Enter item price: "))

    item = inventory_pb2.Item(id=item_id, name=name, category=category, location=location, expiry_date=expiry_date, price=price)
    response = stub.AddItem(item)
    print("AddItem Response:", response)

def get_all_items(stub):
    all_items = stub.GetAllItems(inventory_pb2.Empty())
    print("GetAll Response:", all_items)

def get_item(stub):
    item_id = input("Enter item ID: ")
    item = stub.GetItem(inventory_pb2.ItemId(id=item_id))
    print("GetItem Response:", item)

def update_item(stub):
    item_id = input("Enter item ID to update: ")
    name = input("Enter updated item name: ")
    category = input("Enter updated item category: ")
    location = input("Enter updated item location: ")
    expiry_date = input("Enter updated item expiry date (format: YYYY-MM-DD): ")
    price = int(input("Enter updated item price: "))

    item = inventory_pb2.Item(id=item_id, name=name, category=category, location=location, expiry_date=expiry_date, price=price)
    response = stub.UpdateItem(item)
    print("UpdateItem Response:", response)

def delete_item(stub):
    item_id = input("Enter item ID to delete: ")
    response = stub.DeleteItem(inventory_pb2.ItemId(id=item_id))
    print("DeleteItem Response:", response)

def run():
    channel = grpc.insecure_channel('localhost:5000')
    stub = inventory_pb2_grpc.InventoryServiceStub(channel)

    while True:
        print("\n1. Add Item\n2. Get All Items\n3. Get Item\n4. Update Item\n5. Delete Item\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_item(stub)
        elif choice == '2':
            get_all_items(stub)
        elif choice == '3':
            get_item(stub)
        elif choice == '4':
            update_item(stub)
        elif choice == '5':
            delete_item(stub)
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == '__main__':
    run()
