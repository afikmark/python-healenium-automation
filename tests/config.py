import os


class Config:
    SUPPORTED_ENVS = ['dev', 'qa']

    def __init__(self, env):
        self.base_url = {
            'dev': 'https://www.saucedemo.com/',
            'qa': 'https://www.saucedemo.com/',
            'prd': 'https://saucelabs.com/'
        }[env]

        self.user = {
            "default": os.environ.get('DEFAULT_USER'),
            "password": os.environ.get('DEFAULT_PASSWORD')
        }
