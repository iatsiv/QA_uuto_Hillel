'''
Database User Username: Cluster80618
Database User Password: YntzW29tZGF+
'''

import json
from pymongo import MongoClient


connection = "mongodb+srv://Cluster80618:YntzW29tZGF%2B@cluster80618.cbwjiqn.mongodb.net/?appName=mongosh+1.9.1"
mongo_client = MongoClient(connection, tlsAllowInvalidCertificates=True)

db = mongo_client["hillel_db"]

collection = db["dz20"]

class Products:
    def __init__(self, id: int, name: str, price: float):
        self.id: int = id
        self.name: str = name
        self.price: float = price

class Orders:
    def __init__(self, order_id: int, products: list[Products]):
        self.order_id: int = order_id
        self.products: list[Products] = products

class User:
    def __init__(self, _id: str, id: int, name: str, email: str, orders: list[Orders]):
        self._id: str = _id
        self.id: int = id
        self.name: str = name
        self.email: str = email
        self.orders: list[Orders] = orders

    def __str__(self):
        return f"{self._id} {self.id} {self.name} {self.email} {len(self.orders)}"

def convert_user_to_object(base_dict: dict) -> User:
    list_of_orders = base_dict["orders"]
    order_list = []
    for order in list_of_orders:
        products = order["products"]
        product_list = []
        for product in products:
            product_obj = Products(product["id"], product["name"], product["price"])
            product_list.append(product_obj)
        order_obj = Orders(order["order_id"], product_list)
        order_list.append(order_obj)
    result_user = User(base_dict["_id"], base_dict["id"], base_dict["name"], base_dict["email"], order_list)
    return result_user


with open('user_data.json') as file:
    file_data = json.load(file)

collection.insert_many(file_data["users"])

user_for_move_to_object = collection.find_one({"name": "Bob"})

print(user_for_move_to_object)
print(convert_user_to_object(user_for_move_to_object))
