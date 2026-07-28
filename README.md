# Recommendation Ranking Engine with Postgres

A production-shaped ranking engine. The catalog in Postgres with indexes, weighted/normalized feature scoring, blended with personalization from a user's interaction history, and serves ranked results through a clean repository layer behind FastAPI. The anchor is a /recommendations endpoint that ranks thousands of stays per traveler in milliseconds.

## Stack
- Python
- PostgreSQL
- SQL
- FastAPI
- psycopg
