# 장고로 데이터 가져오고 내보내기
- DB의 종류와 상관없이 간단한 명령어를 이용해 데이터를 json, xml 등의 포맷으로 DB에 넣고 뺄 수 있다.

## 데이터 가져오기 (Load)
- `loaddata` 명령어를 이용하여 추출한 데이터를 DB에 로드하는데 사용할 수 있다.
- 아래 예시는 user.json 파일 콘텐츠를 DB에 추가하는 동작을 수행한다.
```PY
./manage.py loaddata user.json
```

## 데이터 내보내기 (BackUp)
- `dumpdata` 명령어를 이용하여 모델 인스턴스 혹은 전체 DB를 백업하는데 사용할 수 있다.
- 아래 예시는 전체 DB를 db.json 파일에 백업하는 동작을 수행한다.
```py
./manage.py dumpdata > db.json
```
### 특정 앱의 데이터만 백업할 경우
- admin 앱의 데이터를 admin.json 파일로 백업한다.
```py
./manage.py dumpdata admin > admin.json
```
### 특정 테이블의 데이터만 백업할 경우
- admin.logentry 테이블의 콘텐츠만 logentry.json 파일로 백업한다.
```py
./manage.py dumpdata admin.logentry > logentry.json
```
### 특정 데이터만 제외하기 
- `--exclude` 옵션을 사용하여 백업할 필요가 없는 앱과 테이블을 지정할 수 있다.
- 아래는 auth.permission 테이블 내용을 제외한 전체 DB를 백업한다.
```py
./manage.py dumpdata --exclude auth.permission > db.json

# 제외 항목이 2개 이상일 때
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```
### 보기 편하게 백업하기
- `--indent` 옵션을 사용하여 깔끔하게 들여쓰기된 데이터를 추출할 수 있다. (기본적으로 dumpdata는 데이터를 한 줄에 출력하기 때문에 읽기 어려움)
```py
./manage.py dumpdata auth.user --indent 2 > user.json
```
### 저장 포맷 바꾸기
- `--format` 옵션을 사용하여 형식을 바꿀 수 있다. (기본적으로 출력 형식은 json)
- 아래는 기본 출력 형태 json 대신 xml 파일을 추출한다.
```py
./manage.py dumpdata auth.user --indent 2 --format xml > user.xml
```



# DB에서 데이터프레임으로 가져오기
- ML 모델 개발 단계에선 DB가 아닌 csv 파일에서 데이터프레임을 가져와서 개발하는 경우가 있다. 하지만 실무에서는 데이터베이스를 사용해야 하기 때문에, DB에서 데이터프레임으로 가져오는 방법에 대한 연습이 필요하다.
## Django와 MySQL 연결
- settings.py에 db_settings.py를 생성하여 아래 정보를 입력한다. gitignore에 등록하려는 목적이므로, settings.py를 공개하지 않는다면 아래 과정없이 바로 추가해도 상관없다.
```py
# settings.py
import db_settings
DATABASES = db_settings.DATABASES

# db_settings.py
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',    
        'NAME': 'dbname',                  
        'USER': 'username',                          
        'PASSWORD': 'userpassword',                  
        'HOST': 'localhost',                     
        'PORT': '3306',                          
    }
}
```
## Django Migrate
- 모델 정보를 바탕으로 마이그레이션 파일을 만들고 → db에 전송하여 → 엔티티를 생성하는 과정이다.
```py
# shell
python manage.py makemigrations

# db 전송
python manage.py migrate
```
## Pandas 데이터프레임 만들기
```py
from .models import Movie
import pandas as pd

def db_dataframe_test(request):
    movies = Movie.objects.all()
    movies_df = pd.DataFrame(list(movies.values()))
    print(movies_df.head())
```