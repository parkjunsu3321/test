from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from dependencies.database import provide_session, Session
from domains.users.dto import LoginUser, User, Showings
from domains.users.models import UserModel
from dependencies.auth import verify_password,create_access_token, hash_password
from domains.users.services import UserService


name = "users"
router = APIRouter()

@router.post("/login")
def login_user(lg_user: LoginUser, db: Session = Depends(provide_session)):
    result, token = UserService.login_service(lg_user, db)
    return {"message": result, "token": token}

    

@router.post("/register", response_model=User)
def register_user(user: User, db: Session = Depends(provide_session)):
    user_service = UserService(db)  # UserService 인스턴스 생성
    db_user = user_service.register_user(user)  # 서비스 계층에서 회원가입 로직 처리
    return db_user  # 클라이언트에 결과 반환

@router.get("/screening_seet")
def screening_seet(seattype:str, db:Session = Depends(provide_session)):
    user_service = UserService(db)  # UserService 인스턴스 생성
    showings:Showings = user_service.get_seat(seattype=seattype)
    fruits = list(map(int, showings.seat_number.split(',')))
    return fruits

@router.post("/screening", response_model=Showings)
def screening(payload:Showings):
    
    return 0