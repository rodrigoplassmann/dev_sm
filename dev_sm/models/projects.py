from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dev_sm.models import Base

if TYPE_CHECKING:
    from dev_sm.models import User


class Project(Base):
    __tablename__ = 'projects'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    discord_server_url: Mapped[str] = mapped_column(String(255), unique=True)
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
    users: Mapped[List[User]] = relationship(
        secondary='project_users', back_populates='projects'
    )
    tags: Mapped[List[Tag]] = relationship(
        secondary='project_tags', back_populates='projects'
    )


class Tag(Base):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    projects: Mapped[List[Project]] = relationship(
        secondary='project_tags', back_populates='tags'
    )


class ProjectUser(Base):
    __tablename__ = 'project_users'
    project_id: Mapped[int] = mapped_column(
        ForeignKey('projects.id'), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), primary_key=True
    )


class ProjectTag(Base):
    __tablename__ = 'project_tags'
    project_id: Mapped[int] = mapped_column(
        ForeignKey('projects.id'), primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id'), primary_key=True
    )
