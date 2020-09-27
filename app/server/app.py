from fastapi import FastAPI
import httpx
app = FastAPI()

jisho = 'https://jisho.org/api/v1/search/words?keyword='

@app.get("/")
async def welcome():
    return {"welcome"}


@app.get("/search/{query}")
async def search(query: str):
  async with httpx.AsyncClient() as client:
    r = await client.get(jisho + query)
    return {"query": r.json()}

@app.put("/store/{word}")
async def store(word: str):
    return {"welcome"}
