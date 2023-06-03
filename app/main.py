import os

from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.database.database import Base
from app.database.database import engine
from mangum import Mangum
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    root_path = os.getenv('STAGE')
)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hi from Dish API"}


app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
