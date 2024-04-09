from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from src import schemas
from src.repository import HumanRepository


router = APIRouter(
    prefix="/api/v1/humans",
)


@router.post("")
async def post_humans(human: schemas.SHuman) -> dict:
    """
    Добавить новую запись о человеке в базу данных.

    :param human: SHuman
    :return: int
    """
    if not (1 <= human.id <= 1000):
        raise HTTPException(status_code=400, detail="ID должен быть от 1 до 1000")
    if human.gender not in ("male", "female"):
        raise HTTPException(status_code=400, detail="Неверное значение пола")
    human_id = await HumanRepository.add_one(human)
    return {"ok": True, 'human_id': human_id}


@router.get("")
async def get_humans(
    limit: int = Query(None, ge=1, le=100),
    gender: Optional[str] = Query(None, description='Filter by gender (male/female)')
) -> list[schemas.SHuman]:
    """
    Получение данных из базы данных, есть возможность фильтрации по полу и возвращение определенного числа записей
    (limit)

    :param limit: int от 1 до 100
    :param gender: str male или female
    :return: list[SHuman]
    """
    filters = {}
    if gender:
        filters['gender'] = gender
    humans = await HumanRepository.find_all(limit=limit, filters=filters)
    return humans

