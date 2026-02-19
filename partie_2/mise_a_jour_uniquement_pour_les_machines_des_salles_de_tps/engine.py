
"""
Author : AISSANI Yannel
Version : 2026
"""

from __future__ import annotations

from sqlalchemy import create_engine
from app.core.settings import get_settings


def get_engine():

    import sys
    try:
        import pysqlite3 as sqlite3
        sys.modules["sqlite3"] = sqlite3
    except ImportError:
        pass
    
    """
    Construit l'engine SQLAlchemy à partir de Settings.database_url.
    """
    settings = get_settings()
    return create_engine(settings.database_url, echo=False)
