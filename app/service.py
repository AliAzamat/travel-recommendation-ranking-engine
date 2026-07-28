from app.repository import fetch_candidates
from app.personalization import affinity_tags
from app.scoring import score, Weights

DEFAULT_WEIGHTS = Weights()


def recommend(
    user_id: str,
    city: str,
    max_price: float,
    liked_tags: set[str],
    limit: int = 10,
) -> list[dict]:
    # Revealed taste from history reinforces what the user explicitly asked for.
    liked = liked_tags | affinity_tags(user_id)
    rows = fetch_candidates(city, max_price)
    scored = [
        {**row, "score": score(row, liked, max_price, DEFAULT_WEIGHTS)}
        for row in rows
    ]
    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored[:limit]
