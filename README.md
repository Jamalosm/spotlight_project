# 🚀 Spotlight Advertising – Lead Generation System

A production-ready lead generation web application built using **Django, Celery, Redis, Tailwind CSS, and JavaScript**. This project captures user enquiries, stores them in the database, and processes notifications asynchronously.

---

# 📌 FEATURES

* 🔥 Modern single-page responsive UI
* 📩 Lead capture (multiple forms)
* 🧠 Clean architecture (views → services → models)
* ⚡ Async email sending using Celery + Redis
* 📧 Gmail SMTP integration
* 📊 Django Admin dashboard (filter, search, status update)
* 📁 CSV export of leads
* 📱 WhatsApp integration (pre-filled message)
* 🎨 Premium UI (glass effect, animations, gradient)

---

# 🗂️ PROJECT STRUCTURE

```
spotlight_project/
│
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   ├── prod.py
│   ├── celery.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── core/
│   │   ├── views.py
│   │   └── urls.py
│   │
│   └── leads/
│       ├── models.py
│       ├── views.py
│       ├── admin.py
│       ├── tasks.py
│       ├── services/
│       │   └── lead_service.py
│       └── migrations/
│
├── templates/
│   └── home.html
│
├── static/
├── media/
├── .env
├── manage.py
└── requirements.txt
```

---

# ⚙️ ENVIRONMENT VARIABLES (.env)

Create a `.env` file in root:

```
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

---

# 🛠️ INSTALLATION

### 1️⃣ Clone project

```
git clone <your-repo>
cd spotlight_project
```

### 2️⃣ Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate   (Windows)
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# 🧱 DATABASE SETUP

```
python manage.py makemigrations
python manage.py migrate
```

---

# 🔥 RUN PROJECT

### 1️⃣ Start Redis

```
redis-server --port 6380
```

### 2️⃣ Start Celery Worker

```
celery -A config worker --pool=solo --loglevel=info
```

### 3️⃣ Run Django Server

```
python manage.py runserver --settings=config.settings.dev
```

---

# 🌐 ACCESS

* Website → http://127.0.0.1:8000/
* Admin → http://127.0.0.1:8000/admin/

Create admin user:

```
python manage.py createsuperuser
```

---

# 🔄 APPLICATION FLOW

```
User submits form
        ↓
Django View
        ↓
Lead saved in DB
        ↓
Celery Task Triggered
        ↓
Email sent via SMTP
        ↓
Lead visible in Admin Panel
```

---

# 🚀 FUTURE ENHANCEMENTS

* 📧 HTML Email Templates
* 🤖 Auto-reply Email to Users
* 📊 Analytics Dashboard
* 📱 WhatsApp Business API (auto-send)
* 🔐 Authentication system
* 🌍 Deployment (AWS / Docker / Nginx)
* ⚡ Performance optimization

---

# 🧠 TECH STACK

* Backend: Django
* Frontend: HTML, Tailwind CSS, JavaScript
* Queue: Celery
* Broker: Redis
* Email: SMTP (Gmail)
* DB: SQLite / PostgreSQL

---

# 💬 AUTHOR

Built as a scalable SaaS-ready system for real-world lead generation 🚀

---
