from domains import Service

from dependencies.database import Session
from dependencies.auth import hash_password, verify_password, create_access_token
from .repositories import UserRepository
from .models import UserModel, MovieModel
from domains.users.dto import User, Showings, LoginUser, Movie, InputDTO, NewInputDTO

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
        payload.show_time = ','.join(map(str, payload.show_time))
        payload.seat_number = [1 if seat == 2 else seat for seat in payload.seat_number]
        payload.seat_number = ','.join(map(str, payload.seat_number))
        redata = self._user_repository.update_showing(payload=NewInputDTO(theater_name=payload.theater_name, seat_number=payload.seat_number, show_time=payload.show_time))
        return redata

    def insert_showings(self, payload:Showings):
        movie_dict = payload.movie_info
        movie = self._user_repository.movie_add(movie_info=movie_dict)
        payload.seat_number = ','.join(['0'] * 30)
        payload.movie_info = Movie(movie_id = movie.movie_id, movie_name=movie.movie_name,release_date=movie.release_date,audience_count=movie.audience_count)
        payload.show_time = ','.join(['0'] * 5)
        db_sw = self._user_repository.showings_add(payload=payload)
        return db_sw