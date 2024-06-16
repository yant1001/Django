# `request.get` vs `request.GET`
## `request.get`
- `get`은 Python의 메소드로, 딕셔니리 객체를 대상으로 한다.
- `request`라는 딕셔너리 객체에 대해 `get` 메소드를 실행한다.
- 딕셔너리 객체에 대해서만 사용이 가능함에 주의해야 한다.
- 
## `request.GET`
- `GET`은 Django의 메소드이다.
- `request`는 HTTP 요청이 보내지면 Django에서 만들어내는 객체이다. (딕셔너리 형태X)
- `reqest.GET`을 실행하면 `request`의 정보를 딕셔너리 형태로 바꿀 수 있게 된다.
  - 즉 `request.GET`을 하면 `request.get`을 보냈을 때의 데이터도 얻을 수 있다.
  - `request.POST`도 같은 원리로 작동한다.