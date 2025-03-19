from fastapi import FastAPI, HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from routes import chatbot
from auth import auth
app:FastAPI = FastAPI(title="IslamOrbit")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot.router)
app.include_router(auth.router,prefix="/auth")

@app.get("/",tags=["Home"])
def index():
    return {"data": "Hi there"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app",reload=True)