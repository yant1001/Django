# Django
- 파이썬으로 작성된 웹 프레임워크
  - 프레임워크: 반복적으로 사용되는 특정 기술을 모아 놓은 도구 상자와 같은 기능(코드 조각)

## 핵심기능
  - DB 관리
  - 강력한 관리자 기능
  - 보안

## 과정1 (출력되는 페이지가 **1개**일 떄)
  1. 사용자가 내 컴퓨터의 브라우저에서 python.org 입력
  2. 주소가 인터넷을 거쳐 어딘가의 컴퓨터로 보내진다.
  3. 인터넷을 통해 python.org 주소에 해당하는 컴퓨터에 응답 요청
  4. 요청에 대한 응답 페이지를 생성한다.
  5. 다시 인터넷을 통해 내 컴퓨터 브라우저로 응답 전송
  6. 브라우저에서 이 내용을 출력
  7. 사용자는 출력(표시)된 내용을 화면에서 확인한다.

## 과정2 (여러 페이지가 존재하고, 그중 **특정 페이지**를 요청할 때)
  - 사용자가 서버에게 python.org만 입력하면, 뒤에 추가 경로가 없으니 기본 페이지가 반환된다.
  - 사용자가 서버에게 python.orl/**downloads**를 입력하면 지정 경로에 의해 다운로드 페이지를 반환한다.
    - 추가로 입력한 텍스트는 특정 페이지를 요청하는데 사용된다.
    - 이 텍스트는 URL(Uniform Resource Locator)이라고 부르며, 웹사이트를 찾기 위한 주소를 의마한다.



# Django의 원리 이해하기
- `request`(요청)가 들어와서 `response`(응답)가 나간다. == SW 메이커 역할

## 장고가 요청에 응답하는 방법
1. URL로 사용자의 요청`request`이 전달된다.
2. 요청을 받으면 URLconf(URL 설정)가 요청을 전달한다.
3. URLconf가 요청이 어떤 페이지를 요구하는지 구분한다.
4. 요청에 응답할 수 있는 함수 **View** 로 요청을 전달한다.
   1. View는 함수이기 때문에, 입력값을 처리해 반환해준다.
   2. 외부 URL로부터 `request`를 입력값으로 받아 브라우저에 표시할 수 있는 내용을 반환하는 로직이다.
   3. View는 페이지들의 목록이 들어있고, 예를 들어 `main` 페이지 직원, `downloads` 페이지 직원, `about` 페이지 직원 등이 있다.
5. View 함수는 요청을 처리한 후 응답`response`을 만들어 되돌려준다.
6. 응답은 요청자의 브라우저로 전달되며, 브라우저는 응답을 해석해서 사용자에게 보여준다.

## 장고의 MTV 패턴
- Model - Template - View
- 디자인 패턴의 일종으로, 코드를 작성하기 위한 일종의 서식을 의미한다.
- `Model`
  - 장고와 데이터베이스를 연결시켜주는 코드이다.
  - 각각의 모델은 데이터베이스 테이블과 연결된다.
  - 파이썬의 클래스를 사용한다. (ex. `Class Board(models.Model):`)
  - 각각의 모델 속성은 데이터베이스 필드를 나타낸다.
  - `models.py`를 파일명으로 사용한다.
- `Template`
  - 웹 브라우저로 돌려줄 코드이다.
  - 사용자에게 제공될 결과물의 형태이다.
  - `templates` 디렉터리 내에 `HTML` 파일을 사용해서 나타낸다.
- `View`
  - 사용자의 요청을 받아 처리하는 웹 사이트의 로직을 가지는 코드이다.
  - (사용자의 요청을 처리해줄 수 있는 직원들의 목록이 존재한다.)
  - 파이썬의 함수를 사용한다. (ex. `def board_list(request):`)
  - `views.py`를 파일명으로 사용한다.

## 루프백 주소로의 요청
- 외부 네트워크(인터넷)로의 요청
  - 사용자가 브라우저 주소 표시줄에 python.org를 입력한다.
  - 컴퓨터 외부의 네트워크(인터넷)에 **요청**을 보낸다.
  - 즉 python.org라는 특정 주소에 위치하는 서버(컴퓨터)에 요청을 보낸다.
  - 해당 컴퓨터가 처리하여 **응답**을 돌려준다.
- 내부 네트워크 어댑터의 역할
  - 상기 과정에서 브라우저와 외부 네트워크 사이 랜카드(네트워크 어댑터)가 존재한다.
  - 랜카드는 내부와 외부의 요청/응답을 중계하는 역할을 한다.
  - 브라우저와 랜카드는 사용자의 컴퓨터에 속해있다.
  - 사용자가 브라우저 주소 표시줄에 입력한 주소는 랜카드가 해석하여 외부 네트워크(인터넷)에 전달한다.
- 루프백 주소로의 요청 전달
  - 루프백 주소는 주소표시줄에 `localhost`나 `127.0.0.1`을 입력한 형태이다.
  - 루프백 주소를 입력하면, 랜카드에서 외부 네트워크로 전달되어 나가지 않고 개발서버(runserver)로 전달되어 마치 외부에서 사용자 컴퓨터로 전달한 것처럼 내부 시스템으로 다시 요청이 전달된다.
  - `127.0.0.1:8000` => `127.0.0.1`은 요청을 전달할 루프백 주소, `8000`은 컴퓨터의 포트 번호를 의미한다.