# REST server using imaginAIry

## Overview
Python swagger-enabled Flask REST server to generate images with [imaginAIry](https://github.com/brycedrennan/imaginAIry). This server was generated from [here](https://app.swaggerhub.com/apis/HANNESSOFTWARE/imaginAIry/1.0.0#/Environment/generateImage).
This server uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/HANNESSOFTWARE/imaginAIry/1.0.0/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/HANNESSOFTWARE/imaginAIry/1.0.0/swagger.json
```

To launch the integration tests, use tox:
```
pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```

## Apple M1 usage

It needs this https://stackoverflow.com/a/68137855/1079990 and install each separate instead of requirements.txt