from fastapi import FastAPI
from .routers import oauth, db, jisho

app = FastAPI()

@app.get("/")
async def welcome():
    return {"welcome"}

app.include_router(
    oauth.router,
    prefix="/oauth",
)

app.include_router(
    jisho.router,
    prefix="/jisho",
)

app.include_db(
    db.router,
    prefix="/oauth",
)



