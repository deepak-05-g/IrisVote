from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.registrations import router as registrations_router

app = FastAPI(title="IrisVote API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "IrisVote API"}


app.include_router(registrations_router)
