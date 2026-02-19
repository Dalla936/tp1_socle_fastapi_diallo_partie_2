from __future__ import annotations

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UserTable(Base):
    """
    Table ORM représentant l'entité User en base.
    """
    """
    Donne la structure de la table mais en sql avec le mapping etc..
    """
    __tablename__ = "users" #nom de la table en sql, pluriel pour respecter les conventions

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)