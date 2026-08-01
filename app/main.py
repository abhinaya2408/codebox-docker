from fastapi import FastAPI

app = FastAPI(
    title="CodeBox API",
    description="Secure Online Code Execution Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to CodeBox 🚀"}

@app.get("/health")
def health():
    return {"status": "Running"}