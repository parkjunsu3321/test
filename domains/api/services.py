from domains import Service
from .repositories import APIRepository
import requests

class APIService(Service):
    def get_daily_box_office(API_KEY ,URL,date, item_per_page=10, page_no=1, multi_movie_yn=None, rep_nation_cd=None, wide_area_cd=None):
        date = date + "15"
        params = {
            "key": API_KEY,         # 발급받은 API Key
            "targetDt": date,       # 조회할 날짜 (형식: YYYYMMDD)
            "itemPerPage": item_per_page,  # 한 페이지에 출력할 항목 수
            "pageNo": page_no,      # 페이지 번호
            "multiMovieYn": multi_movie_yn,  # 다양성 영화/상업영화 구분 (Y: 다양성, N: 상업영화, default: 전체)
            "repNationCd": rep_nation_cd,  # 한국영화/외국영화 구분 (K: 한국영화, F: 외국영화, default: 전체)
            "wideAreaCd": wide_area_cd   # 상영 지역 코드 (default: 전체)
        }

        response = requests.get(URL, params=params)

        # 응답 상태 코드 확인
        if response.status_code != 200:
            return {"error": f"API 요청 실패. 상태 코드: {response.status_code}"}

        # 박스오피스 데이터 처리
        box_office_data = response.json()
        if "boxOfficeResult" not in box_office_data:
            return {"error": "데이터가 없습니다."}

        movie_list = box_office_data["boxOfficeResult"].get("dailyBoxOfficeList", [])

        if not movie_list:
            return {"error": "오늘의 박스오피스 정보가 없습니다."}
        movie_names = [movie["movieNm"] for movie in movie_list]
        # 데이터를 JSON 형식으로 반환
        return movie_names, movie_list
    

    def get_movie_posters_from_tmdb(movie_names: list, api_key: str):
        posters = []  # 포스터 URL을 저장할 리스트
    
        for movie_name in movie_names:
            search_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}&language=en-US'
            response = requests.get(search_url)
            search_results = response.json()

            if search_results['results']:
                movie_data = search_results['results'][0]
                poster_path = movie_data.get('poster_path')

                if poster_path:
                    base_url = 'https://image.tmdb.org/t/p/w500'
                    posters.append(base_url + poster_path)  # 포스터 URL 리스트에 추가
                else:
                    posters.append('No poster available for this movie.')
            else:
                posters.append('No movie found with that name.')

        return posters