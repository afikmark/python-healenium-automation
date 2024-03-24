import time
import subprocess
from pathlib import Path
from framework.logger import get_logger

logger = get_logger()


class SelenoidManager:
    ROOT_DIR = Path(__file__).resolve().parent.parent
    CONFIGURATION_MANAGER_SELENOID = ROOT_DIR / "cm.exe"  # todo: add command to download selenoid configuration manager

    def action_selenoid(self, action: str):
        match action:
            case "START":
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid", "start", "--vnc"], check=True)
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid-ui", "start"], check=True)
                logger.info("Selenoid is up")
            case "STOP":
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid", "stop"], check=True)
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid-ui", "stop"], check=True)
                self.stop_all_containers()
                logger.info("Selenoid is down")
            case _:
                raise RuntimeError("Provide either START or STOP for running docker")

    def stop_all_containers(self):
        running_containers = self.get_running_containers_ids()
        for container_id in running_containers:
            try:
                subprocess.run(['docker', 'stop', container_id], check=True)
            except subprocess.CalledProcessError as e:
                logger.error(f"Error stopping container {container_id}: {e}")

    def get_running_containers_ids(self) -> list:
        output = subprocess.check_output('docker ps -a --format "{{.ID}}"', shell=True).decode("utf-8").rstrip()
        return output.split("\n")
