from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dev_sm.models import Base

if TYPE_CHECKING:
    from dev_sm.models.projects import Project


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
    projects: Mapped[List[Project]] = relationship(
        secondary='project_users', back_populates='users'
    )
