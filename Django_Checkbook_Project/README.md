# Django Checkbook Project 💰

A simple banking web app built with Django to manage accounts and transactions.

##  Project Structure

- **Project Name:** BlueBirdBanking  
- **App Name:** Checkbook

##  Features

- Create and manage **bank accounts**
- Record **deposits and withdrawals**
- View a live **balance sheet** with running totals
- Select accounts from a dropdown menu on the homepage

##  Setup Overview

1. Created project in **PyCharm**
2. Set up a **virtual environment**
3. Created Django project: BlueBirdBanking
4. Added Checkbook app and linked it in settings.py
5. Added templates and static files
6. Configured URLs in both project and app
7. Built view functions to render supplied templates

##  Models

### Account
- first_name
- last_name
- initial_deposit

### Transaction
- date
- type (Deposit or Withdrawal)
- amount
- description
- account (ForeignKey to Account)

##  Forms

- Account creation form
- Transaction creation form

##  Functionality

- Home page displays account selection form
- Balance sheet shows all transactions and current balance for selected account
- New transactions update the database and redirect to the updated balance sheet

##  Migrations

Apply migrations with:

' bash
python manage.py makemigrations
python manage.py migrate
'

##  How to Run

1. **Navigate to the project directory:**

' bash
cd Django_Checkbook_Project
'

2. **Activate your virtual environment:**

- On Windows:

' bash
venv\Scripts\activate
'

- On macOS/Linux:

' bash
source venv/bin/activate
'

3. **Run the development server:**

' bash
python manage.py runserver
'

4. **Open your browser and visit:**
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin (User: user / Password: user)