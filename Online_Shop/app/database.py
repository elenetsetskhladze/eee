from sqlalchemy import create_engine
<<<<<<< HEAD
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:Elene!123@localhost:5432/Online_Shop"
=======
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql://postgres:Elene!123@localhost:5432/homework42"
>>>>>>> 31e6cbabc407509ec51ddc3452de5676eedca4d4

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

<<<<<<< HEAD
=======
Base = declarative_base()

>>>>>>> 31e6cbabc407509ec51ddc3452de5676eedca4d4
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

<<<<<<< HEAD
class Base(DeclarativeBase):
    pass








=======
>>>>>>> 31e6cbabc407509ec51ddc3452de5676eedca4d4
