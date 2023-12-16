# Collabstr Full-Stack Developer Project

## Introduction

This project is a Django-based web application designed to showcase content from various creators. It combines RESTful backend services using Django REST framework with traditional Django views and templates, enhanced with jQuery for dynamic content updates.

## Project Scope

### A. Back-End Development
1. Models for storing data from a JSON file (`Creator` and `Content`).
2. Script for populating SQLite database with creators and their content.
3. Django REST framework to create RESTful services.
4. Django view for querying the `Content` model and its related `Creator` object, with a limit of 30 objects returned.

### B. Front-End Development
1. Display content with details of its creator.
2. Implementation of tabs to filter creators by platform (Instagram, TikTok, User Generated Content) using AJAX and jQuery.
3. Responsive design using modern CSS techniques.

### C. Deployment
1. Hosting the implementation on a publicly accessible webpage.
2. Code hosted on a GitHub repository.

## Prerequisites
- Python 3.x
- Django 3.x or 5.x
- Django REST Framework
- Other Python libraries as required (listed in `requirements.txt`)

## Installation and Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Populate the database: `python seed.py`

## Running the Application
1. Start the server: `python manage.py runserver`
2. Access the application at `http://localhost:8000`.

## Running Tests
- Run tests using: `pytest` or `python manage.py test`

## Architecture and Design Decisions

### Backend
- **Django REST Framework**: Used for creating RESTful services. It provides a powerful and flexible toolkit for building Web APIs.
- **Data Models**: Models are defined to represent the data structure required for creators and their content.
- **Database Migrations**: Django's migration system is used for evolving the database schema over time in a consistent and database-agnostic way.

### Frontend
- **Django Views and Templates**: Leveraged for rendering the initial HTML content.
- **jQuery and AJAX**: Used for dynamic content loading without the need to reload or navigate away from the current page. This enhances user experience by providing a smooth and interactive interface.
- **Responsive Design**: Implemented using CSS, ensuring the application is accessible and usable across various devices and screen sizes.

### Deployment
- **Development Server**: Django's built-in server is used for development and testing.
- **Production Deployment**: Instructions for deploying to a production environment can be added as needed, including settings for static file management, database configuration, and security settings.

## Contact and Support
For any queries or support during the project, please contact caio27joseph@gmail.com

### OBS: Frontend Directory
This directory is the first version of the front end without using the django templates.