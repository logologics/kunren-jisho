from fastapi import APIRouter
import httpx

router = APIRouter()

jisho = 'https://jisho.org/api/v1/search/words?keyword='

@router.get("/search/{query}")
async def search(query: str):
  async with httpx.AsyncClient() as client:
    r = await client.get(jisho + query)
    return {"query": r.json()}