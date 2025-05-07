# Blog Api
A simple and secure RESTful API for managing blog posts, built with Django. This API allows users to create posts and authenticated users to add comments. It also supports filtering of posts based on `title`, `author`, or `category`.

## Features

- JWT-based authentication
- User registration with Django's default user model
  - User Name
  - Email 
  - Password 
- Create and manage blog posts with:
  - Author
  - Title
  - Status
  - Category
  - Description
- Authenticated User allow to do comment on blog post
- Filter posts by title, author, or category
- Pagination support for listing posts
- API rate limiting with Throttling

## Technologies Used

- Python 
- Django
- Django REST Framework
- SQLite 

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Blog_Api.git
cd Recipe-App-Api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

- API documentation is available via Swagger UI at `http://127.0.0.1:8000/api/docs/`

## License

This project is licensed under the MIT License.

## Author

- Your Name - Nikunj Kakadiya
