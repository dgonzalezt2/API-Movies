# API-Movies

## Docker 

Crear imagen de docker

```bash
docker login
```
```bash
docker build -t api-movies:1.1.0 .
```
```bash
docker tag api-movies:1.1.0 dgonzalez2/api-movies:1.1.0
```
```bash
docker push dgonzalez2/api-movies:1.1.0
```
![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/c5bf9805-0467-40b7-8a0d-ace958736fc8)

## Kubernetes

### API

Se requiere agregar las siguientes variables de entorno:
```yaml
 env:
          - name: SQLALCHEMY_DATABASE_URI
            value: postgresql://dgonzalez2:12345@postgres:5432/api-movies
          - name: SQLALCHEMY_TRACK_MODIFICATIONS
            value: "false"
          - name: SHOW_SQLALCHEMY_LOG_MESSAGES
            value: "false"
          - name: ERROR_404_HELP
            value: "false"
```
Para leer las variables de entorno se requiere instalar la siguiente dependencia: `python-decouple`
Fijarse bien si esta incluido en el archivo: `requirements.txt`

### Base de datos

### Despliegue

Una vez creado el archivo `project.yaml` se debe ejecutar el siguiente comando para aplicar los cambios

```bash
kubectl apply -f project.yaml
```

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/b2ba7021-6d94-4995-b7fa-62fcd3dac997)

#### Exponer puerto

Para poder acceder a la API desde un servicio externo se ejecuta el siguiente comando

```bash
gcloud compute firewall-rules create api-movies --allow tcp:5000
```

#### Conexion BD

Para verificar si los datos si se guardaron correctamente se hace un port forward debido a que la BD no esta expuesta publicamente

```bash
kubectl get pods
```
```bash
kubectl port-forward -n default postgres-65bcfb64b7-kqdhn 5432:5432
```

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/c105ae1a-7948-4aae-a9d5-51a19af1e12d)

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/b058aa98-8ff6-4850-be55-330defb05d30)

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/b14b458c-a0e6-43e1-a555-0837e6b380bf)


### Visor de kubernetes 

Se instala la herramienta OpenLens para visualizar el cluster

Para lograrlo se realizo el siguiente [TUTORIAL](https://krisadas.medium.com/k8s-lens-with-google-cloud-255ccff5692) 

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/c2249d0b-69f1-4426-a6e4-547d85aa3ff8)


### DEMO

Haciendo un POST con el siguiente http:

```bash
http://34.122.77.128:5000/api/v1.0/films/
```

Con el siguiente Json:

```bash
{
    "title": "Pulp Fiction",
    "length": 9180,
    "year": 1994,
    "director": "Quentin Tarantino",
    "actors": [
        { "name": "John Travolta" },
        { "name": "Samuel L. Jackson" },
        { "name": "Uma Thurman" }
    ]
}
```

En Insomnia se veria asi el POST:

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/e359919e-21dc-49c5-bff7-24a42cd06e60)

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/579c436c-822b-4fca-8b1b-5d53834a1b3f)

![image](https://github.com/dgonzalezt2/API-Movies/assets/81880494/2d1d7956-e5bf-4ee7-a286-c03771defb00)

