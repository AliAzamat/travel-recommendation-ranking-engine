from psycopg_pool import ConnectionPool
from psycopg.rows import dict_row

from app.config import settings

# One pool for the whole process: connections are created once and reused.
pool = ConnectionPool(
    settings.database_url,
    min_size=settings.pool_min,
    max_size=settings.pool_max,
    kwargs={"row_factory": dict_row},
    open=True,
)


def query(sql: str, params: dict) -> list[dict]:
    """Borrow a connection from the pool, run a read, return rows."""
    with pool.connection() as conn, conn.cursor() as cur:
        cur.execute(sql, params)
        return cur.fetchall()
