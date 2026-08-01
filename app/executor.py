import os
import docker

client = docker.from_env()


def execute_python_code(code: str):

    # Create temp folder if it doesn't exist
    os.makedirs("temp", exist_ok=True)

    file_path = os.path.join("temp", "sample.py")

    with open(file_path, "w") as file:
        file.write(code)

    output = client.containers.run(
    image="python:3.11",
    command="python sample.py",
    volumes={
        os.path.abspath("temp"): {
            "bind": "/app",
            "mode": "rw"
        }
    },
    working_dir="/app",
    remove=True
    )

    return output.decode("utf-8")