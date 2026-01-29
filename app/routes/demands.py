from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/demandas", tags=["Demandas"])


class Demanda(BaseModel):
    
    titulo: str
    descricao: str
    status: str


class Demanda(DemandaCreate):
    id:int


demandas: List[Demanda] = []


@router.get("/", response_model=List[Demanda])
def listar_demandas():
    return demandas


@router.post("/", response_model=Demanda)
def criar_demanda(demanda: DemandaCreate): 
    novo_id = len(demandas) +1

    nova_demanda = Demanda(
        id=novo_id,
        titulo=demanda.titulo,
        descricao=demanda.descricao,
        status=demanda.status
    )

    demandas.append(nova_demanda)
    return nova_demanda
