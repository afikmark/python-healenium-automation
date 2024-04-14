from env_vars import MONGO_URL

from pymongo import MongoClient
from typing import TypeVar, Any, Mapping
from pymongo.collection import Collection
from abc import ABC, abstractmethod

T = TypeVar('T')


class DbClient(ABC):

    @staticmethod
    @abstractmethod
    def _connect(connection_data: str) -> T:
        """This method should connect to the DataBase"""


class MongoDbClient(DbClient):

    def __init__(self, connection_data: str):
        self.cluster = self._connect(connection_data)

    @staticmethod
    def _connect(connection_data: str) -> MongoClient[Mapping[str, Any] | Any]:
        return MongoClient(connection_data)

    def get_collection(self, *, data_base: str, collection: str) -> Collection[Mapping[str, Any] | Any]:
        return self.cluster[data_base][collection]


# mongo_client_url = "mongodb+srv://afikmark:5JyM1AdyT8zFkvTY@cluster0.ywacopc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
if __name__ == '__main__':
    client = MongoDbClient(MONGO_URL)
    users_collection = client.get_collection(data_base="users", collection="users")
    print(users_collection.find_one({"_id": 0}))

# post = {"_id": 0, "first_name": ["John", "Ashley", "Kate", 'Daniel', 'Emily', 'Daniel'],
#         "last_name": ["Mark", "Smith", "Briar", 'Miller', 'Brown', 'Williams'],
#         "address": [{"state": "NY", "city": "New York", "street": "Maple Ave", "zip_code": "16156"},
#                     {'state': 'CA', 'city': 'San Diego', 'street': 'Park Ave', 'zip_code': '07746'},
#                     {'state': 'AZ', 'city': 'Phoenix', 'street': 'Washington St', 'zip_code': '76343'},
#                     {'state': 'TX', 'city': 'San Antonio', 'street': 'Main St', 'zip_code': '97916'}]}

# print(collection.find_one({"_id": 0}))
