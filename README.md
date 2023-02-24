# TEST TASK

Приложение разработано на Django для прохождения тестового задания. В качестве СУБД используется sqlite3 при запуске без докера, в докере используется postgresql. При необходимости можно настроить работу с другими СУБД, добавив переменные окружения и внеся изменения в settings/prod.py

## Установка и запуск

1. Склонировать репозиторий с Github:

````
git clone git@github.com:Lumbril/test-task-for-stripe.git
````

2. Перейти в директорию проекта
3. Создать виртуальное окружение:

````
python -m venv venv
````

4. Активировать окружение: 

````
source \venv\bin\activate
````
5. Файл .envEx переименовать в .env и изменить данные в нем на подходящие вам (Переменная LEVEL имеет два значения: PROD и LOCAL (default=LOCAL))
6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:
```
python manage.py makemigrations
python manage.py migrate
```
8. Запустить сервер
```
python manage.py runserver
```

***
## Установка проекта с помощью docker-compose


1. Склонировать репозиторий с Github
```
git clone git@github.com:Lumbril/test-task-for-stripe.git
```
2. Перейти в директорию проекта
3. Файл .envEx переименовать в .env и изменить данные в нем на подходящие вам (Переменная LEVEL имеет два значения: PROD и LOCAL (default=LOCAL)) 
4. Запустить контейнеры 
``` 
docker-compose up -d
 ```
5. Остановка работы контейнеров 
```
docker-compose stop
```
***

