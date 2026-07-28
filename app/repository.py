from app.db import query


def fetch_candidates(city: str, max_price: float, limit: int = 500) -> list[dict]:
    """Pull the rows worth ranking — the DB does the cheap, selective filter."""
    sql = """
        SELECT id, city, kind, price_per_night, rating, tags,
               EXTRACT(EPOCH FROM (now() - updated_at)) / 86400.0 AS days_old
        FROM listings
        WHERE city = %(city)s AND price_per_night <= %(max_price)s
        ORDER BY rating DESC, id ASC
        LIMIT %(limit)s
    """
    return query(sql, {"city": city, "max_price": max_price, "limit": limit})


def fetch_page(city: str, max_price: float, offset: int, limit: int) -> list[dict]:
    """A stable page of the catalog: deterministic order, then OFFSET/LIMIT."""
    sql = """
        SELECT id, city, kind, price_per_night, rating, tags
        FROM listings
        WHERE city = %(city)s AND price_per_night <= %(max_price)s
        ORDER BY rating DESC, id ASC          -- tiebreak by id → deterministic
        OFFSET %(offset)s LIMIT %(limit)s
    """
    return query(sql, {"city": city, "max_price": max_price,
                       "offset": offset, "limit": limit})
