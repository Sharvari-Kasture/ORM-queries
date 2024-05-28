Book Store

Welcome to the Book Store project! This is a Django-based web application for managing books.

Features

Add New Book: Easily add new books to the store.
Edit Existing Books: Update the details of books already in the store.
List Books: View a list of all books in the store.
Bootstrap Integration: Stylish user interface using Bootstrap.
Installation
Prerequisites
Before you begin, ensure you have the following installed on your system:

Python

pip (Python package installer, usually installed with Python)
Installing
Clone the repository:

bash

Copy code
git clone https://github.com/your_username/bookstore.git
Navigate to the project directory:

bash

Copy code
cd bookstore
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the project dependencies:

bash
Copy code
pip install -r requirements.txt
Starting the Django Project
To start the Django project named "Queries", run the following command:

bash
Copy code
django-admin startproject Queries .
This command creates a new Django project in the current directory (denoted by the dot .).

Creating a Django App
To create a new Django app named "QueriesApp", run the following command:

bash
Copy code
django-admin startapp QueriesApp
This command creates a new Django app within your project.

Running the Development Server
To run the Django development server, execute the following command:

bash
Copy code
python manage.py runserver
You should see output indicating that the development server is running. Visit http://localhost:8000 in your web browser to access the application.

Usage
To add a new book, navigate to the "Add New Book" page from the navigation bar and fill out the form.
To edit an existing book, click on the book in the book list and then click on the "Edit" button.
To view the list of books, click on the "Home" link in the navigation bar.
Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

