<<<<<<< HEAD
from app.database import Base
from sqlalchemy import String,DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(50), default="user", nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
=======
from datetime import datetime
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    role: Mapped[str] = mapped_column(String(50), default="user", nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime (timezone=True), server_default=func.now())
>>>>>>> 31e6cbabc407509ec51ddc3452de5676eedca4d4

    def __str__(self):
        return self.username