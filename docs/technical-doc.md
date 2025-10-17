## Technical Documentation - Discussion Board App

**Project**: Discussion Board
**Team**: Alessandro Villegas, Andres Cantu
**Date**: October 2025

1. ## What is this App?
**A discussion board where users can:**

- Create topics to discuss
- Reply to topics
- Edit and delete their own posts
- Upvote/downvote posts
- Search for topics
- Subscribe to groups
- Access contacts
- Upcoming events calendar

2. ## Technology Used
**Backend**

- Python 3.10+
- Django 4.2 - Web framework
- PostgreSQL - Database (or SQLite for development)

**Frontend**

- Django Templates - HTML pages
- Bootstrap 5 - Styling and design
- CSS - Extra Styling if needed

**Tools**

- Git & GitHub - Version control
- VS Code - Code editor


3. ## How the App Works
**User Flow**

- User visits the site
- User registers/logs in
- User views list of topics
- User clicks on a topic to read
- User posts a reply
- User can edit/delete their own posts
- User can join groups (ex. clubs)


**App Structure**
User → Django Views → Database → Django Templates → User's Browser

4. ## Database Design
- Tables
**Users (Built-in Django)**

- user_id (primary key)
- username
- email
- password (encrypted)

**Topics**

- topic_id (primary key)
- author (who created it)
- title
- content
- created_at (date/time)
- view_count

**Posts**

- post_id (primary key)
- topic (which topic it belongs to)
- author (who wrote it)
- content
- nested replies
- upvotes
- created_at (date/time)

**Reactions**

- reaction_id (primary key)
- user (who reacted)
- post (which post)
- reaction_type (upvote/downvote)

**How They Connect**

- One User can create many Topics
- One Topic can have many Posts
- One Post can have many Reactions
- Posts can reply to other Posts (nested)


5. ## Main Features
**Authentication**
- What: User registration and login
- How: Django's built-in authentication system
- Files: users/views.py, users/templates/

**Topics (CRUD)**
- What: Create, Read, Update, Delete topics
- How: Django views and forms
- Files: forum/views.py, forum/models.py, forum/templates/

**Posts/Replies (CRUD)**
- What: Create, Read, Update, Delete replies
- How: Django views connected to Topic model
- Files: forum/views.py, forum/models.py

**Upvote/Downvote**
- What: Users can like/dislike posts
- How: Reaction model tracks votes
- Files: forum/models.py (Reaction model)

**Search**
- What: Find topics by keyword
- How: Django QuerySet filtering
- Files: forum/views.py (search view)

