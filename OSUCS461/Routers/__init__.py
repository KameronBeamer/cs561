_scriptname = "Routers"

from fastapi import APIRouter
from starlette.responses import RedirectResponse
# from OSUCS461.Routers.v1 import router as v1
# from _migrations import base

router = APIRouter()
# router.include_router(v1, prefix="/v1")
router.include_router(router, prefix="/v1")

@router.get("/")
async def redirect_to_ap():
	return RedirectResponse(url="https://oregonstate.edu")


# This is not how I am supposed to do this, but I am doing it to make it work while I figure other things out
# from fastapi import FastAPI
from pydantic import BaseModel

# app = FastAPI()

class user(BaseModel):
  uuid: str
  name: str
  time_created: int

@router.get("/users")
async def get_users():
     return {user}

@router.get("/users/{user_uuid}")
async def get_user(user_uuid: str):
    return {"user_uuid": user_uuid}

@router.post("/users")
async def create_user(email: str):
    return {"user_uuid": email}
