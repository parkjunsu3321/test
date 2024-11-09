from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from dependencies.database import provide_session, Session
from domains.users.dto import LoginUser, User, Showings, InputDTO
from domains.users.models import UserModel
from dependencies.auth import verify_password,create_access_token, hash_password
from domains.users.services import UserService
from domains.users.repositories import UserRepository

name = "users"
router = APIRouter()

@router.post("/login")
def login_user(lg_user: LoginUser, db: Session = Depends(provide_session)):
    result, token = UserService.login_service(lg_user, db)
    return {"message": result, "token": token}

@router.post("/register", response_model=User)
def register_user(user: User, db: Session = Depends(provide_session)):
    user_service = UserService(user_repository=UserRepository(session=db))  # UserService 인스턴스 생성
    db_user = user_service.register_user(user)  # 서비스 계층에서 회원가입 로직 처리
    return db_user  # 클라이언트에 결과 반환

@router.get("/screening_seat")
def screening_seet(db:Session = Depends(provide_session)):
    user_service = UserService(user_repository=UserRepository(session=db))  # UserService 인스턴스 생성
    showings = user_service.get_seat()
    for showing in showings:
        if showing.seat_number is not None and showing.show_time is not None:
            fruits = list(map(int, showing.seat_number.split(',')))
            showing["seat_array"] = fruits

            # show_time을 ,로 구분하여 int 리스트로 변환
            fruits2 = list(map(int, showing.show_time.split(',')))
            showing["time_array"] = fruits2
        return showings

@router.post("/screening")
def screening(payload:Showings, db: Session = Depends(provide_session)):
    screen_service = UserService(user_repository=UserRepository(session=db))
    db_sw = screen_service.insert_showings(payload)
    return db_sw

@router.post("/booking")
def booking_mv(payload:InputDTO, db: Session = Depends(provide_session)):
    screen_service = UserService(user_repository=UserRepository(session=db))
    redata = screen_service.update_showings(payload=payload)
    return 0