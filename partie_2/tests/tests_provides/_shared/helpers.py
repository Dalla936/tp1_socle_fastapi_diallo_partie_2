from __future__ import annotations

from pathlib import Path
import json


def write_users_json(path: Path, users_payload) -> Path:
    """Write a minimal users.json file for tests."""
    payload = {"users": users_payload}
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path
