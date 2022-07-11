# CloudProject: End-to-end chat containerized and deployed

- [CloudProject: End-to-end chat containerized and deployed](#cloudproject-end-to-end-chat-containerized-and-deployed)
  - [Integrantes](#integrantes)
  - [Diagrama general](#diagrama-general)
  - [Scripts](#scripts)
    - [Docker](#docker)
    - [Multicontainer (Docker-compose)](#Multicontainer (Docker-compose))
    - [Multicontainer (Docker-compose)](#Multicontainer (Docker-compose))
    - [Docker-compose to Minikube](#Docker-compose to Minikube)
    - [OpenFaaS](#openfaas)
    - [Prometheus](#prometheus)
    - [Grafana](#grafana)

## Integrantes
- Raúl Vides Mosquera Pumaricra
- Osman Rafael Vilchez Aguirre

## Diagrama general
En el presente diagrama se muestra como la aplicación fue deployada en minikube, así como su interacción con diversas apliaciones como por ejemplo openFaaS.

![Diagrama con containers](/imgs/CloudProject.jpg)


## Scripts
### Docker
```console
docker build -t rvmosquera/cloud-web-app:testing .

docker run -p 8080:8080 rvmosquera/cloud-web-app:testing

```
### Minikube
```console
kubectl create deployment flask-node --image=rvmosquera/cloud-web-app:testing

kubectl expose deployment flask-node --type=NodePort --port=8080

kubectl port-forward service/flask-node 7070:8080
```
### Multicontainer (Docker-compose)
```console
#Creating docker-compose.yml
doker up -
```
### Docker-compose to Minikube 
```console
minikube 
```
### OpenFaaS
```console
faas-cli new --lang python3 generate-pinv2

faas-cli build -f ./generate-pinv2.yml

faas-cli push -f ./generate-pinv2.yml

faas-cli deploy -f ./generate-pinv2.yml

faas-cli list --gateway http://127.0.0.1:8010
```

### Prometheus
```console
//openFaaS prometheus 
kubectl port-forward svc/prometheus 9090 -nopenfaas

kubectl run grafana -n openfaas --image=stefanprodan/faas-grafana:4.6.3 --port=3000


//mikube prometheus 
kubectl --namespace default port-forward prometheus-server-6bd8b49ff8-7jnxn 9090
```

### Grafana
```console
kubectl run --generator=run-pod/v1

kubectl -n openfaas run --image=stefanprodan/faas-grafana:4.6.3 --port=3000 grafana

kubectl -n openfaas expose pod grafana --type=NodePort --name=grafana

kubectl port-forward pod/grafana 3000:3000 -n openfaas
```
