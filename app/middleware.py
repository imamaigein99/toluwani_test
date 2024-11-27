# app/middleware.py
import logging
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.config import settings

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get("Authorization")
        tag = request.query_params.get("tag")

        if not auth_header:
            raise HTTPException(status_code=401, detail="Unauthorized: Missing Authorization header")
        
        try:
            client_id, client_secret = auth_header.split(":")
        except ValueError:
            raise HTTPException(status_code=401, detail="Unauthorized: Invalid Authorization header format")

        valid_client = None
        for client, creds in settings.clients.items():
            if creds['client_id'] == client_id and creds['client_secret'] == client_secret and creds['tag'] == tag:
                valid_client = client
                break
        
        if not valid_client:
            raise HTTPException(status_code=401, detail="Unauthorized: Invalid credentials or tag")

        return await call_next(request)
