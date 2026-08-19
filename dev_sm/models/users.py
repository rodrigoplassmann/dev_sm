from datetime import datetime
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from dev_sm.models import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    github_profile_url: Mapped[Optional[str]] = mapped_column(
        unique=True, default=None
    )
    linkedin_profile_url: Mapped[Optional[str]] = mapped_column(
        unique=True, default=None
    )
    password: Mapped[str]
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
