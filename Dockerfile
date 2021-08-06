FROM python:3.8-slim

WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8181

CMD [ "python", "src/app.py" ]