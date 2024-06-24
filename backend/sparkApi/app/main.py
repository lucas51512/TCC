from fastapi import FastAPI
from app.routes import spark

app = FastAPI()

app.include_router(spark.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
