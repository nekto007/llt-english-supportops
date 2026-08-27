from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {
        "service": "supportops",
        "message": "SupportOps Hub is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "supportops"
    }
