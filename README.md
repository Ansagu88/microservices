# Microservices Project
This project consists of several microservices, each with its own directory and specific functionality. The microservices are auth, cart and wishlist.

## Auth
The auth microservice is located in the auth/ directory. This service is responsible for authentication and user management. Uses Django and Django Rest Framework to expose user management and authentication endpoints.

### Principal functions
User authentication through JWT (JSON Web Tokens).
User management, including creating, updating and deleting user accounts. These functions can be found in UserAccountTests.
How to run
To run this service, use the docker-compose up command in the auth/ directory.

## Cart
The cart microservice is located in the cart/ directory. This service is responsible for managing the users' shopping cart.

### Principal functions
Shopping cart management, including adding and deleting products.
How to run
To run this service, use the docker-compose up command in the cart/ directory.

## Wishlist
The wishlist microservice is located in the wishlist/ directory. This service is responsible for managing the users' wish list.

### Principal functions
Wish list management, including adding and removing products.
How to run
To run this service, use the docker-compose up command in the wishlist/ directory.

## Requirements
Docker and Docker Compose
Python 3.8 or higher
Django 4.2.3 or higher
How to run the tests
To run the tests, navigate to the directory of the service you want to test and run the python manage.py test command.

## Contribute
To contribute to this project, please fork the repository, make your changes, and then submit a pull request.
