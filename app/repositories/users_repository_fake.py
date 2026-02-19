from typing import Optional
from app.models.user_model_create import UserModelCreate
from app.repositories.i_users_repository import IUsersRepository
from app.factories.users_factory import UsersFactory
from app.services.users_service import UsersService
from app.models.user_model import UserModel


class FakeUsersRepository(IUsersRepository):

    def __init__(self, factory: UsersFactory, json_path : str) -> None: #vu depuis les tests, on peut se permettre de faire du coupling fort avec la factory et le json_path
        self.users : list[UserModel] = []
        self.factory = factory
        self.json_path = json_path

    
    def list_users(self):
        service = UsersService(factory=self.factory, users_json_path=self.json_path)
        return service.list_users()
    
    def get_user_by_id(self, user_id: int) -> UserModel:
        service = UsersService(factory=self.factory, users_json_path=self.json_path)
        user = service.get_user_by_id(user_id)
        if user is None:
            return None
        return user
    
    def create_user(self, user_data: UserModelCreate) -> UserModel:
        factory = self.factory
        if isinstance(user_data, UserModelCreate):
            service = UsersService(factory=self.factory, users_json_path=self.json_path)
            #service pour bénéficier de la logique de génération d'id et de persistance en mémoire, on utilise pas la factory car elle prends pas des UserModelCreate en entrée
            user = service.create_user(user_data)
        else:
            user = factory.create_users(user_data)
        self.users.append(user)
        return user