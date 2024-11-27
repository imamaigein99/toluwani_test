from fastapi import HTTPException, Request
from .config import settings


def validate_request(tag: str, client_id: str, client_secret: str) -> None:
    settings_tag = settings.tag
    settings_clients = settings.clients

    # Check if the tag is valid
    if tag != settings_tag:
        raise HTTPException(status_code=400, detail="Invalid tag")

    # Check if the client ID and client secret are valid
    if client_id not in settings_clients or settings_clients[client_id] != client_secret:
        raise HTTPException(status_code=400, detail="Invalid client credentials")