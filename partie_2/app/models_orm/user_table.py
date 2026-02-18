from __future__ import annotations

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UserTable:
    """
    Table ORM représentant l'entité User en base.
    """

    id: Mapped[int] = mapped_column(Integer, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)