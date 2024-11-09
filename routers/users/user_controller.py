from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from dependencies.database import provide_session, Session
from domains.users.dto import LoginUser, User, MovieAddDTO, InputDTO, BookingDTO
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
    return db_user 

@router.get("/screening_seat")
def screening_seet(db: Session = Depends(provide_session)):
    user_service = UserService(user_repository=UserRepository(session=db))  # UserService 인스턴스 생성
    showings = user_service.get_seat()
    return showings


@router.post("/update")
def update_mv(payload:InputDTO, db: Session = Depends(provide_session)):
    screen_service = UserService(user_repository=UserRepository(session=db))
    redata = screen_service.update_showings(payload=payload)
    print(redata)
    return redata

@router.post("/booking")
def booking_mv(payload:BookingDTO ,db:Session = Depends(provide_session)):
    screen_service = UserService(user_repository=UserRepository(session=db))
    redata = screen_service.booking_showings(payload=payload)
    return redata