from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from httpx import AsyncClient
from datetime import datetime
import mysql.connector
import socket
import os

app = FastAPI()

load_dotenv()
API_KEY = os.getenv("API_KEY")
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Tao connection voi MySQL database
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
)

class WeatherInfo(BaseModel):
    temp: float
    feels_like: float
    humidity: float
    weather: str

def get_ip_address():
    # Lay IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return ip_address

def store_user_info(city_name: str):
    # Luu tru thong tin user trong database
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = get_ip_address()

    cursor = connection.cursor()
    query = "INSERT INTO users (city_name, ip_address, time) VALUES (%s, %s, %s);"
    values = (city_name, ip_address, time)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

@app.get("/weather/{city_name}")
async def generate_weather_info(city_name: str) -> WeatherInfo:
    store_user_info(city_name)

    async with AsyncClient() as client:
        # Tao HTTP request de lay thong tin ve kinh tuyen va vi tuyen (lat, lon) cua thanh pho tu OpenWeatherMap
        response = await client.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}")
        city_info = response.json()
        # Tao HTTP request de lay thong tin ve thoi tiet cua thanh pho tu OpenWeatherMap
        response = await client.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={city_info[0]['lat']}&lon={city_info[0]['lon']}&units=metric&appid={API_KEY}")
        data = response.json()

    # Lay nhung thong tin can thiet va store chung trong dict
    weather_info = {
        "temp": data["current"]["temp"],
        "feels_like": data["current"]["feels_like"],
        "humidity": data["current"]["humidity"],
        "weather": data["current"]["weather"][0]["main"]
    }

    return WeatherInfo(**weather_info)

    