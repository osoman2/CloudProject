FROM python:3.10
LABEL Maintainer="Cloud@team"

#host for calling functions inside minikube
ENV OPENFAAS_HOST=http://10.105.163.115:8080

WORKDIR /cloud-app

COPY requeriments.txt .

RUN pip install --no-cache-dir -r requeriments.txt

COPY ./web ./web

CMD ["python", "./web/server.py"]