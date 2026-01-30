from fastapi import FastAPI
from app.routes.demands import router as demands_router

app = FastAPI(title="Demand API")

app.include_router(demands_router)

@app.get("/")
def root():
    return {"message": "Está ativa a API de demandas "}
