# CloudProject: End-to-end chat containerized and deployed

- [CloudProject: End-to-end chat containerized and deployed](#cloudproject-end-to-end-chat-containerized-and-deployed)
  - [Integrantes](#integrantes)
  - [Diagrama general](#diagrama-general)
  - [Scripts](#scripts)
    - [Docker](#docker)

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