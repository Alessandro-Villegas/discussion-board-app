# Discussion Board App

## Project Description
This app focuses on UTRGV students and enables users to post and view announcements, leave comments on their own posts and others, manage activities, discover events, and connect with the community.

## Team Members
- Alessandro Villegas
- Andres Cantu

## Tech Stack
- Frontend HTML, CSS (Django Templates), Bootstrap
- Backend: Python (Django Framework)
- Database: SQLite (development)
- Version Control: Git & GitHub
- Environment: Virtual Environment (virt)

## How to Run
git clone https://github.com/Alessandro-Villegas/discussion-board-app.git
cd discussion-board-app
python3 -m venv virt
source virt/bin/activate (mac) or source virt/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Open in browser: http://127.0.0.1:8000/

## Features (Planned)
- User authentication
- Create, read, update, delete (CRUD) posts
- Comments and replies
- Admin moderation
- Style the frontend with Bootstrap
- Notifications or reminders for upcoming events
- Event Calendar
- Emergency Contacts & Quick Access
- Subscribe to groups (academic, sports, civil, clubs)

## Target Users
- Students (primary users)
- Campus administrators
- Event organizers
- Faculty and staff