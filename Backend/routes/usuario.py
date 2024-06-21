from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

usuario = APIRouter()
usuarios=[]

class model_usuarios(BaseModel):
    id:int
    nombre:str
    password:str
    id_persona:int
    created_at: datetime = datetime.now()
    estatus: bool = False


@usuario.get('/')

def bienvenido():
    return "Bienvenido al api del sistema"

@usuario.get("/usuarios")

def getUsuarios():
    return usuarios

@usuario.post('/usuarios')

def save_usuario(datos_usuario:model_usuarios):
    usuarios.append(datos_usuario)
    return "Datos guardados correctamente papu"


@usuario.delete('/usuarios/{id_usuario}')

def delete_usuario(id_usuario: int):
    global usuarios
    
    # Buscar la persona por su ID
    for i, usuario in enumerate(usuarios):
        if usuario.id == id_usuario:
            del usuarios[i]
            return f"Dato con ID {id_usuario} eliminado correctamente."



@usuario.put('/usuarios/{id_usuario}')
def update_usuario(id_usuario: int, datos_usuario: model_usuarios):
    global usuarios
    
    # Buscar la persona por su ID
    for usuario in usuarios:
        if usuario.id == id_usuario:
            # Actualizar los campos de la persona
            usuario.nombre = datos_usuario.nombre
            usuario.password= datos_usuario.password
            usuario.id_persona= datos_usuario.id_persona
            usuario.estatus = datos_usuario.estatus
            
        return f"Dato con ID {id_usuario} actualizado correctamente."

@usuario.get('/usuarios/{id_usuario}')

def get_usuarios_id(id_usuario: int):
    global usuarios
    # Buscar la persona por su ID
    for  usuario in usuarios:
        if usuario.id == id_usuario:
            return usuario
    return f"No hay we {id_usuario}"