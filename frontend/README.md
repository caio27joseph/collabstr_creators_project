# Collabstr Full-Stack Developer Project

## Introduction

This Django-based web application showcases content from various creators, combining RESTful backend services (Django REST framework) with traditional Django views and templates, enhanced with jQuery for dynamic content updates.

## Project Scope

### A. Back-End Development
1. Models for data from a JSON file (`Creator` and `Content`).
2. Script for populating a SQLite database.
3. Django REST framework for RESTful services.
4. Django views for querying `Content` and `Creator` models.

### B. Front-End Development
1. Display content with creator details.
2. Tabs for filtering creators by platform (Instagram, TikTok, UGC) using AJAX and jQuery.
3. Responsive design with modern CSS.

### C. Deployment
1. Hosted on a publicly accessible webpage.
2. Code on GitHub.

## Prerequisites
- Python 3.x
- Django 3.x or 5.x
- Django REST Framework
- Dependencies in `requirements.txt`

## Installation and Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Populate the database: `python seed.py`

## Running the Application
1. Start the server: `python manage.py runserver`
2. Access at `http://localhost:8000`.

## Running Tests
- Use `pytest` or `python manage.py test`

## Architecture and Design Decisions

### Backend
- Django REST Framework for Web APIs.
- Data models for creators and content.
- Database migrations for schema evolution.

### Frontend
- Django views and templates for initial rendering.
- jQuery and AJAX for dynamic content.
- Responsive design for various devices.

### Deployment
- Django's server for development.
- Production deployment includes static file management, database configuration, and security settings.

## Accessing the Live Application
The live application is hosted at [caiojoseph.com/creators](http://caiojoseph.com/creators).

### Note: Frontend Directory
The frontend directory contains the initial version without Django templates.

## Contact and Support
For queries or support, contact caio27joseph@gmail.com
