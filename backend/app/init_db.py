import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import engine
from models import Base


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
