# Desafio Wattio

Implementação da atividade sugerida para a vaga de estágio back-end n Wattio.

## Pré-requisitos

O daemon do Docker precisa estar executando em segundo plano.

## Como executar essa aplicação

1. Clone o repositório e acesse a pasta da aplicação

```
git clone --branch feature/andrew git@github.com:andrewunifei/backend.git
cd backend
```

2. Execute o arquivo do docker compose

```
docker compose up --build
```

## Utilizando a aplicação

O docker compose irá iniciar o contâiner com o sqlite e criará um banco de dados e uma tabela de filmes caso ela não exista. O docker compose também irá iniciar um segundo contâiner com o server rodando ouvindo as requisições. 

O banco de dados vem apenas com a tabela filmes e ela está vazia. É necessário adicionar filmes.

### Endpoints da API

Exemplos:

- ```GET /filmes```

Corpo da resposta:

```JSON
[
    {
        "id": 1,
        "nome": "Pulp Fiction",
        "ano": 1995,
        "diretor": "Quentin Tarantino"
    }
]
```

- ```GET /filmes/{id}```

Corpo da resposta:

```JSON
{
    "id": 1,
    "nome": "Pulp Fiction",
    "ano": 1995,
    "diretor": "Quentin Tarantino"
}
```

- ```POST /filmes```

Corpo da requisição:

```JSON
{
    "nome": "Pulp Fiction",
    "ano": 1995,
    "diretor": "Quentin Tarantino"
}
```

Corpo da resposta:

```JSON
{
    "id": 1,
    "nome": "Pulp Fiction",
    "ano": 1995,
    "diretor": "Quentin Tarantino"
}
```
