from typing import Generator
from .db.session import SessionLocal

def get_db() -> Generator:
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()
