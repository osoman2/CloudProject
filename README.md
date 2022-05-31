# CloudProject: End-to-end chat containerized and deployed


## Diseño 
![Arquitectura PreCloudCourse](https://github.com/osoman2/CloudProject/blob/main/imgs/arquitecturaPreCloud.PNG)


## ¿Porque escogió esa aplicación? ¿Qué características de la computación en nube pueden ser integradas en la aplicación?
- Escoger esta app tiene la ventaja de ser fácilmente desacoplable, tiene detalles de implementación requerido en otros cursos como proyecto parcial y/o final (e.g Seguridad en Computación) y tenemos conocimiento profundo de ella. Pues ha sido un proyecto que nos ha permitido comprender de forma efectiva los conceptos de otros cursos a lo largo de la carrera. Asímismo, las dependencias son pocas, no cuenta con un package manager (e.g npm) que complique la containerización. 
- Al ser sencilla y dado el requerimiento de esta end-to-end chat. Usar una nube pública (AWS) con docker y K8s serían un ejercicio que sintetizaría los conceptos aprendidos.
- Como requerimiento adicional, la app crea llaves privadas y las guarda en "local storage" por lo cuál es probable que se usen algunos *storages persistentes* vistos en clase. 

## Pasos de ejecución
Recomendación: Correr en un venv.
1. pip install flask
2. pip install sqlalchemy
3. pip install sqllite
//En la carpeta del backend ejecutar
5. python3 main.py
