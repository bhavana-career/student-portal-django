# 🎓 Student Course Registration Portal (Django)

A web-based application built using Django that allows students to register for courses, view enrolled courses, and manage student data efficiently.

---

## 📌 Project Overview

This project demonstrates the use of Django for building a dynamic web application. It includes both Function-Based Views (FBV) and Generic Class-Based Views (CBV) such as ListView and DetailView to display student data and details.

---

## Features

* Student Registration with course selection
* Course listing and management
* Filter students based on enrolled courses
* Display list of students using ListView (CBV)
* View detailed information of a selected student using DetailView (CBV)
* Many-to-Many relationship between Students and Courses
* Simple UI using HTML & CSS

---

##  Concepts Used

* Django Models & ORM
* Function-Based Views (FBV)
* Generic Class-Based Views (ListView, DetailView)
* URL Routing
* Templates & Template Inheritance
* Forms handling (GET/POST)
* Database migrations (SQLite)

---

## Tech Stack

* Python 3.x
* Django
* HTML5
* CSS3
* SQLite3

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/bhavana-career/student-portal-django.git
cd student-portal-django
```

### 2. Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

### 6. Open in Browser

http://127.0.0.1:8000/

---

## 📂 Project Structure

```
Studentproject/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
├── static/
├── manage.py
```

---

##  Screenshots

<img width="1596" height="802" alt="image" src="https://github.com/user-attachments/assets/f6a26165-c1cf-4d25-aec7-f7e86657ddce" />


##  Author

Bhavana S

---

## 📌 Future Improvements

* User authentication (login/signup)
* Admin dashboard enhancements
* Responsive UI
* Deployment (Render/Heroku)

---
