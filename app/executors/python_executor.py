import os
import uuid
import time
import docker
from docker.errors import ContainerError

# Connect to Docker Engine
client = docker.from_env()


def execute_python(code: str):

    # Create temp directory if it doesn't exist
    os.makedirs("temp", exist_ok=True)

    # Generate unique filename
    filename = f"{uuid.uuid4()}.py"

    # Full file path
    file_path = os.path.join("temp", filename)

    # Start execution timer
    start_time = time.time()

    try:
        # Save user code
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)

        # Run code inside Docker
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

        # End timer
        end_time = time.time()

        return {
            "status": "success",
            "output": output.decode("utf-8"),
            "execution_time": round(end_time - start_time, 3)
        }

    except ContainerError as e:

        end_time = time.time()

        return {
            "status": "error",
            "output": e.stderr.decode("utf-8"),
            "execution_time": round(end_time - start_time, 3)
        }

    finally:
        # Delete temporary file
        if os.path.exists(file_path):
            os.remove(file_path)