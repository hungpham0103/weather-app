from fastapi import FastAPI

from . import models, database
from .routers import users, weather

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router)
app.include_router(weather.router)