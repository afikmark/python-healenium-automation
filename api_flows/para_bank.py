from requests import Session

from framework.api.rest_api import RestApi


class ParaBankApi(RestApi):
    URL = 'https://parabank.parasoft.com/parabank/services/bank'

    def __init__(self):
        session = Session()
        super().__init__(self.URL, session)

    def login(self, user_name: str, password: str):
        return self.get(url=f'{self.URL}/login/{user_name}/{password}')
