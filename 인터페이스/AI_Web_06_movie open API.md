# 06_movie open API

http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=ce9dadd4f55de8ecbed0a447de4ba1ea&targetDt=20200726



1. 첫페이지에서는 박스오피스 순위를 알고싶은  날짜가 입력으로 들어감.

2.  출력되는 결과는

   - 박스오피스 순위(1등, 2등 ...10등)

   - 영화 포스터 그림. (다른 API이용: DAUM등..)
   - 영화명(국문)
   - 누적 매출액(검색일 까지의)
   - 누적 관람객수( 검색일까지의)
   - 영화상세정보 버튼
     - 영화코드를 가지고 영화 상세정보 API에서 값가져올 수 있음
     - 해당 영화의 영화제목,제작년도, 장르명, 감독명, 배우명(데이터가 있는경우)
     - 위의 정보를 alert()으로 출력되게끔 처리



3. 다음 API를 이용해서 포스터 이미지 가져오기

   REST KEY: 030562ab4f7e3c0da053dff0d160bc7e

   url: https://dapi.kakao.com/v2/search/image

```javascript
$.ajax({
    async: true, //동기 or 비동기
    url: "https://dapi.kakao.com/v2/search/image",  // 호출할 서버쪽 프로그램
    data: {
        query: "영화"+item.movieNm+'"포스터"',
        sort: "accuracy"
    },
    beforeSend: function (xhr) {
        xhr.setRequestHeader('Authorization',
            'KakaoAK 030562ab4f7e3c0da053dff0d160bc7e')
    },
    type: "GET",
    timeout: 3000,
    dataType: "json",
    success: function (result2) {
        var img_list = result2.documents
        var img = $("<img/>").attr("src", img_list[0].thumbnail_url)
            .addClass("myImage")
        imgTd.append(img)
    },
    error: function (error) {
        alert("실패")

    }
})
```