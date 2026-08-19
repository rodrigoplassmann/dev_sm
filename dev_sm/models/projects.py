from datetime import datetime

from pydantic import HttpUrl
from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from dev_sm.models import Base


class Project(Base):
    __tablename__ = 'projects'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    discord_server_url: Mapped[HttpUrl] = mapped_column(unique=True)
    current_stage: Mapped[str] = mapped_column(String(50))
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )


class Tag(Base):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)


class ProjectContributor(Base):
    __tablename__ = 'project_contributors'
    project_id: Mapped[int] = mapped_column(
        ForeignKey('projects.id'), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), primary_key=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )


class ProjectTag(Base):
    __tablename__ = 'project_tags'
    project_id: Mapped[int] = mapped_column(
        ForeignKey('projects.id'), primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id'), primary_key=True
    )
