# The Wave Social Media Application

# Table of Contents

1. Introduction
2. Features
3. Demo
4. Installation
5. Usage
6. Contributing
7. License
8. Contact


# Introduction

The Wave is a social media application built with Django, allowing users to create accounts, follow each other, create posts, and     interact through likes and comments. This project demonstrates a fully functional social media platform with a modern and responsive design.



# Features

  User authentication and authorization
  Profile creation and customization (including profile pictures and bios)
  Follow and unfollow users
  Create, edit, and delete posts
  Like and comment on posts
  View posts in a feed
  Search for users and posts
  Responsive design for mobile and desktop
  Demo

A live demo of the application can be found here.

# Installation

# Prerequisites
Python 3.x
Django 3.x
PostgreSQL
Heroku CLI

# Steps

1. Clone the repository:

2. git clone https://github.com/your-username/The-Wave-Social-Media-Application-.git
cd The-Wave-Social-Media-Application-
Create a virtual environment and activate it:

3. python -m venv venv
source venv/bin/activate  
# On Windows use `venv\Scripts\activate`
Install the dependencies:

4. pip install -r requirements.txt

5. Set up the database:

6. Configure your database settings in settings.py. Create and apply migrations:

7. python manage.py makemigrations
   python manage.py migrate
   Create a superuser:


8. python manage.py createsuperuser
   Run the development server:

9. python manage.py runserver
   Access the application:

10. Open your browser and go to http://127.0.0.1:8000/.

# Usage

Register an account or log in with an existing one.
Customize your profile by adding a profile picture and bio.
Start creating posts and follow other users.
Like and comment on posts to interact with others.
Contributing

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.




# Contact

# For any inquiries or issues, please contact:

    Name: Daniel Roth 
    Email: Danielcharlesroth@gmail.com
    GitHub: Dcroth99
