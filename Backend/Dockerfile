FROM python:3

WORKDIR /usr/src/backend

RUN pip install flask

ENV FLASK_APP=app.py

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]