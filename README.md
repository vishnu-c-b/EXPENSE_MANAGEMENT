# Daily Expenses Sharing Application

This application allows users to add expenses and split them using three different methods: exact amounts, percentages, and equal splits. It also manages user details, validates inputs, and generates downloadable balance sheets.

## Features

- User Management
  - Create and manage user details (email, name, mobile number).
- Expense Management
  - Add expenses with different split methods:
    - Equal: Split equally among all participants.
    - Exact: Specify the exact amount each participant owes.
    - Percentage: Specify the percentage each participant owes (ensure percentages add up to 100%).
  - Retrieve individual user expenses.
  - Retrieve overall expenses for all users.
  - Download the balance sheet in CSV format.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST framework
- MySQL or SQLite

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vishnu-c-b/SIMPLE-BLOG

   ```

2. **Navigate to the project directory:**

   ```bash
   cd expense_manage
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Create user:** `POST /users/create/`

- **Retrieve user details:** `GET /users/<id>`

- **Add expense(EQUAL,EXACT,PERCENTAGE):** `POST /expenses/create/`

- **Retrieve individual user expenses:** `GET /expenses/user/<id>/`

- **Retrieve overall expenses:** `GET /expenses/overall/`

- **Download balance sheet:** `GET /expenses/download-balance-sheet/`

## Access the API Endpoints in Postman:

Follow these steps to interact with the API using Postman:

1. **Import the provided Postman collection:**

   - Click on the following button to view the Postman documentation:

     [![Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/33931821/2sA3kaDKpu)

2. **Set up the environment in Postman:**

   - After importing the collection, set up your environment variables, such as the base URL (`http://127.0.0.1:8000`).

3. **Send requests using example data:**
   - Explore the endpoints documented in the collection and use the example data provided in the documentation as test inputs.
