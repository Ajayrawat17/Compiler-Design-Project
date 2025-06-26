# 💻 Code Box – Online Code Compiler

> A full-stack web application built using ReactJS and Django that allows users to write, compile, and execute Python code directly in the browser using a custom-built compiler.

---

## 📚 Table of Contents

- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Author](#author)
- [License](#license)
- [Recruiter Note](#recruiter-note)

---

## 🚀 Tech Stack

### Frontend:
- ReactJS
- Axios

### Backend:
- Django
- Django REST Framework
- Python Custom Compiler

---

## ✅ Features

- Online Python code compilation
- Real-time execution with output display
- ReactJS frontend with clean UI
- Django REST API integration
- Custom-built compiler with multiple phases
- Secure backend logic and modular architecture

---

## 📁 Project Structure


CodeBox/
├── frontend/ # ReactJS frontend code
├── backend/ # Django backend + API
├── P-C-Compiler/ # Custom compiler logic
├── venv/ # Python virtual environment
├── .gitignore


---

## ⚙️ Installation

### 🔹 Backend Setup (Django)

``bash
cd backend
python -m venv venv
source venv/bin/activate       # For macOS/Linux
venv\Scripts\activate          # For Windows

pip install -r requirements.txt
python manage.py runserver


Frontend Setup (ReactJS)
bash
Copy
Edit
cd frontend
npm install
npm start

▶️ Usage
Open the frontend in browser: http://localhost:3000

Write Python code in the editor

Click on Run

The code is sent to the Django backend via API

Custom compiler processes and executes the code

Output is returned and displayed in the browser


