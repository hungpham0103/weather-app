# Weatherapp

## Installation

Tải [Docker](https://www.docker.com/get-started/) về máy

## Usage

Build Docker image:

```shell
docker build -t weatherapp .
```

Run application trong Docker container:

```shell
docker run -p 8000:8000 weatherapp
```

Access API Documentation:

Để access API Documentation (Swagger UI), truy cập: http:0.0.0.0:8000/docs