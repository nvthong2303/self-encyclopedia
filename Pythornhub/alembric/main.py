from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("postgresql+psycopg2://user-name:strong-password@127.0.0.1:5432/postgresql_test")


def app():
    with engine.connect() as conn:
        stmt = text("select * from pg_database")
        print(conn.execute(stmt).fetchall())


if __name__ == "__main__":
    app()
