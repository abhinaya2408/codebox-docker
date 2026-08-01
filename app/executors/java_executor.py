import os
import time
import docker
from docker.errors import ContainerError

client = docker.from_env()


def execute_java(code: str):

    os.makedirs("temp", exist_ok=True)

    java_file = os.path.join("temp", "Main.java")

    start_time = time.time()

    try:

        with open(java_file, "w", encoding="utf-8") as file:
            file.write(code)

        output = client.containers.run(
            image="eclipse-temurin:21",
            command="sh -c 'javac Main.java && java Main'",
            volumes={
                os.path.abspath("temp"): {
                    "bind": "/app",
                    "mode": "rw"
                }
            },
            working_dir="/app",
            remove=True
        )

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

        if os.path.exists(java_file):
            os.remove(java_file)

        class_file = os.path.join("temp", "Main.class")

        if os.path.exists(class_file):
            os.remove(class_file)