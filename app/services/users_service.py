from __future__ import annotations

from app.factories.users_factory_protocol import IUsersFactory
from app.models.user_model import UserModel
from app.models.user_model_create import UserModelCreate
from app.repositories.protocols.i_users_repository import IUsersRepository
from app.factories.users_factory import UsersFactory


class UsersService(IUsersRepository):
    """
    Service applicatif : orchestre la logique Users.

    - charge les users via la factory (source JSON pour ce TP)
    - expose list/get/create
    - persistance en mémoire (volontairement simple)
    """

    def __init__(self, repository: IUsersRepository = None, factory: UsersFactory = None, users_json_path: str = None) -> None:
        self._repository = repository
        self._factory = factory
        if factory is None and users_json_path is None:
            self._users: list[UserModel] = None #Pas de json path ni de factory, ni de repository, on initialise une liste, il utilisera listusers du repo
        else:
            self._users = self._factory.create_users(users_json_path)



    def list_users(self) -> list[UserModel]:
        if self._factory is not None and self._users is not None:
            return self._users
        return list(self._repository.list_users())

    def get_user_by_id(self, user_id: int) -> UserModel | None:
        if self._factory is not None and self._users is not None:
            for u in self._users:
                if u.id == user_id:
                    return u
            return None
                
        for u in self._repository.list_users():
            if u.id == user_id:
                return u
        return None

    def create_user(self, payload: UserModelCreate) -> UserModel:
        if self._repository is None:

            next_id = max((u.id for u in self._users), default=0) + 1

            created = UserModel(
                id=next_id,
                login=payload.login,
                age=payload.age,
            )
            self._users.append(created) #Service crée un utilisateur en mémoire, pas de persistance réelle, juste pour les tests
            return created
        else:
            next_id = max((u.id for u in self._repository.list_users()), default=0) + 1
            created = UserModel(
                id=next_id,
                login=payload.login,
                age=payload.age,
            )
            self._repository.create_user(created)
            return created

