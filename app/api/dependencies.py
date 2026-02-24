"""
Module de composition de l'application.
Rôle :
    - Lire la configuration (Settings).
    - Choisir l'implémentation concrète du repository (SQL, Fake, etc.).
    - Construire le service
    - Exposer une dépendance FastAPI unique 
Aucune logique métier ici, juste de la composition.
Aucune route ici.
"""
from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.settings import get_settings
from app.db.session import get_db

from app.repositories.users_repository_sql import UsersRepositorySql
from app.repositories.users_repository_fake import FakeUsersRepository
from app.repositories.protocols.i_users_repository import IUsersRepository
from app.repositories.users_repository_sql import UsersRepositorySql

from app.factories.users_factory import UsersFactory
from app.services.users_service import UsersService

# 1. Factory de repositories (à compléter)

def build_users_repository(settings, db : Session | None = None) -> IUsersRepository:
    """
    Construit le repository Users en fonction du profil applicatif
    Si APP_PROFILE == "fake" -> FakeUsersRepository
    - Si APP_PROFILE = "sql" -> UsersRepositorySql
    """
    #TODO
    #1. Vérifier settings.app_profile
    #2. Si fake :
    #   - instancier UsersFactory
    #   - retourner FakeUsersRepository(factory, settings.users_json_path)
    #3. Si sql :
    #   - vérifier que db n'est pas None
    #   - retourner UsersRepositorySql(db)
    #4. Sinon, lever une exception ValueError
    if settings.app_profile == "fake" or settings.users_backend == "fake":
        factory = UsersFactory()
        return FakeUsersRepository(factory, settings.users_json_path)
    elif settings.app_profile == "sql" or settings.users_backend == "db":
        if db is None:
            raise RuntimeError("Database session is required for SQL repository")
        return UsersRepositorySql(db)
    else:
        raise ValueError("pas de APP_PROFILE:")
    
# 2. Fournisseur unique de service 
def get_users_service(settings = None, db: Session = Depends(get_db)) -> UsersService:
    """
    Dépendance FastAPI principale pour fournir une instance de UsersService.
    Cette fonction :
    - lit les settings
    - construit le repository adéquat
    - construit et retourne le service

    Important : 
    Le routeur ne connaît jamais le repository.

    """
    settings = get_settings()
    repo = build_users_repository(settings, db = db)
    return UsersService(repo)
 #TODO: construire le service avec le repo construit, pas de coupling fort entre la dépendance et le service, on utilise pas directement le service pour construire le repo, c'est la dépendance qui orchestre tout ça


    #TODO: 
    #repo = build_users_repository(settings, db = db)
    #return UsersService(repo)
    raise NotImplementedError