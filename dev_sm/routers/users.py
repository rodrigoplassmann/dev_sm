from fastapi import APIRouter, status
from dev_sm.db import USERS
from dev_sm.schemas.users import (
    UserSchema,
    UserListPublicSchema,
    UserPublicSchema,
)

router = APIRouter()


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=UserPublicSchema,
)
def create_user(user: UserSchema):
    user_with_id = UserPublicSchema(**user.model_dump(), id =len(USERS) + 1)
    USERS.append(user_with_id)
    return user_with_id


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=UserListPublicSchema,
)
def list_users():
    return {
        'users': [
            {
                'id': 1,
                'username': 'joao',
                'email': 'joao@gmail.com',
                'github_profile_url': 'https://github.com/joao',
                'linkedin_profile_url': 'https://www.linkedin.com/in/joao',
            },
            {
                'id': 2,
                'username': 'jose',
                'email': 'jose@gmail.com',
                'github_profile_url': 'https://github.com/jose',
            },
            {
                'id': 3,
                'username': 'andre',
                'email': 'andre@hotmail.com',
                'linkedin_profile_url': 'https://www.linkedin.com/in/andre',
            },
            {
                'id': 4,
                'username': 'pedro',
                'email': 'pedro@outlook.com',
            },
        ]
    }
