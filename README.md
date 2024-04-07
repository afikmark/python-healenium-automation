# Python-Healenium Automation Project

This project demonstrates automated testing using Python with Healenium for self-healing capabilities. It includes automated tests for a demo application and Swag Labs.

## Prerequisites

- Python 3.x installed on your system.
- Dependencies installed from `requirements.txt`. You can install them using:
```sh
pip install -r requirements.txt
```
- Docker installed
```sh
- git clone https://github.com/your_username/python-healenium-automation.git
```
### Set Up Configuration
Modify the config.json file in the config directory to match your environment settings, application URLs, and user info.

### Run Tests
You can run the tests with different configurations using pytest. Here are some examples:

Run tests locally with Chrome:
```sh
pytest --browser_type=chrome --app swag_labs
```
Run tests with Firefox:
```sh
pytest --browser_type=firefox --app swag_labs
```
Run tests remotely using Healenium:
```sh
pytest --browser_type=chrome --is_local False --app swag_labs
```
### Contributing:
Contributions are welcome! If you find any issues or improvements, feel free to open an issue or pull request.

### License
This project is licensed under the MIT License.
