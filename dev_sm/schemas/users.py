from typing import List, Optional

from pydantic import BaseModel, EmailStr, HttpUrl


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    github_profile_url: Optional[HttpUrl] = None
    linkedin_profile_url: Optional[HttpUrl] = None
    password: str


class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    github_profile_url: Optional[HttpUrl] = None
    linkedin_profile_url: Optional[HttpUrl] = None


class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    github_profile_url: Optional[HttpUrl] = None
    linkedin_profile_url: Optional[HttpUrl] = None
    password: Optional[str] = None


class UserListPublicSchema(BaseModel):
    users: List[UserPublicSchema]
