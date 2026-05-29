from fastapi import FastAPI
from routes import dashboard

app = FastAPI()

app.include_router(dashboard.router)

@app.get("/")
def home():
    return {"message": "Backend running"}