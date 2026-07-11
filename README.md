# 📋 TaskFlow – Student Task Management System

<div align="center">

### Organize Your Tasks. Track Your Progress. Achieve Your Goals.

A modern full-stack productivity platform built to help students efficiently manage assignments, projects, deadlines, and daily activities through an intuitive, responsive, and productivity-focused interface.

<br>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</div>

---

# 🌟 Overview

TaskFlow is a modern full-stack Student Task Management System designed to simplify the way students organize academic responsibilities, personal commitments, and project deadlines.

Built using **Flask**, **SQLAlchemy**, and **Bootstrap 5**, the application combines secure authentication, intelligent task organization, real-time dashboard analytics, and calendar-based scheduling into a seamless productivity experience.

Rather than functioning as a simple to-do application, TaskFlow provides a centralized workspace where users can efficiently plan, prioritize, monitor progress, and stay focused throughout their academic journey.

---

# 💡 Why TaskFlow?

Managing assignments, examinations, projects, and personal responsibilities simultaneously can quickly become overwhelming.

TaskFlow was developed to solve this challenge by providing a clean, intuitive, and productivity-focused environment where students can organize their work efficiently, monitor their progress, and stay ahead of deadlines.

The platform emphasizes simplicity, usability, and performance while delivering the essential tools needed for effective task management.

---

# ✨ Project Highlights

- 🔐 Secure User Authentication
- 📊 Interactive Productivity Dashboard
- ✅ Complete Task Management System
- 📅 Calendar-Based Deadline Tracking
- 🔍 Real-Time Search & Filtering
- 🗂️ Custom Categories & Priorities
- 🌙 Premium Dark Theme
- 📱 Fully Responsive Design
- ⚡ Keyboard Shortcuts
- 🎯 Clean and User-Friendly Interface

---

# 🚀 Live Demo

### 🌐 Live Application

> 🌐 Live Website: https://taskflow-9cuj.onrender.com



---

# 🖥️ Application Walkthrough
## 🔐 Authentication Module

Secure user authentication with password hashing, protected sessions, and CSRF protection.
<img width="1319" height="603" alt="WhatsApp Image 2026-07-11 at 4 39 01 PM" src="https://github.com/user-attachments/assets/edae64d6-549e-4c70-a005-9d83d0304d74" />
## 📊 Dashboard

Monitor your productivity through an interactive dashboard displaying task statistics, pending work, completed tasks, and overdue activities.
<img width="1363" height="628" alt="WhatsApp Image 2026-07-11 at 4 40 14 PM" src="https://github.com/user-attachments/assets/e1276d06-d03a-46e0-902a-50cb31a413e6" />

## ✅ Task Management

Create, update, prioritize, search, filter, and manage daily tasks through an intuitive and responsive interface.
<img width="1365" height="622" alt="WhatsApp Image 2026-07-11 at 4 40 41 PM" src="https://github.com/user-attachments/assets/9fbece2b-4f41-4a9e-b358-813beba29f00" />

## ➕ Create New Task

Quickly add new assignments, projects, personal tasks, and deadlines with custom priorities and categories.
<img width="1360" height="619" alt="image" src="https://github.com/user-attachments/assets/81a1edb8-c97c-413a-8537-1427a2d7bd3c" />

## 📅 Calendar View

Visualize upcoming deadlines, today's schedule, and overdue activities using the integrated calendar interface.
<img width="1354" height="627" alt="WhatsApp Image 2026-07-11 at 4 41 06 PM" src="https://github.com/user-attachments/assets/dd705418-27a1-471c-8cb5-3deeff3afc15" />

## 👤 Profile Management

Update profile information, change passwords securely, and personalize account settings.
<img width="1365" height="632" alt="WhatsApp Image 2026-07-11 at 4 41 29 PM" src="https://github.com/user-attachments/assets/afa2d34c-6fe5-46a9-b9a3-04f385cfc88a" />


# ✨ Features

## 🔐 Authentication & Security

- User Registration
- Secure Login & Logout
- Password Hashing
- Session Management
- Protected Routes
- CSRF Protection

---

## 📋 Task Management

- Create Tasks
- Edit Tasks
- Delete Tasks
- Mark Tasks as Complete
- Task Prioritization
- Custom Categories
- Drag & Drop Task Ordering
- Search Tasks
- Filter Tasks
- Pagination Support

---

## 📊 Productivity Dashboard

- Total Tasks
- Pending Tasks
- Completed Tasks
- Overdue Tasks
- Task Statistics
- Productivity Overview

---

## 📅 Calendar Integration

- Upcoming Deadlines
- Today's Tasks
- Overdue Tasks
- Calendar-Based Navigation

---

## 🎨 User Experience

- Premium Dark Theme
- Responsive Design
- Animated Loading Screen
- Toast Notifications
- Sidebar Navigation
- Theme Switching
- Keyboard Shortcuts
- Clean Modern UI

---

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| **Programming Language** | Python |
| **Backend Framework** | Flask |
| **Database** | SQLite |
| **ORM** | SQLAlchemy |
| **Authentication** | Flask-Login |
| **Forms & Validation** | Flask-WTF |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Icons** | Font Awesome |
| **Deployment** | Render |
| **Version Control** | Git & GitHub |

---

# 🏗️ Application Architecture

```text
                     User
                       │
                       ▼
                Flask Application
                       │
        ┌──────────────┼──────────────┐
        │                              │
 Authentication                 Task Management
        │                              │
        └──────────────┬──────────────┘
                       ▼
                 SQLAlchemy ORM
                       │
                       ▼
                 SQLite Database
```

---

# 📂 Project Structure

```text
TaskFlow/
│
├── app.py
├── config.py
├── extensions.py
├── forms.py
├── models.py
├── requirements.txt
│
├── instance/
│   └── database.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── tasks.html
    ├── add_task.html
    ├── edit_task.html
    ├── calendar.html
    └── profile.html
```

---

# ⚙️ Getting Started

## Clone the Repository

```bash
git clone https://github.com/ohemanth/TaskFlow.git
```

---

## Navigate to the Project

```bash
cd TaskFlow
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

---

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

---

Visit

```text
http://127.0.0.1:5000
```

---

# ⚡ Productivity Shortcuts

| Shortcut | Description |
|-----------|-------------|
| **N** | Create a New Task |
| **/** | Focus Task Search |

---

# 🚀 Future Roadmap

TaskFlow is designed with scalability and future expansion in mind. Planned enhancements include:

- 🤖 AI-powered task prioritization and intelligent productivity recommendations
- 📅 Google Calendar & Outlook synchronization
- ☁️ Cloud database integration with PostgreSQL
- 🔔 Email and push notification reminders
- 👥 Team collaboration and shared workspaces
- 📈 Advanced productivity analytics and reporting
- 📱 Progressive Web App (PWA) support
- 📲 Native Android & iOS applications
- 🎤 Voice-based task creation
- 🔒 Google & GitHub OAuth authentication
- 🌍 Multi-language support
- 📊 Personalized productivity insights powered by AI

---

# 👨‍💻 About the Developer

## Obulampally Hemanth Kumar

AI Engineer • Full Stack Developer

Passionate about building intelligent software that solves real-world problems through Artificial Intelligence, Full Stack Development, and continuous research. I enjoy transforming innovative ideas into scalable software products while constantly learning and exploring emerging technologies.

### 📬 Connect with Me

- **GitHub:** https://github.com/ohemanth
- **LinkedIn:** https://linkedin.com/in/hemanth-kumar-a9b15525a
- **Email:** ohemanthkumar8765@gmail.com
- **Portfolio:** Coming Soon

---

# 🤝 Contributing

Contributions, feature suggestions, and improvements are always welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

### Building intelligent software that solves real-world problems.

Made with ❤️ by **Obulampally Hemanth Kumar**

</div>


