import requests

# 영화진흥회 API URL과 발급받은 API Key
API_KEY = "0878b3e586d2b43cabce61aec20da98a"  # 자신의 API Key를 입력하세요.
URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"

def get_daily_box_office(date, item_per_page=10, page_no=1, multi_movie_yn=None, rep_nation_cd=None, wide_area_cd=None):
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
        print(f"API 요청 실패. 상태 코드: {response.status_code}")
        return

    # 박스오피스 데이터 처리
    box_office_data = response.json()
    if "boxOfficeResult" not in box_office_data:
        print("데이터가 없습니다.")
        return

    movie_list = box_office_data["boxOfficeResult"].get("dailyBoxOfficeList", [])

    if not movie_list:
        print("오늘의 박스오피스 정보가 없습니다.")
        return

    # 모든 리턴 데이터 출력
    for movie in movie_list:
        print(f"순위: {movie.get('rank', '정보 없음')}")
        print(f"영화 제목: {movie.get('movieNm', '정보 없음')}")
        print(f"영화 코드: {movie.get('movieCd', '정보 없음')}")
        print(f"개봉일: {movie.get('openDt', '정보 없음')}")
        print(f"매출액: {movie.get('salesAmt', '정보 없음')}")
        print(f"매출 비율: {movie.get('salesShare', '정보 없음')}")
        print(f"매출 증감: {movie.get('salesInten', '정보 없음')}")
        print(f"매출 증감 비율: {movie.get('salesChange', '정보 없음')}")
        print(f"누적 매출액: {movie.get('salesAcc', '정보 없음')}")
        print(f"관객수: {movie.get('audiCnt', '정보 없음')}")
        print(f"관객수 증감: {movie.get('audiInten', '정보 없음')}")
        print(f"관객수 증감 비율: {movie.get('audiChange', '정보 없음')}")
        print(f"누적 관객수: {movie.get('audiAcc', '정보 없음')}")
        print(f"스크린 수: {movie.get('scrnCnt', '정보 없음')}")
        print(f"상영 횟수: {movie.get('showCnt', '정보 없음')}")
        print(f"순위 변화: {movie.get('rankInten', '정보 없음')}")
        print(f"랭킹 신규 여부: {movie.get('rankOldAndNew', '정보 없음')}")
        print("--------------")

# 예시 호출 (2023년 11월 8일의 박스오피스 정보 가져오기)
get_daily_box_office("20231108", item_per_page=10, page_no=1, multi_movie_yn="N", rep_nation_cd="K")