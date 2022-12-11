# bioimage_analysis_framework_demo
Demo application for the position Python programmer at Danish BioImaging Infrastructure Image Analysis Core Facility (DBI-INFRA IACF)


# Prerequisites

The code in this repository is only known to run on Linux but Windows and Mac should in principle work as well if below requistes are installed.

Feel free to submit an issue or drop me an email if you have problems setting things up .

1. [Python 3.10+](https://www.python.org/)
2. [poetry version 1.2.2+](https://python-poetry.org/docs/#installing-with-the-official-installer)
3. [Node 18.12.1 LTS](https://nodejs.org/en/)
4. [Docker 20.10.21+](https://docs.docker.com/get-docker/)
5. [VSCode](https://code.visualstudio.com/)


# Installation / Library download
The framework is not really installed but rather the required libraries are download using poetry and npm.
All commands have to be executed in the repository root.

Download python libraries for the virtual environment:

```
poetry install
```

Download node modules for web frontend development:

```
cd frontend
npm install
```

# Architecture
![](architecture.drawio.png)

# Development

Note: Below instructions are written for a machine running Linux and VSCode as IDE. 

Generally speaking, all orange components of above architecture have to be started successively:

1. The AMQP message broker that distributes tasks amongst workers
2. The redis results backend for sending task results back to the requester
3. The celery service that executes tasks
4. The web frontend (optional)

## 1. AMQP broker
Execute in a shell:

```bash
# remove potential "old" container
docker rm bioimage-db-infra-rabbit
# start RabbitMQ broker
docker run --hostname localhost --name bioimage-db-infra-rabbit -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=biodude -e RABBITMQ_DEFAULT_PASS=biodude rabbitmq:3-management
```

The management interface can be found at http://localhost:15672/ with the user/password biodude

## 2. redis results backend

Execute in a shell:

```
docker run --name bioimage-db-infra-redis redis
```

## 3. Image processing service

TBD

## 4. Web frontend
To start the Quasar development server:

1. Press **Ctrl+Shift+P**
2. Select **Run Task**
3. Select **quasar-dev**

Note: the quasar-dev task is defined in .vscode/tasks