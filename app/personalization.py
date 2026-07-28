from app.repository import _conn


def affinity_tags(user_id: str, limit: int = 50) -> set[str]:
    """Tags from listings the user recently CLICKED or BOOKED — their revealed taste."""
    sql = """
        SELECT DISTINCT unnest(l.tags) AS tag
        FROM interactions i
        JOIN listings l ON l.id = i.listing_id
        WHERE i.user_id = %(user_id)s AND i.action IN ('click', 'book')
        ORDER BY tag
        LIMIT %(limit)s
    """
    with _conn() as conn, conn.cursor() as cur:
        cur.execute(sql, {"user_id": user_id, "limit": limit})
        return {r["tag"] for r in cur.fetchall()}
