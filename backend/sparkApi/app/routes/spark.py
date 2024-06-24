from fastapi import APIRouter
from app.services.spark_services import run_spark_job

router = APIRouter()

@router.post("/run-spark-job")
def execute_spark_job():
    result = run_spark_job()
    return {"result": result}
