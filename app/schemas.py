from datetime import datetime
from typing import List
from pydantic import BaseModel


class Query(BaseModel):
    id: int
    city_name: str
    ip_address: str
    time: datetime
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    queries: List[Query] = []

    class Config:
        orm_mode = True


class WeatherInfo(BaseModel):
    temp: float
    feels_like: float
    humidity: float
    weather: str

    class Config:
        orm_mode = True