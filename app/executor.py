import os
import uuid
import docker
from docker.errors import ContainerError

client = docker.from_env()


def execute_python_code(code: str):

    os.makedirs("temp", exist_ok=True)

    filename = f"{uuid.uuid4()}.py"

    file_path = os.path.join("temp", filename)

    try:

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)

        output = client.containers.run(
            image="python:3.11",
            command=f"python {filename}",
            volumes={
                os.path.abspath("temp"): {
                    "bind": "/app",
                    "mode": "rw"
                }
            },
            working_dir="/app",
            remove=True
        )

        return {
            "status": "success",
            "output": output.decode("utf-8")
        }

    except ContainerError as e:

        return {
            "status": "error",
            "output": e.stderr.decode("utf-8")
        }

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)