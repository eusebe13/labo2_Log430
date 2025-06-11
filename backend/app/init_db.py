import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import engine
from app.models import Base


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
