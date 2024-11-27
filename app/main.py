from fastapi import FastAPI
from .routers import blacklist
from .middleware import AuthMiddleware
from .config import settings
import logging

app = FastAPI()

# Add custom middleware
app.add_middleware(AuthMiddleware)

# Include routers
app.include_router(blacklist.router)

# Set up logging
logging.basicConfig(filename=settings.log_file, level=logging.INFO, format='%(asctime)s %(message)s')
