from sqlalchemy.orm import Session

from . import models, schemas, auth

import socket

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, new_password: str):
    db_user = get_user(db, user_id=user_id)
    new_hashed_password = auth.get_password_hash(new_password)
    db_user.hashed_password = new_hashed_password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id=user_id)
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


def get_queries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Query).offset(skip).limit(limit).all()


def create_user_query(db: Session, city_name: str, user_id: int):
    ip_address = socket.gethostbyname('localhost')
    db_query = models.Query(city_name=city_name, ip_address=ip_address, user_id=user_id)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query