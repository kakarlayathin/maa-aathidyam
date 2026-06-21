from fastapi import FastAPI

app = FastAPI(title="Maa Aathidyam API")

@app.get("/")
async def root():
    return {"message": "Welcome to Maa Aathidyam API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
