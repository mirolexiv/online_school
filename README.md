# 🎓 Online School (Django Project)

Веб-додаток онлайн-школи, створений на Django.
Проєкт включає систему уроків, користувачів та форм.

## 🚀 Демо

🔗 Live: https://online-school-38x8.onrender.com/

login: admin
password:123

## 🛠️ Технології

* Python 3
* Django 6
* PostgreSQL
* Gunicorn
* Whitenoise
* Render (деплой)

## 📁 Структура проєкту

```
online_school/
├── online_school/     # основні налаштування Django
├── lessons/           # додаток уроків
├── users/             # користувачі
├── form_app/          # форми
├── static/            # статичні файли
├── templates/         # HTML шаблони
├── manage.py
├── requirements.txt
├── Procfile
├── build.sh
```

---

## ⚙️ Локальний запуск

### 1. Клонувати репозиторій

```
git clone https://github.com/mirolexiv/online_school.git
cd online_school
```

---

### 2. Створити віртуальне середовище

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Встановити залежності

```
pip install -r requirements.txt
```

---

### 4. Створити `.env`

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*

# SQLite (локально) або PostgreSQL
DATABASE_URL=postgres://user:password@host:5432/db_name
```

---

### 5. Міграції

```
python manage.py migrate
```

---

### 6. Запуск сервера

```
python manage.py runserver
```

---



## 📌 Автор

GitHub: https://github.com/mirolexiv


