# Gerenciador de acervo de filmes / Movie Collection Manager🎬

Este projeto consiste em um programa que permite armazenar, consultar, deletar e alterar filmes de uma base de dados.

This project is a program that allows storing, searching, deleting and updating movies from a database.

<br>

### Features:
✔ O sistema pode incluir informações de título, gênero, ano e avaliação dos filmes / The application can include information about the movie's title, genre, year, and rating.

✔ CRUD: O sistema inclui funções de criar, atualizar, listar, deletar e pesquisar filmes / The application can create, update, list, delete, and search for movies.

✔ Serialização dos dados em json / Data serialization in json format.

✔ Listagem paginada / Paginated listing.

✔ Listagem com agrupamento por gênero, ano ou avaliação / List movies grouping by genre, year, or rating.

<br>

### Configurando o ambiente / Environment configuration
1. Ter o Python instalado no seu computador (para o desenvolvimento dessa aplicação foi usada a versão 3.11.2) / You will need to have Python installed on your computer (version 3.11.2 was used for the development of this application).

2. Clonar o repositório / clone the repository:
```bash
git clone https://github.com/viquiiz/python-gestao-filmes.git
``` 

3. Abrir a pasta na IDE de sua escolha e instalar as bibliotecas contidas no arquivo requirements.txt via terminal / Open the folder in the IDE of your choice and install the libraries contained in the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Como rodar / how to run
1. Na pasta raiz do projeto, rodar o arquivo main.py / In the project root folder, run the main.py file:
```bash
python main.py
```

<hr>

### Exemplos de uso / usage examples

1. Cadastrando / adding movies

<img src="./assets/exemplo-cadastrar.png">

Neste caso temos um exemplo onde o usuário inclui um novo filme ao banco de dados (arquivo db.json) passando por diversas etapas de validação, como por exemplo: o título e gênero não podem ficar em branco, os campos ano e nota apenas aceitam números, o ano precisa ser um número de quatro dígitos e a nota precisa estar entre zero e 10. O id é gerado automaticamente com base no último id já cadastrado.

In this example the user adds a new film to the database (db.json file) going through several validation steps, for example: the title and genre cannot be left blank, the year and rating fields only accept numbers, the year must be a four-digit number and the grade must be between zero and 10. The id is automatically generated based on the last id already registered.

<br>

2. Pesquisando / searching

<img src="./assets/exemplo-pesquisar.png">

Nesta segunda imagem é mostrado um exemplo de pesquisa por título do filme. Ao fazer a pesquisa por "senhor dos aneis" são exibidos todos os filmes em que se encontra essa correspondência no título. Também seria possível fazer a pesquisa por ano, gênero, avaliação ou id dos filmes. Ao clonar esse repositório, o arquivo db.json já trás alguns filmes cadastrados para testar a pesquisa. 

This second image shows an example of searching by movie title. When searching for "Lord of the Rings" all films containing this sentence in the title are displayed. It would also be possible to search by year, genre, rating or film ID. When cloning this repository, the db.json file already contains some films registered to test.

<br>

3. Listando / listing

<img src="./assets/exemplo-listar.png">

Este exemplo mostra como é apresentada a listagem de todos os filmes na aplicação, com paginação exibindo 5 resultados por vez e contagem de páginas no final do print.

This example shows how the list of all films in the application is presented, with pagination displaying 5 results at a time and page count at the end of the print.

<br>

4. Excluindo / deleting

<img src="./assets/exemplo-deletar.png">

No exemplo acima o usuário escolhe um id de filme para ser excluído do banco de dados, no caso, o id número 1. As informações do filme em questão são exibidas na tela para que seja feita uma confirmação da exclusão ou não do filme.

Here the user chooses a film id to be deleted from the database, in this case, id number 1. The information about the film in question is displayed on the screen to confirm whether or not this is the right movie to be deleted.
