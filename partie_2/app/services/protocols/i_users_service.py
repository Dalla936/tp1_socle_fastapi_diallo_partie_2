from __future__ import annotations

from typing import Protocol
from app.models.user_model import UserModel
from app.models.user_model_create import UserModelCreate


class IUsersService(Protocol):
    """
    Contrat du service applicatif Users.

    Rôle :
    - exposer les opérations métier liées aux utilisateurs,
    - orchestrer le repository,
    - rester indépendant du stockage et du framework web.
    """

    def list_users(self) -> list[UserModel]:
        """
        Retourne tous les utilisateurs.

        Returns:
            list[UserModel]
        """
        ...

    def get_user_by_id(self, user_id: int) -> UserModel | None:
        """
        Recherche un utilisateur par id.

        Args:
            user_id (int): identifiant recherché.

        Returns:
            UserModel | None
        """
        ...

    def create_user(self, payload: UserModelCreate) -> UserModel:
        """
        Crée un utilisateur.

        Args:
            payload (UserModelCreate)

        Returns:
            UserModel
        """
        ...