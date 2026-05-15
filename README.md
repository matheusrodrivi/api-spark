# API Spark

Projeto desenvolvido para a disciplina de **Big Data** da pós-graduação em Engenharia de Software da UFRJ.

O objetivo do trabalho é realizar o tratamento e processamento de dados utilizando Apache Spark, disponibilizando posteriormente os dados tratados através de uma API para consumo no front-end..

---

## Tecnologias utilizadas

- Python
- FastAPI
- Apache Spark
- Docker
- Docker Compose

---

## Como executar o projeto

### Subindo os containers

### Com docker

```
docker compose up --build
```

### Com sudo docker (caso não tenha permissão)

```
sudo docker compose up --build
```

### Para rodar o container em background

```
sudo docker compose up -d --build
```

## Para acessar a API / docmentação swagger

```
http://localhost:8001
```

```
http://localhosfit:8001/docs
```

