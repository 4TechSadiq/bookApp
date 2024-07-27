# BookApp

This is a basic Django application for managing a collection of books. The application uses SQLite as the database and includes routes for performing various CRUD (Create, Read, Update, Delete) operations on books.

## Features

- View details of individual books
- Add new books
- Update existing books
- Delete books

## Requirements

- Python 3.x
- Django 3.x or later
- SQLite (default with Django)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-app.git
   cd book-app
2. Create Virtual environment and Activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
4. Apply migrations:
   ```bash
   python manage.py migrate
5. Create a superuser to access the Django admin:
   ```bash
   python manage.py createsuperuser
6. Run the development server:
   ```bash
   python manage.py runserver
7. Open your web browser and go to http://127.0.0.1:8000 to see the app.

## Usage

### Viewing Books

Go to the homepage to see a list of all books. Click on a details to view its details.

### Adding a New Book

Fill the form to add new record.

### Updating a Book

From the Record Table choose Update to update the record.

### Deleting a Book

From the book detail view, click the "Delete" button to remove the book from the collection.

## Project Structure

- `bookapp/`: Contains the main Django project settings and URLs.
- `books/`: Contains the book application with models, views, templates, and forms.
- `templates/`: Contains HTML templates for the application.
- `db.sqlite3`: The SQLite database file.
- `manage.py`: The command-line utility for administrative tasks.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the `LICENSE` file for more information.







