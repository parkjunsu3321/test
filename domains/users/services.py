from domains import Service

from dependencies.database import Session
from dependencies.auth import hash_password, verify_password, create_access_token
from .repositories import UserRepository
from .models import UserModel, LoginUser
from domains.users.dto import User, Showings


class UserService(Service):
    def __init__(
        self,
        *,
        user_repository: UserRepository,
    ):
        self._user_repository = user_repository
    
    def login_service(lg_user: LoginUser, db: Session):
        user_repo = UserRepository(db)
        user = user_repo.find_id(lg_user.id)  # 레포지토리 사용
        if user:
            if verify_password(lg_user.password, user.password):
                token = create_access_token({"sub": lg_user.id})
                return "로그인 성공", token
            else:
                return "비밀번호 불일치", None
        else:
            return "일치하는 학번 없음", None
        
    def register_user(self, user: User):
        # 비즈니스 로직 처리 (필요시 추가)
        return self.user_repo.add_user(user)  # 레포지토리의 메서드를 호출하여 데이터베이스에 저장
    
    def get_seat(self, seattype:str):
        showings = self._user_repository.get_seat(type=seattype)
        return showings