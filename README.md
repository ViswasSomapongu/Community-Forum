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
## Screenshots
![image](https://github.com/ViswasSomapongu/Community-Forum/assets/145599843/a781ee16-57fb-4e6a-a539-55332ff66baa)

![image](https://github.com/ViswasSomapongu/Community-Forum/assets/145599843/e48ab0de-76d2-4755-bede-f008923d6194)

![image](https://github.com/ViswasSomapongu/Community-Forum/assets/145599843/10b9012b-b0d9-4dad-81ef-c5adf3f2118c)

![image](https://github.com/ViswasSomapongu/Community-Forum/assets/145599843/d1ce1a2b-fa84-4694-81e9-7422e7d82dd7)

![image](https://github.com/ViswasSomapongu/Community-Forum/assets/145599843/70bf4a83-b72c-4db9-a1cc-d1f6c292421a)

![image](https://github.com/ViswasSomapongu/Community-Forum/assets/145599843/a9d865b2-63ef-4602-b48b-3e8fc1f4bbe9)

![image](https://github.com/ViswasSomapongu/Community-Forum/assets/145599843/9273d442-867c-4ef9-8e40-b097bf11e89b)


## Setup Instructions

### Clone the repository to your local machine:
git clone https://github.com/ViswasSomapongu/Community-Forum.git

### Navigate to the project directory:
cd communityproject

### Install the required dependencies:
pip install -r requirements.txt

### Apply migrations to set up the database:
python manage.py migrate

### Create a superuser account to access the admin panel (optional):
python manage.py createsuperuser

### Run the development server:
python manage.py runserver

