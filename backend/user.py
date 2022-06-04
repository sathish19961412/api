from fastapi import APIRouter
from endpoint import question,adminlogin


api_router = APIRouter()


api_router.include_router(question.router)
api_router.include_router(adminlogin.router)
