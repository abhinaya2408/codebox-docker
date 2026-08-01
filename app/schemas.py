from pydantic import BaseModel


class CodeRequest(BaseModel):
    code: str


class CodeResponse(BaseModel):
    status: str
    output: str