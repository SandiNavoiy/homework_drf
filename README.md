# homework_drf
Проект онлайн-обучения (REST API) с использованием Docker

Запуск проекта:
1.Клонируйте репозиторий на вашем локальном компьютере.
2. Виртуальная среда  venv/Scripts/Activate.ps1   
3. Установка зависимостей pip install -r requirements.txt
4.Выполните все миграции python manage.py migrate
5.Запуск сервера python manage.py runserver
6. Переменные окружения, храняться в файле .env 
Для его создания необходимо переименовать .env-sampel в .env и заполнить своими данными 
Пример: CACHE_ENABLED=True (по умолчанию) DATABASES_NAME= Ваше название базы данных DATABASES_USER= пользователь баз данных 
DATABASES_PASSWORD= его пароль DEBUG=True (по умолчанию) 
CACHES_LOCATION=redis://127.0.0.1:6379 - расположение доступа и порт к REDIS (по умолчанию)


Работа с Docker: 
Прежде чем начать использовать проект нужно:
Установить на ПК пакет docker.
my-python-app  - заменить на свое название приложения
Собираем образ с помощью команды: docker build -t my-python-app .
Запускаем контейнер с помощью команды: docker run my-python-app


Работа с Docker compose

ВАЖНО!
На Windows запустите подсистему WSL(или установите ее), установите в ней например Ubunty, через магазин приложений,
Установите брокер Redis (sudo apt update, sudo apt install redis-server),
и запустите его командой redis-server start
Сборка Docker образа:
docker-compose build (обязательно на Windows запустите сам Docker!)
Сделайте миграцию внутри контейнера через команду:
docker-compose exec <имя контейнера если оно было изменено вами> python manage.py migrate
(Например docker-compose exec app python manage.py migrate)

Запуск контейнера:
-docker-compose build -docker-compose up
Эти команды создадут и запустят контейнеры для Django приложения и PostgreSQL базы данных.
Откройте браузер и перейдите по адресу http://localhost:8000, чтобы использовать запустить приложение через контейнер
(Например запрос http://localhost:8000/course/)