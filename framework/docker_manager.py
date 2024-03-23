import time
from datetime import datetime, timedelta

from settings import ROOT_DIR
import os
import subprocess
from pathlib import Path


class DockerManager:
    ROOT_DIR = Path(__file__).resolve().parent.parent
    LOG_FILE = ROOT_DIR / "log.txt"
    STARTED_MSG = " Node has been added "
    STOPPED_MSG = "selenium-hub existed with code 0"
    START_DOCKER_FILE = ROOT_DIR / "startDocker.bat"
    STOP_DOCKER_FILE = ROOT_DIR / "stopDocker.bat"

    def action_docker(self, action: str):
        match action:
            case "START":
                subprocess.Popen(["cmd", "/c", "start", self.START_DOCKER_FILE])
                self.wait_till_log_file_created()
                # self.wait_till(self.STARTED_MSG)
                time.sleep(40)
                print("Grid is up")

            case "STOP":
                subprocess.Popen(["cmd", "/c", "start", self.STOP_DOCKER_FILE])
                # self.wait_till(self.STOPPED_MSG)
                time.sleep(40)
                print("Grid is down")

            case _:
                raise RuntimeError("Provide either START or STOP for running docker")

    def wait_till_log_file_created(self):
        flag = False
        while not flag:
            flag = os.path.exists(self.LOG_FILE)
            time.sleep(1)
        print("Logs file is created")

    # def wait_till(self, signal):
    #     wait_till = datetime.now() + timedelta(seconds=40)
    #     started = False
    #     while datetime.now() < wait_till:
    #         with open(self.LOG_FILE, 'r') as file:
    #             file_content = file.read()
    #             if signal in file_content:
    #                 started = True
    #                 break
    #         time.sleep(1)
    #     if not started:
    #         raise RuntimeError("Grid not started/terminated")
