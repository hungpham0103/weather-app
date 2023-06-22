from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from httpx import AsyncClient

from .. import crud, models, schemas, auth, database

import os

router = APIRouter()

load_dotenv()
API_KEY = os.getenv("API_KEY")


@router.get("/weather/{city_name}")
async def generate_weather_info(city_name: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)) -> schemas.WeatherInfo:
    async with AsyncClient() as client:
        response = await client.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}")
        city_info = response.json()
        response = await client.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={city_info[0]['lat']}&lon={city_info[0]['lon']}&units=metric&appid={API_KEY}")
        data = response.json()

    weather_info = {
        "temp": data["current"]["temp"],
        "feels_like": data["current"]["feels_like"],
        "humidity": data["current"]["humidity"],
        "weather": data["current"]["weather"][0]["main"]
    }

    crud.create_user_query(db=db, city_name = city_name, user_id=current_user.id)

    return schemas.WeatherInfo(**weather_info)