FROM python:3.10-alpine

ENV SECRET_KEY="django-insecure-*@h&ig2_tf8d-2))2p2j(&if*^+t_qd8z-4wtbi*a6u+vpd&zw"

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]