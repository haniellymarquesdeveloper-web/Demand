from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException


router = APIRouter(prefix="/demandas", tags=["Demandas"])


class DemandaCreate(BaseModel):
    titulo: str
    descricao: str
    status: str
    criador: str


class Demanda(DemandaCreate):
    id: int



demandas: List[Demanda] = []


@router.get("/", response_model=List[Demanda])
def listar_demandas():
    return demandas

@router.get("/{demanda_id}", response_model=Demanda)
def buscar_demanda(demanda_id: int):
     for demanda in demandas:
        if demanda.id == demanda_id:
            return demanda

     raise HTTPException(
        status_code=404,
        detail="Desculpe, mas essa demanda não foi encontrada. Tente novamente."
    )

@router.put("/{demanda_id}", response_model=Demanda)
def atualizar_demanda(demanda_id: int, dados: DemandaCreate):
    for index, demanda in enumerate(demandas):
        if demanda.id == demanda_id:
            demanda_atualizada = Demanda(
                id=demanda_id,
                titulo=dados.titulo,
                descricao=dados.descricao,
                status=dados.status,
                criador=dados.criador
            )

            demandas[index] = demanda_atualizada
            return demanda_atualizada

    raise HTTPException(
        status_code=404,
        detail="Desculpe, mas essa demanda não foi encontrada."
    )

@router.delete("/{demanda_id}")
def deletar_demanda(demanda_id: int):
    for index, demanda in enumerate(demandas):
        if demanda.id == demanda_id:
            demandas.pop(index)
            return {"message": "Demanda removida com sucesso."}

    raise HTTPException(
        status_code=404,
        detail="Desculpe, mas essa demanda não foi encontrada."
    )


@router.post("/", response_model=Demanda)
def criar_demanda(demanda: DemandaCreate): 
    novo_id = len(demandas) +1

    nova_demanda = Demanda(
        id=novo_id,
        titulo=demanda.titulo,
        descricao=demanda.descricao,
        status=demanda.status,
        criador=demanda.criador 
    ) 

    demandas.append(nova_demanda)
    return nova_demanda



