# CloudProject: End-to-end chat containerized and deployed


## Diseño 
### Arquitectura
![Arquitectura PreCloudCourse](https://github.com/osoman2/CloudProject/blob/main/imgs/arquitecturaPreCloud.PNG)

### Funcionalidad
La aplicación es un chat 1 a 1 con encriptación asimétrica. Usa una base de datos para almacenar la contraseña hasheada de los usuarios, los mensajes encriptados y los códigos de verificación del 2-step autentificator. 
- Cada usuario puede crearse una cuenta, loguearse y chatear con todas las personas disponibles en la base de datos pero para ello deberá subir una llave que está guardada en el local storage.
- Al iniciar el chat con cada una de las personas, se creará una llave privada para ambos usuarios mediante criptografía asimétrica que deberá ser descargada por ambos para que se pueda reutilizar para encriptar y desencriptar los mensajes posteriores. Conservar la llave en local storage fue el resultado parcial de un modelamiento de amenazas por lo que conservar esta idea de la creación del secreto compartido debe de tener soluciones que mantengan esta naturaleza.

### Referencias
- T. Bose, “Implementing end to end encryption in your cross platform app,” DEV Community, 10-Mar-2021. [Online]. Available: https://dev.to/ruppysuppy/implementing-end-to-end-encryption-in-your-cross-platform-app-3a2k. 
- “Hashlib - Secure hashes and message digests,” hashlib - Secure hashes and message digests - Python 3.10.1 documentation. [Online]. Available: https://docs.python.org/3/library/hashlib.html

## ¿Porque escogió esa aplicación? ¿Qué características de la computación en nube pueden ser integradas en la aplicación?
- Escoger esta app tiene la ventaja de ser fácilmente desacoplable, tiene detalles de implementación requerido en otros cursos como proyecto parcial y/o final (e.g Seguridad en Computación) y tenemos conocimiento profundo de ella. Pues ha sido un proyecto que nos ha permitido comprender de forma efectiva los conceptos de otros cursos a lo largo de la carrera. Asímismo, las dependencias son pocas, no cuenta con un package manager (e.g npm) que complique la containerización. 
- Al ser sencilla y dado el requerimiento de esta end-to-end chat. Usar una nube pública (AWS) con docker y K8s serían un ejercicio que sintetizaría los conceptos aprendidos.
- Como requerimiento adicional, la app crea llaves privadas y las guarda en "local storage" por lo cuál es probable que se usen algunos *storages persistentes* vistos en clase. Así como este problema puede dar la apertura para sacar la otra base de datos solo de los mensajes y contaneirizarlo; entre otras variantes.

## Pasos de ejecución
Recomendación: Correr en un venv.
1. pip install flask
2. pip install sqlalchemy
3. pip install sqllite
4. pip install hashlib
//En la carpeta del backend ejecutar
5. python3 main.py
