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

if __name__ == '__main__':
    client = MongoDbClient(MONGO_URL)
    users_collection = client.get_collection(data_base="users", collection="users")
    print(users_collection.find_one({"_id": 0}))
