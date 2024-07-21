from requests import Session, Response

from framework.api.rest_api import RestApi


class PetStoreApi(RestApi):
    URL = 'https://petstore.swagger.io/v2'

    def __init__(self):
        session = Session()
        super().__init__(self.URL, session)

    def create_user(self, params) -> Response:
        """
        param example: {
          "id": 0,
          "username": "string",
          "firstName": "string",
          "lastName": "string",
          "email": "string",
          "password": "string",
          "phone": "string",
          "userStatus": 0
        }
        :param params:
        :return:
        """
        return self.post(url=f'{self.URL}/user', json=params)

    def login(self, **params):
        """
        params example: {username='John', password='Demo'}
        :param params:
        :return:
        """
        return self.get(url=f'{self.URL}/user/login', params=params)


