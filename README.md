## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.


To run tests :

```sh
$ python manage.py test
```


Then the endpoint:

    GET http://localhost:8080/api/external-books?name=:nameOfABook

is requested, your application should query the Ice And Fire API and use the data received to respond with precisely the following JSON if there are results:
    

    [
        "status_code": 200,
        "status": "success",
        "data": [
            {
                "name": "A Game of Thrones",
                "isbn": "978-0553103540",
                "authors": [
                    "George R. R. Martin"
                ],
                "number_of_pages": 694,
                "publisher": "Bantam Books",
                "country": "United States",
                "release_date": "1996-08-01",
            },
            {
                "name": "A Clash of Kings",
                "isbn": "978-0553108033",
                "authors": [
                    "George R. R. Martin"
                ],
                "number_of_pages": 768,
                "publisher": "Bantam Books",
                "country": "United States",
                "release_date": "1999-02-02",
            }
        ]
    ]
or precisely this JSON if the Ice and Fire API returns no results:
```
{
    "status_code": 200,
    "status": "success",
    "data": []
}
```

where `:nameOfABook` is a variable. Example value for `:nameOfABook` can be A Game Of Thrones.
Note that the JSON property names that Ice And Fire uses don't quite match the ones in the required output that your application needs to deliver, so pay attention to this. Also, not all of the output from Ice And Fire is required in your application's output - you may need to suppress some field(s).


**Create**

When the endpoint:

    POST http://localhost:8080/api/v1/books
is requested with the following data:

```
name
isbn
authors
country
number_of_pages
publisher
release_date
```
a book should be created in the local database and the following response should be returned:
```
[
    "status_code": 201,
    "status": "success",
    "data": [
        "book": {
            "name": "My First Book",
            "isbn": "123-3213243567",
            "authors": [
                "John Doe"
            ],
            "number_of_pages": 350,
            "publisher": "Acme Books",
            "country": "United States",
            "release_date": "2019-08-01",
        },
    ]
]
```
**Read**

When the endpoint:

    GET http://localhost:8080/api/v1/books
is requested, your solution will return a list of books from the local database using the following response:
```
[
    "status_code": 200,
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "number_of_pages": 694,
            "publisher": "Bantam Books",
            "country": "United States",
            "release_date": "1996-08-01",
        },
        {
            "id": 2,
            "name": "A Clash of Kings",
            "isbn": "978-0553108033",
            "author": [
                "George R. R. Martin"
            ],
            "number_of_pages": 768,
            "publisher": "Bantam Books",
            "country": "United States",
            "release_date": "1999-02-02",
        }
    ]
]

```

or precisely this JSON if the Books API returns no results:
```
{
    "status_code": 200,
    "status": "success",
    "data": []
}
```

The Books API should be searchable by name (string), country (string), publisher (string) and release date (year, integer).

**Update**
When the endpoint:

    PATCH http://localhost:8080/api/v1/books/:id
is requested with any of the following form data:
```
name
isbn
authors
country
number_of_pages
publisher
release_date
```

and a specific `:id ` in the URL, where `:id ` is a place holder variable for an integer (for example 1), the specific book should be updated in the database and the following response should be returned:

```
[
    "status_code": 200,
    "status": "success",
    "message": "The book My First Book was updated successfully",
    "data": {
        "id": 1,
        "name": "My First Updated Book",
        "isbn": "123-3213243567",
        "authors": [
            "John Doe"
        ],
        "number_of_pages": 350,
        "publisher": "Acme Books Publishing",
        "country": "United States",
        "release_date": "2019-01-01",
    }
]
```

**Delete**

When the endpoint:

    DELETE http://localhost:8080/api/v1/books/:id
is requested with a specific :id in the URL, where :id is a placeholder variable for an integer (for example 1), the specific book should be deleted from the database and the following response will be returned:
```
[
    "status_code": 204,
    "status": "success",
    "message": "The book My First Book was deleted successfully",
    "data": []
]
```

**Show**

When the endpoint:

    GET http://localhost:8080/api/v1/books/:id
is requested with a specific `:id` in the URL, where `:id` is a placeholder variable for an integer (for example 1), it should show the specific book and the following response will be returned:

```
[
    "status_code": 200,
    "status": "success",
    "data": {
        "id": 1,
        "name": "My First Book",
        "isbn": "123-3213243567",
        "authors": [
            "John Doe"
        ],
        "number_of_pages": 350,
        "publisher": "Acme Books Publishing",
        "country": "United States",
        "release_date": "2019-01-01",
    }
]
```