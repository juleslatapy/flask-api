FROM python:3.7.3-alpine3.9 as base

RUN pip install Flask==2.0.3

WORKDIR /app
COPY src/app.py /app/
ENV FLASK_APP=app.py
CMD flask run -h 0.0.0 -p 5000