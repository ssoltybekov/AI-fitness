from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Fitness AI Assistant",
    description="",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Fitness AI Assistant", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "ok", "ollama_model": settings.ollama_model}