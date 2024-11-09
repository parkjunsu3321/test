from domains import Service

from dependencies.auth import hash_password
from .repositories import UserRepository
from .models import UserModel


class UserService(Service):
    def __init__(
        self,
        *,
        user_repository: UserRepository,
    ):
        self._user_repository = user_repository
