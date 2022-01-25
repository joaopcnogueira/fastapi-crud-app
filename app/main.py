from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import post, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI",
    description="From the youtube freecodecamp course 🚀"
)

app.include_router(post.router)
app.include_router(user.router)

