import json

from settings import ROOT_DIR

class Config:
    def __init__(self, is_local, app, browser_type='chrome'):
        with open(f'{ROOT_DIR}/config/config.json') as config_file:
            config_data = json.load(config_file)

        self.is_local = is_local
        self.env_config = config_data['env']['local' if is_local else 'remote']
        self.base_url = "local" if is_local else "remote"
        self.app_url = config_data['app_urls'][app]
        self.user_name = config_data['user_info']['default_name']
        self.user_password = config_data['user_info']['default_password']
        self.browser_type = config_data['browsers'][browser_type]
        if not self.is_local:
            self.remote_url = self.env_config['healenium_url']
            self.selenoid_options = self.env_config['selenoid_options']
