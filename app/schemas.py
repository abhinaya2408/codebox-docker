from pydantic import BaseModel


class CodeRequest(BaseModel):
    language: str
    code: str


class CodeResponse(BaseModel):
    status: str
    output: str
    execution_time: float