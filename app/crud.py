# app/crud.py
from sqlalchemy.orm import Session
from app.models import UserDB, UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = UserDB(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
