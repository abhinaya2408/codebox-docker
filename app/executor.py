from .executors.python_executor import execute_python
from .executors.java_executor import execute_java


def execute(language: str, code: str):

    language = language.lower()

    if language == "python":
        return execute_python(code)

    elif language == "java":
        return execute_java(code)

    else:
        return {
            "status": "error",
            "output": f"Unsupported language: {language}",
            "execution_time": 0.0
        }