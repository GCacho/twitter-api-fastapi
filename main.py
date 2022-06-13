#Python
import json
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

app = FastAPI()

#//////////////////////////
#         Models
#//////////////////////////

## id - email
class UserBase(BaseModel):
    user_id: UUID = Field(...) # UUID - Universal Unic ID
    email: EmailStr = Field(...)

## password
class UserLogin(UserBase): #Hereda de Userbase.
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )

## name and lastname
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

## user password for registation
class UserRegister(User, UserLogin):
        pass 

##tweets
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

### Registrar Usuario / User registation
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup a User

    This path operation registers a user in the app

    Parameters:
        - Request body parameter
            - user: UserRegister

   Returns a json with the basic user information:
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - bird_date: date
    """
    with open("users.json", "r+", encoding="utf8") as f: #para abrir un archivo extra, volverlo de lectura y escritura y que acepte tipografía español
        results = json.loads(f.read()) #json.loads toma un string y lo convierte a json
        user_dict = user.dict() #convierte el body a un diccionario / se necesita importar el body
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["bird_date"] = str(user_dict["birth_date"])
        results.append(user_dict) #anda fallando el append
        f.seek(0) #Regresa para remplazar la lista original.
        f.write(json.dumps(results)) #lo retransforma a json
        return user

### Login de Usuario / User Login
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

### Mostrar listado de usuarios / Show user list
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["Users"]
)
def show_all_users():
    pass

### Mostrar usuario especifico / Show specific user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

### Borrar un usuario / Delete User
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

### Actualizar un usuario / Update User
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

### Mostrar todos los tweets / Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet], #Para mostrar todos los tweets
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home1():
    return {"Twitter API": "Working!"}

### Publicar un tweet / Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post():
    pass

### Mostrar un tweet / Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Borrar un tweet / Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Actualizar un tweet / Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass