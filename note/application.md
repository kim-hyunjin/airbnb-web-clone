**어플리케이션**

    function의 집합
    ex) airbnb room 어플리케이션
    - room 생성하기
    - room 검색하기
    - room 삭제하기
    - room 수정하기
    - room 페이지 보여주기
    - room 업로드
    - room 리뷰하기
    - room 예약하기
    ...

    ex) 리뷰 어플리케이션
    - 리뷰 작성하기
    - 리뷰 삭제하기
    - 리뷰 수정하기
    - 리뷰 나열하기
    ...

    ex) 유저 어플리케이션
    - 로그인
    - 로그아웃
    - 메시지 기능
    - 팔로우 기능
    - 룸 리스트

`devide & conquer 방식을 사용할 것이다.`

    ex) list 어플리케이션은 오직    list만 다룬다.
    ex) 예약 어플리케이션은 예약만  다룬다.

`여러 작은 function 집합을 만들고 이 모든걸 합해서 config에 import할 것임`

<Tip>
한 문장으로 어플리케이션을 표현할 수 있어야 한다.

**어플리케이션 만들기**

    \$django-admin startapp rooms(반드시 복수형으로)

`react같은 library는 그저 build하기 위해 가져다 마음껏 사용할 수 있지만, django와 같은 framework를 사용할 때는 framework의 룰에 따라야 한다.`

\$django-admin startapp을 했을 때 장고가 생성한 파일이나 폴더들은 이름을 변경하거나 삭제해선 안된다. 추가생성은 가능.

- urls.py는 url을 컨트롤.
- view.py는 사용자 화면을 컨트롤
- models.py에는 데이터베이스
  등등
