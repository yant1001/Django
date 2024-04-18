# Django 정참조와 역참조
- 관계되어 있는 객체에 접근해야 하는 경우, 정참조인지 역참조인지에 따라 데이터에 접근하는 방식이 다르다.
- 예를 들어, 사람과 개는 1:N 관계이다. (개=N) 이 때 개 → 사람을 참조하는 걸 정참조, 사람 → 개를 참조하는 걸 역참조라고 한다.
  - 즉, N이 1을 참조하는게 정참조이다.

## 정참조
- 정참조인 경우
  - Foreign Key 속성이 있는 객체에서 없는 개체를 참조 (N→1)
  - One to One 관계에서 참조 (1→1)
- 코드 구현 예시
    ```py
    dog = Dog.objects.get(pk=1)

    dog.owner.name
    ```

## 역참조
- 역참조인 경우
  - Foreign Key 속성이 없는 객체에서 관계된 모델을 참조 (1→N)
- 코드 구현 예시
    ```py
    # set managere을 사용한 참조

    person = Person.objects.get(name='홍길동')

    person.dog.name   # X
    person_dogs = person.dog_set.all()
    ```
    ```py
    # related_name을 사용한 참조
    class Person(models.Model)
        name = models.CharField(max_length=10)

    class Dog(models.Model)
        owner = models.ForeignKey(Person, related_name='dogs')
        name = models.CharField(max_length=20)
    ```
- related_name을 사용하는 이유
  - 여러 속성에서 같은 모델을 Foriegn Key로 가지고 있을 경우, 역참조할 때 어떤 속성에 대한 참조인지 찾지 못해 에러가 발생할 수 있다.
  - 이 때 장고에서 related_name 설정을 통해 각 필드의 이름을 구분하여 참조할 수 있도록 한다.



# all, get, values
- 각각의 차이
  - `all`은 전부 가져온다.
  - `get`은 1개만 가져온다.
  - `values`는 딕셔너리 형태로 가져온다.
  - field 값을 즉시 불러오기 위해선 object로 반환되어야 한다.
  - object 형태일때만 `i.name`과 같은 dot 형태로 field 값을 가져올 수 있다.
- **하나의 값**만 가지고 있는 경우
  - `get`을 사용한다.
  - object 형태의 string 타입으로 반한된다.
- **여러 값**을 가지고 있는 경우
  - `all`을 사용하는 경우
    - query set을 반환하기 때문에 field 값을 바로 불러오는 것은 불가능하다.
    - for문을 사용해서 query set을 object 형태로 바꿔줘야 한다.
    - 변수에 집어넣고, `i.name` 등과 같은 형태로 가져온다.
  - `values`를 사용하는 경우
    - 딕셔너리를 담고 있는 query set을 반환하기 때문에 동일하게 for문을 사용해야 한다.
    - for문을 사용해서 딕셔너리 형태로 바꿔준다.
    - `i.name`이 아닌 `i['name']`과 같은 형태로만 가져올 수 있다.