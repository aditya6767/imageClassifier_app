FROM python:3.8-slim

WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8181

# CMD [ "python", "src/app.py" ]

CMD ["gunicorn","-w", "2","-t", "600",  "-b", "0.0.0.0:8181","--reload","src.wsgi:app"]