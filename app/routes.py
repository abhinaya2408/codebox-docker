from fastapi import APIRouter
from .schemas import CodeRequest, CodeResponse
from .executor import execute_python_code

router = APIRouter()


@router.post("/execute", response_model=CodeResponse)
def execute_code(request: CodeRequest):

    output = execute_python_code(request.code)

    return CodeResponse(
        output=output
    )