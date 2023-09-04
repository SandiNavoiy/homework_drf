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