import time
import subprocess
from pathlib import Path


class SelenoidManager:
    ROOT_DIR = Path(__file__).resolve().parent.parent
    CONFIGURATION_MANAGER_SELENOID = ROOT_DIR / "cm_windows_amd64.exe"

    def action_selenoid(self, action: str):
        match action:
            case "START":
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid", "start", "--vnc"], check=True)
                time.sleep(5)
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid-ui", "start"], check=True)
                print("Selenoid is up")
            case "STOP":
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid", "stop"], check=True)
                time.sleep(5)
                subprocess.run([self.CONFIGURATION_MANAGER_SELENOID, "selenoid-ui", "stop"], check=True)
                print("Selenoid is down")
            case _:
                raise RuntimeError("Provide either START or STOP for running docker")
