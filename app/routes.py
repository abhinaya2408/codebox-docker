from fastapi import APIRouter
from .schemas import CodeRequest, CodeResponse

router = APIRouter()


@router.post("/execute", response_model=CodeResponse)
def execute_code(request: CodeRequest):

    return CodeResponse(
        output=f"Received code:\n{request.code}"
    )