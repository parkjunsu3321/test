from fastapi import APIRouter
import requests
from dependencies.config import get_config
from datetime import datetime
from dateutil.relativedelta import relativedelta
from domains.api.services import APIService

name = "api"
router = APIRouter()
config = get_config()

@router.get("/movie_info")
def get_movie_info():
    apiService = APIService
    M_API_KEY = config.movie_api_key  # config에서 API 키 불러오기
    Img_api_key = config.img_api_key
    today = datetime.today()
    one_year_ago = today - relativedelta(years=1)
    one_year_ago_str = one_year_ago.strftime('%Y%m%d')
    URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    print(today)
    # 요청 파라미터 설정
    names, movie_dict = apiService.get_daily_box_office(API_KEY=M_API_KEY,URL=URL,date=one_year_ago_str)
    img_url = apiService.get_movie_posters_from_tmdb(movie_names=names, api_key=Img_api_key)
    i = 0
    for movie in movie_dict:
        movie["img_url"] = img_url[i]
        i+=1
    return movie_dict