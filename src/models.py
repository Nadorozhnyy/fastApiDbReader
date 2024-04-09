from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Model(DeclarativeBase):
    pass


class HumanOrm(Model):
    """
    Модель для представления людей в базе данных.
    """
    __tablename__ = "humans"
    id: Mapped[int] = mapped_column(primary_key=True, comment="id")
    name: Mapped[str] = mapped_column(comment="Имя человека")
    gender: Mapped[str] = mapped_column(comment="Пол человека")
