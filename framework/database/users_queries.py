from framework.database.data_base import MongoDbClient
from env_vars import MONGO_URL


class UsersQueries:
    DB = 'users'
    COLLECTION = 'users'

    def __init__(self):
        self.client = MongoDbClient(MONGO_URL)

    def get_first_names(self) -> list[str]:
        projection = {"first_name": 1, "_id": 0}
        cursor = self.client.get_collection(data_base=self.DB, collection=self.COLLECTION).find({}, projection)
        first_names = [name for doc in cursor for name in doc.get("first_name", [])]
        return first_names

    def get_last_names(self) -> list[str]:
        projection = {"first_name": 1, "_id": 0}
        cursor = self.client.get_collection(data_base=self.DB, collection=self.COLLECTION).find({}, projection)
        first_names = [name for doc in cursor for name in doc.get("last_name", [])]
        return first_names
