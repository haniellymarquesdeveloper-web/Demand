from enum import Enum

class ProfileEnum(str, Enum):
    ADMIN = "admin"
    GESTOR = "gestor"
    USUARIO = "usuario"