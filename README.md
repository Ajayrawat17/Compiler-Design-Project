# 💻 Code Box – Online Python Compiler

> A full-stack web application that allows users to write, compile, and execute Python code directly in the browser. Built with ReactJS on the frontend and Django on the backend, featuring a custom-built compiler and secure code execution pipeline.

---

## 📚 Table of Contents

- [Overview](#overview)
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

## 📖 Overview

**Code Box** is a compiler project developed as part of Compiler Design & Software Engineering curriculum. It offers a simple yet powerful platform to write Python code in the browser, send it to the backend, and get the output in real time. The project demonstrates full-stack development, API integration, and compiler concepts.

---

## 🚀 Tech Stack

### Frontend:
- ReactJS
- Axios
- HTML5 + CSS3

### Backend:
- Django
- Django REST Framework
- Python (Custom Compiler Logic)

### Tools:
- Git & GitHub
- VS Code
- Postman (for API testing)

---

## ✅ Features

- Live Python code execution from browser
- Secure backend code evaluation
- Modular compiler logic in Python
- REST API-based communication
- Real-time input-output processing
- Clean and responsive UI

---

## 📁 Project Structure

CodeBox/
├── frontend/ # ReactJS codebase
│ ├── src/
│ └── public/
├── backend/ # Django backend + API
│ ├── compiler/ # Custom compiler logic
│ └── codebox/ # Django app files
├── venv/ # Python virtual environment
├── .gitignore
├── README.md

yaml
Copy
Edit

---

## ⚙️ Installation

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/Ajayrawat17/Compiler-Design-Project.git
cd Compiler-Design-Project
�� 2. Backend Setup (Django)
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

pip install -r requirements.txt
python manage.py runserver
🔹 3. Frontend Setup (ReactJS)
bash
Copy
Edit
cd frontend
npm install
npm start
▶️ Usage
Go to http://localhost:3000

Type Python code into the editor

Click "Run"

Code is sent to the backend via API

Backend processes & executes the code

Output is returned and shown in the browser


👨‍�� Author
Ajay Rawat
🎓 B.Tech (CSE), Graphic Era Hill University
📫 ajayrawat11146@gmail.com
🔗 GitHub: Ajayrawat17

📄 License
This project is open-source and available under the MIT License.
