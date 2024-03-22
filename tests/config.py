import json

from settings import ROOT_DIR


class Config:
    SUPPORTED_ENVS = ['local', 'remote']

    def __init__(self, env, app, browser_type='chrome'):
        with open(f'{ROOT_DIR}/config.json') as config:
            configs = json.load(config)
        self.base_url = configs['app_url'][app]
        self.user_name = configs['user_info']["default_name"]
        self.user_password = configs['user_info']["default_password"]
        self.browser_type = configs['browser'][browser_type]
        self.env = configs['env'][env]
