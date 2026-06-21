from fastapi import FastAPI
from app.routes import clients, projects, tasks

app = FastAPI(title="Shipyard Client Dashboard API")

app.include_router(clients.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Shipyard Client Dashboard API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
