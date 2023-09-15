# Person API

A simple Django REST API for managing person records.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Development Server](#running-the-development-server)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [Postman](#postman)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) installed (>=3.6)
- [Django](https://www.djangoproject.com/download/) installed
- [Django REST Framework](https://www.django-rest-framework.org/#installation) installed
- Git for version control (optional)

## Installation

1. Clone the repository (if you haven't already):

   bash
   git clone https://github.com/yourusername/your-repo.git

2. Navigate to the project directory: cd repo-name

3. Create a virtual environment (optional but recommended): python -m venv venv

4. Activate the virtual environment (Windows): venv\Scripts\activate
(macOS/Linux): source venv/bin/activate

5. Install project dependencies: pip install djangorestapiframework

6. Apply database migrations: python manage.py migrate

### Usage

## Running the Development Server
To run the development server: python manage.py runserver

The API will be accessible at http://127.0.0.1:8000/.

API Endpoints
List/Create Persons:
Endpoint: /api/
Method: GET (list) / POST (create)
Request (POST):
{
  "name": "John Doe",
  "age": 30
}
Response (GET):
[[
  {
    "id": 1,
    "name": "John Doe",
    "age": 30
  }
]]
Retrieve/Update/Delete Person by ID:
Endpoint: /api/{id}/
Methods: GET (retrieve) / PUT (update) / DELETE (delete)
Retrieve/Update/Delete Person by Name:
Endpoint: /api/name/{name}/
Methods: GET (retrieve) / PUT (update) / DELETE (delete)

### Testing

To run unit tests: python manage.py test

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and submit a pull request.

### Using Postman

Postman is a useful tool for testing APIs. Here's how you can use Postman with the Person API:

Open Postman.
Create a new request.
Choose the HTTP method (GET, POST, PUT, DELETE) for the desired operation.
Enter the API endpoint URL (http://josh565.pythonanywhere.com/api/) for the request.
Add any required headers (e.g., Content-Type: application/json, Authorization).
In the request body (if needed), provide the data in JSON format.
Click the "Send" button to make the request.
View the API's response in Postman.
