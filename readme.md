To run using CLI:
    $ pip install -r requirements.txt
    $ py manage.py runserver 0.0.0.0:8000

To run using Docker
    $ docker build -t todo .
    $ docker run -p 8000:8000 todo

HomePage at "localhost:8000/todo/login"