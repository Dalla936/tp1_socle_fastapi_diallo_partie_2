from __future__ import annotations

from sqlalchemy.orm import InstrumentedAttribute

from app.models_orm.user_table import UserTable


def test_should_define_tablename_users():
    # Arrange / Act
    name = getattr(UserTable, "__tablename__", None)

    # Assert (1 assertion métier)
    assert name == "users"


def test_should_have_mapped_columns_id_login_age():
    # Arrange / Act
    attrs = (UserTable.id, UserTable.login, UserTable.age)

    # Assert (1 assertion métier)
    assert all(isinstance(a, InstrumentedAttribute) for a in attrs)
