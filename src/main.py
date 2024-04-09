from fastapi import FastAPI
from src.router import router as human_router


app = FastAPI()
app.include_router(human_router)



