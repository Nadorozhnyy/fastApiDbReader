from sqlalchemy import select

from src.database import new_session
from src.models import HumanOrm
from src.schemas import SHuman


class HumanRepository:
    """
    Репозиторий для работы с данными из базы данных
    """
    @classmethod
    async def add_one(cls, data: SHuman):
        """
        Добавить новую запись о человеке в базу данных.

        :param data: SHuman
        :return: int
        """
        async with new_session() as session:
            human_dict = data.model_dump()
            human = HumanOrm(**human_dict)
            session.add(human)
            # Отправляем изменения в базу
            await session.flush()
            await session.commit()
            return human.id

    @classmethod
    async def find_all(cls, limit: int = None, filters: dict = None) -> list[SHuman]:
        """
        Получение данных из базы данных, есть возможность фильтрации по полу и возвращение определенного числа записей
        (limit)
        :param limit: int от 1 до 100
        :param filters: str male или female
        :return: list[SHuman]
        """
        async with new_session() as session:
            query = select(HumanOrm)
            # Проверяем наличие фильтров
            if filters:
                for key, value in filters.items():
                    query = query.filter(getattr(HumanOrm, key) == value)
            # Проверяем наличие лимита на возврат
            if limit:
                query = query.limit(limit)
            result = await session.execute(query)
            human_models = result.scalars().all()
            human_schemas = [SHuman.model_validate(human_model) for human_model in human_models]
            return human_schemas
