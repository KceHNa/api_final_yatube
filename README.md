# api_final_yatube
### Описание. 

Бэкенд для сообщества писателей постов. REST API Django.

### Как запустить проект.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://<cсылка_на_проект_в_git>api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3  yatube_api/manage.py migrate
```

Запустить проект:

```
python3 yatube_api/manage.py runserver
```

### Документация к API

Доступна по адресу http://127.0.0.1:8000/redoc/ . Здесь можно увидеть все возможные запросы к api и ответы.

---

Приятного пользования!
