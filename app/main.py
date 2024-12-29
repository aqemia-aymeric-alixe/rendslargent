import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Rends l'argent"}

@app.get("/health")
def healtcheck():
    return {"Alive"}

if __name__ == "__main__":
    port = os.getenv("PORT", 80)
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)