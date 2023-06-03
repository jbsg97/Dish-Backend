from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.database.database import Base
from app.database.database import SessionLocal, engine
from mangum import Mangum

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hi from Dish API"}


app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
