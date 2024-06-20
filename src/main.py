import os
from dotenv import dotenv_values
from fastapi import FastAPI
from pymongo import MongoClient
import uvicorn
from routers.users import router as user_router
from routers.holidays import router as holiday_router

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
config = dotenv_values(dotenv_path)

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=5000, log_level="info")
    
app.include_router(user_router, tags=['Users'], prefix="/api/v1/users")
app.include_router(holiday_router, tags=['Holidays'], prefix="/api/v1/holidays")

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB Database")
    
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()