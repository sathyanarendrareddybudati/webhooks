# webhooks
 - It is a email sender to user for signup

# Technologies Used
 - Django & Django-Restframework
 - Mysql
 - webhooks 

## Getting started
To get started with Logging, follow these steps:

- Clone the repository to your local machine
- Install the required packages listed in requirements.txt
- Set up your MYSQL database and create a table for storing logs
- Start the Djnago application using `make run` or  `python manage.py runserver`


## Note
- All requests must have Authorization token in headers
- To install all packages using `make install` or `pip install -r requirements.txt`
- Token must pass like in headers `Authorization : Token <Token value>`
- SET UP APP PASSWORD FOR GOGGLE   `https://support.google.com/accounts/answer/185833?hl=en`

## In body data for example
 - `data : {
    "event": "signup",
    "user": {
        "name": "<name>",
        "email": "<email>",
        "username": "<username>"
    }
}
`