from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    ABERTA = "ABERTA"
    FECHADA = "FECHADA"


class DemandaBase(BaseModel):
    titulo: str
    descricao: str
    criador: str
    status: StatusEnum

class DemandaCreate(DemandaBase):
    pass

class Demanda(DemandaBase):
    id: int


