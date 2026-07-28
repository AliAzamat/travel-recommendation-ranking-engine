# Recommendation Ranking Engine with Postgres

An intermediate project that grows the four-line scorer into a production-shaped ranking engine. You move the catalog into Postgres with indexes, learn weighted/normalized feature scoring, blend in personalization from a user's interaction history, and serve ranked results through a clean repository layer behind FastAPI. The anchor is a /recommendations endpoint that ranks thousands of stays per traveler in milliseconds.

Built step-by-step with [KhwajaLabs Build](https://khwajalabs.com).

## Stack
- Python
- PostgreSQL
- SQL
- FastAPI
- psycopg
