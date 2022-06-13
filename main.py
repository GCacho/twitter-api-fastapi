#Python
from datetime import date, datetime
from uuid import UUID
from typing import Optional

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

#id - email
class UserBase(BaseModel):
    user_id: UUID = Field(...) # UUID - Universal Unic ID
    email: EmailStr = Field(...)

#password
class UserLogin(UserBase): #Hereda de Userbase.
    password: str = Field(
        ..., 
        min_length=8
    )

#name and lastname
class User(UserBase): #Hereda de Userbase.
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1, 
        max_length=256
    ) 
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


@app.get(path="/")
def home():
    return{"Twitter API": "Working!"}

