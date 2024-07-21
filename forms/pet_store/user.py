from common.providers import DictWithAttributes


class CreateUser(DictWithAttributes):
    id: str = ''
    username: str = ''
    firstName: str = ''
    lastName: str = ''
    email: str = ''
    password: str = ''
    phone: str = ''
    userStatus: str = ''
