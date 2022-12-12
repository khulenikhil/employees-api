from fastapi import FastAPI
from routes import employees_router

app = FastAPI()

app.include_router(employees_router)
