from fastapi import FastAPI

app = FastAPI(
    title="OpenSource Navigator",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "OpenSource Navigator Backend Running"
    }