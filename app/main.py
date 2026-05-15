from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="AI Project Template")
app.include_router(router)


@app.get("/")
def health():
    return {"status": "AI system running"}
