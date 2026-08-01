import os
import uuid
import docker

# Connect to Docker Engine
client = docker.from_env()


def execute_python_code(code: str):

    # Create temp directory if it doesn't exist
    os.makedirs("temp", exist_ok=True)

    # Generate unique filename
    filename = f"{uuid.uuid4()}.py"

    # Complete path
    file_path = os.path.join("temp", filename)

    try:

        # Save code to file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)

        # Execute inside Docker
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

        return output.decode("utf-8")

    finally:

        # Delete temporary file
        if os.path.exists(file_path):
            os.remove(file_path)