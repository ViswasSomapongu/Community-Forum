# Community Forum

Welcome to the Community Forum, a simple Django web app where users can connect, share experiences, and engage in discussions on various topics.

## Features

- **User Authentication:** Users can register, login, and logout securely to access the forum features.
- **Thread Posting:** Users can create new discussion threads to share their experiences or initiate discussions on topics of interest.
- **Replying to Threads:** Users can reply to existing threads to contribute to the discussion or provide insights.
- **Reply Deletion:** Users can delete their own replies if they wish to remove their contributions.
- **User Profiles:** Users have personalized profiles where they can view their own details.
- **Authentication Redirect:** If a user tries to comment or reply to a thread without authentication, they will be redirected to the login page.
- **Public Access:** Visitors can view a list of all threads, even without logging in.
- **Thread Viewing:** Users can view all replies to a particular thread when logged in.

## Setup Instructions

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ViswasSomapongu/Community-Forum.gi
Navigate to the project directory:
cd community-forum

Install the required dependencies:
pip install -r requirements.txt

Apply migrations to set up the database:
python manage.py migrate

Create a superuser account to access the admin panel (optional):
python manage.py createsuperuser

Run the development server:
python manage.py runserver
