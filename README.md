# Person API Documentation

This is a simple Django REST API for managing person records.

## Table of Contents

- [Introduction](#introduction)
- [Accessing the API](#accessing-the-api)
- [Using the API](#using-the-api)
  - [GET Request (List Persons)](#get-request-list-persons)
  - [POST Request (Create Person)](#post-request-create-person)
  - [GET Request (Retrieve Person)](#get-request-retrieve-person)
  - [PUT Request (Update Person)](#put-request-update-person)
  - [DELETE Request (Delete Person)](#delete-request-delete-person)
- [Using Postman](#using-postman)
- [License](#license)

## Introduction

The Person API is a simple REST API that allows you to perform CRUD (Create, Read, Update, Delete) operations on person records. It is hosted at [http://your-api-url.com/api/](http://your-api-url.com/api/).

## Accessing the API

You can access the API using the following base URL: http://josh565.pythonanywhere.com/api/


## Using the API

### GET Request (List Persons)

To retrieve a list of all persons, make a GET request to the following endpoint: GET http://josh565.pythonanywhere.com/api/
## Using the API



### POST Request (Create Person)

To create a new person, make a POST request to the following endpoint: POST http://josh565.pythonanywhere.com/api/

In the request body, provide the person's details in JSON format. For example:

json
{
  "name": "Mark Essien",
  "age": 30
}

### GET Request (Retrieve Person)

To retrieve the details of a specific person by their ID, make a GET request to the following endpoint, replacing {id} with the person's ID:
GET http://josh565.pythonanywhere.com/api/{id}/

### PUT Request (Update Person)
To update the details of a specific person by their ID, make a PUT request to the following endpoint, replacing {id} with the person's ID:
PUT http://josh565.pythonanywhere.com/api/{id}/
In the request body, provide the updated person's details in JSON format.

DELETE Request (Delete Person)
To delete a specific person by their ID, make a DELETE request to the following endpoint, replacing {id} with the person's ID:
PUT http://josh565.pythonanywhere.com/api/{id}/


### Using Postman

Open Postman.
Create a new request.
Choose the HTTP method (GET, POST, PUT, DELETE) for the desired operation.
Enter the API endpoint URL (http://josh565.pythonanywhere.com/api/) for the request.
Add any required headers (e.g., Content-Type: application/json, Authorization).
In the request body (if I'm needed), provide the data in JSON format.
Click the "Send" button to make the request.
View the API's response in Postman.
