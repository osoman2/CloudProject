FROM python:3.10
LABEL Maintainer="Cloud@team"

WORKDIR /cloud-app

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY ./web ./web

CMD ["python", "./web/server.py"]