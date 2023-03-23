FROM python:3

WORKDIR /usr/src/backend

RUN pip install flask
RUN pip install Flask-JSON

ENV FLASK_APP=app.py

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]