FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD [ "python3", "-m" , "flask",  "--app", "main.py", "run", "--host=0.0.0.0"]
