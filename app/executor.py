import os
import docker

client = docker.from_env()


def execute_python_code(code: str):

    # Create temp folder if it doesn't exist
    os.makedirs("temp", exist_ok=True)

    file_path = os.path.join("temp", "sample.py")

    with open(file_path, "w") as file:
        file.write(code)

    return "Python file created successfully."