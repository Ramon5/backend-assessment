## REQUISITOS

docker: https://www.docker.com/get-started \
docker-compose: https://docs.docker.com/compose/install/

## Instalando as dependências

$ pipenv install --three

# Ativando o ambiente virtual

$ pipenv shell

## Criação das imagens docker

Rode o comando abaixo, para executar o build das imagens do docker.

$ make dev_setup

## Executar testes

$ make test

## RUN

para subir os containers e executar a aplicação, rode o comando abaixo:

$ make run

## Rotas

No navegador, acesse o endereço: http://0.0.0.0:8000/swagger

**Utilitários:** \

Postman
Insomnia
httpie


## Monitor de requisições (Flower)

Monitora os workers e lista o estado da tarefa

http://0.0.0.0:5555

## Email Server (MailHog)

Caixa de entrada para verificação dos emails de aprovação ou rejeição de requisições

http://0.0.0.0:8025

