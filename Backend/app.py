from fastapi import FastAPI
from routes.persona import persona
from routes.users import user
from routes.persons import person

app = FastAPI()
app.include_router(person)
app.include_router(user)


print("Bienvenido a mi aplicacion")