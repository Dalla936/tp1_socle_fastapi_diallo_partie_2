import os
from dotenv import load_dotenv


class Settings:
    """
    Objet de configuration de l'application.
    Centralise l'accès aux variables d'environnement.

    - Charge le fichier .env s'il existe (python-dotenv)
    - Expose des propriétés utilisées par l'application
    """

    def __init__(self) -> None:
        # Charge .env si présent (n'écrase pas les variables déjà définies)
        load_dotenv(override=False)

        self.users_json_path: str = os.getenv("USERS_JSON_PATH", "data/users.json")
