from domains import Service

from dependencies.database import Session
from dependencies.auth import hash_password, verify_password, create_access_token
from .repositories import UserRepository
from .models import UserModel, MovieModel
from domains.users.dto import User, MovieAddDTO, LoginUser, InputDTO, BookingDTO

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
        return self._user_repository.add_user(user)
    
    def get_seat(self):
        showings = self._user_repository.get_seat()
        return showings
    
    def update_showings(self, payload:InputDTO):
        redata = self._user_repository.update_showing(payload=payload)
        return redata
    
    def booking_showings(self, payload:BookingDTO):
        payload.seat_number = [1 if seat == 2 else seat for seat in payload.seat_number]
        redata = self._user_repository.booking_showings(payload=payload)
        return redata