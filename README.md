# Microservices Project

This project consists of several microservices, each with its own directory and specific functionality. The microservices are Auth, Cart and Wishlist.
When a user is created in the Auth application, it sends a message through Apache Kafka to the Cart and Wishlist application, so that the user's respective services are created, such as the shopping cart and the wish list.

## Facility

To install and run this project, you will need to follow these steps:

    1.Clone the repository
    2.For each application you must navigate to its own directory
    3.Create a virtual environment for each application, in total you must create three virtual environments
    4.Install the dependencies: pip install -r requirements.txt
    3.Run the project: docker compose up  

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

## Principal Requirements
Docker and Docker Compose
Python 3.8 or higher
Django 4.2.3 or higher
How to run the tests
To run the tests, navigate to the directory of the service you want to test and run the python manage.py test command.

## Contribute
To contribute to this project, please fork the repository, make your changes, and then submit a pull request.

## License
This project is licensed under the MIT license.

## Contact
If you have any questions or suggestions, please feel free to contact me at my email: ansagu88@gmail.com

## Thanks
I thank everyone who has contributed to this project and those who have used it and provided valuable feedback.
