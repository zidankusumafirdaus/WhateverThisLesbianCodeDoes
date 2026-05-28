# test_db_sqlalchemy.py
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("SQLALCHEMY_DATABASE_URL")
if not uri:
    raise SystemExit("Environment variable SQLALCHEMY_DATABASE_URL tidak ditemukan")

engine = create_engine(uri, pool_pre_ping=True, connect_args={"connect_timeout": 5})

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("OK, query returned:", result.scalar())
except Exception as e:
    print("Gagal koneksi / query:", type(e).__name__, "-", e)