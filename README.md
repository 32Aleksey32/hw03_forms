# hw03_forms - спринт №4 в Яндекс.Практикум
## Спринт 4 -  Новые записи

### Добавлены следующие возможности:
- регистрация пользователя,
- вход/выход пользователя,
- восстановление пароля,
- создание записей сообщества,
- подробная информация, редактирование только своей записи,
- отображение постов пользователя,
- пагинация, раздел Об авторе, Технологии, отображения профиля пользователя.

### Настройка и запуск на компьютере
Клонируем проект:
```
https://github.com/32Aleksey32/hw03_forms.git
```
Переходим в папку с проектом:
```
cd hw03_forms
```
Устанавливаем виртуальное окружение:
```
python -m venv venv
```
Активируем виртуальное окружение:
```
source venv/Scripts/activate
```
Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Применяем миграции:
```
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```
Создаем супер пользователя:
```
python yatube/manage.py createsuperuser
```
Запускаем проект:
```
python yatube/manage.py runserver
```
После чего проект будет доступен по адресу http://127.0.0.1/

Заходим в http://127.0.0.1/admin и создаем группы и записи. После чего записи и группы появятся на главной странице.
