from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.service import recommend

app = FastAPI(title="Travel Ranking Engine")


class RecRequest(BaseModel):
    user_id: str
    city: str
    max_price: float = Field(gt=0)
    liked_tags: list[str] = Field(default_factory=list)
    limit: int = Field(default=10, ge=1, le=50)


@app.post("/recommendations")
async def recommendations(body: RecRequest) -> dict:
    results = recommend(
        body.user_id, body.city, body.max_price,
        set(body.liked_tags), body.limit,
    )
    return {"city": body.city, "count": len(results), "results": results}
