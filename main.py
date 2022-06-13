#Python
from datetime import date, datetime
from uuid import UUID
from typing import Optional, List

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

#//////////////////////////
#         Models
#//////////////////////////

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

#tweets
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

#//////////////////////////
#     Path Operations
#//////////////////////////


#home
@app.get(path="/")
def home():
    return{"Twitter API": "Working!"}


##---Users---

#Registrar Usuario
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup():
    pass

#Login de Usuario
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

#Mostrar listado de usuarios
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["Users"]
)
def show_all_users():
    pass

#Mostrar usuario especifico
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

#Borrar un usuario
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

#Actualizar un usuario
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass

##---tweets---

