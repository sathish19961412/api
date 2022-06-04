from fastapi.middleware.cors import CORSMiddleware
from fastapi import  FastAPI
import os
import sys
import logging
import traceback
# from router.api import router
# from endpoints.main import  router
# from user import user
from user import api_router
logger = logging.getLogger(__name__)


app = FastAPI(title="backend")

origins= [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(api_router)