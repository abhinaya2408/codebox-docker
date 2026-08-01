from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="CodeBox Docker",
    description="Secure Online Code Execution Platform",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CodeBox Docker 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Running"
    }