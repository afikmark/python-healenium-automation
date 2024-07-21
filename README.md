# Python-Healenium Automation Project

This project demonstrates automated testing using Python with Healenium for self-healing capabilities. It includes automated tests for a demo application and Swag Labs.

## Prerequisites

- Python 3.12 installed on your system.
- Dependencies installed from `requirements.txt`. You can install them using:


1. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    ```

2. **Activate the Virtual Environment**:
    - **Windows**:
      ```sh
      .\venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```sh
      source venv/bin/activate
      ```


- Docker installed
```sh
- git clone https://github.com/your_username/python-healenium-automation.git
```
## Set Up Configuration
Modify the config.json file in the config directory to match your environment settings, application URLs, and user info.
### pull selenoid browsers
```shell
docker compose -f framework/docker-browsers-pull.yaml up -d
```

### Set up healenium
```shell
docker compose -f /framework/healenium/docker-compose-selenoid.yaml up -d
```
### Run Tests
You can run the tests with different configurations using pytest. Here are some examples:

Run tests locally with Chrome:
```sh
pytest --browser_type=chrome --is_local True
```

Run tests with Chrome:
```sh
pytest --browser_type=chrome --is_local False
```
Run tests with Firefox:
```sh
pytest --browser_type=firefox --is_local False
```
Run tests remotely using Healenium:
```sh
pytest --browser_type=chrome --is_local False 
```
### Contributing:
Contributions are welcome! If you find any issues or improvements, feel free to open an issue or pull request.

### License
This project is licensed under the MIT License.
