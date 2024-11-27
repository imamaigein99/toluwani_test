from fastapi import APIRouter, Request, HTTPException, Header
import requests
import logging
from app.config import settings
from app.services import validate_request

router = APIRouter()

logging.basicConfig(filename=settings.log_file, level=logging.INFO)

@router.get("/v2/blacklist/{phone_number}/status")
async def get_status(phone_number: str, tag: str, client_id: str, client_secret: str, request: Request):
    logging.info(f"GET /v2/blacklist/{phone_number}/status - {request.client.host}")

    # Validate the request
    validate_request(tag, client_id, client_secret)

    # Proceed with the request
    url = f"http://{settings.ip}/v2/blacklist/{phone_number}/status?tag={tag}"
    response = requests.get(url)
    return response.json()


@router.post("/v2/blacklist/{id}")
async def post_blacklist(id: str, data: dict, request: Request):
    logging.info(f"POST /v2/blacklist/{id} - {request.client.host} - {data}")
    url = f"http://{settings.ip}/v2/blacklist/{id}"
    response = requests.post(url, json=data)
    return response.json()

@router.get("/v2/blacklist/{id}/history")
async def get_history(id: str, request: Request):
    logging.info(f"GET /v2/blacklist/{id}/history - {request.client.host}")
    url = f"http://{settings.ip}/v2/blacklist/{id}/history"
    response = requests.get(url)
    return response.json()
