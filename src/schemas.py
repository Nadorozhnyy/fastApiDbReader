from pydantic import BaseModel, Field


class SHumanBase(BaseModel):
    """
    Базовая модель человека для базы данных
    """
    name: str = Field(
        ...,
        title='human name',
        min_length=2,
        max_length=100,
    )
    gender: str


class SHuman(SHumanBase):
    """
    Модель данных для представления человека из базы данных.
    Включает в себя поле id.
    """
    id: int

    class Config:
        from_attributes = True
