from fastapi import APIRouter
from utils.func import open_api_call

router = APIRouter()



@router.get("/v1/chat",tags=["Chatbot API"])
async def chat(prompt:str):
    resp = open_api_call(prompt)
    return {"message": resp}