from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI()

app.include_router(health_router)


@app.get("/")
async def main():
    return {
        "service": "supportops",
        "message": "SupportOps Hub is running"
    }
