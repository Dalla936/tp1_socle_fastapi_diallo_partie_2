from app.models_orm.user_table import UserTable
from app.repositories.protocols.i_users_repository import IUsersRepository
from app.db.session import Session
from app.models.user_model import UserModel
from app.models.user_model_create import UserModelCreate

class UsersRepositorySql(IUsersRepository):

    def __init__(self, session : Session) -> None:
        if session is not None: #Le repository ne crée pas la session
            self._db = session 
        else:
            self._db = None

    def list_users(self):
        list_users = self._db.query(UserTable).all() #return tt les utilisateurs
        for users in list_users:
            yield UserModel(id=users.id, login=users.login, age=users.age)
        return list(users)
    
    def get_user_by_id(self, user_id):
        user = self._db.query(UserTable).filter(UserTable.id == user_id).first()
        if not user :
            return None
        user_model = UserModel(id=user.id, login=user.login, age=user.age)
        return user_model

    def create_user(self, payload):
        user = UserTable(login=payload.login,age=payload.age)
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user) #recharger le user depuis la bd pour avoir une bonne version en memoire et en bd
        user_model_generated = UserModel(id=user.id, login=user.login,age=user.age)
        return user_model_generated
        

    

    