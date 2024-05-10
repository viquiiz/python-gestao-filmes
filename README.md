# Movie Collection Manager🎬

This project is a program that allows storing, searching, deleting and updating movies from a database.

<br>

### Features:
✔ The application can include information about the movie's title, genre, year, and rating.

✔ CRUD: The application can create, update, list, delete, and search for movies.

✔ Data serialization in json format.

✔ Paginated listing.

✔  List movies grouping by genre, year, or rating.

<br>

### Environment config
1. You will need to have Python installed on your computer (version 3.11.2 was used for the development of this application).

2. Clone the repository:
```bash
git clone https://github.com/viquiiz/python-gestao-filmes.git
``` 

3. Open the folder in the IDE of your choice and install the libraries contained in the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Run
1. In the project root folder, run the main.py file:
```bash
python main.py
```

<hr>

### Usage examples

1. Add movies

<img src="./assets/exemplo-cadastrar.png">

In this example the user adds a new film to the database (db.json file) going through several validation steps, for example: the title and genre cannot be left blank, the year and rating fields only accept numbers, the year must be a four-digit number and the grade must be between zero and 10. The id is automatically generated based on the last id already registered.

<br>

2. Search movies

<img src="./assets/exemplo-pesquisar.png">

This second image shows an example of searching by movie title. When searching for "Lord of the Rings" all films containing this sentence in the title are displayed. It would also be possible to search by year, genre, rating or film ID. When cloning this repository, the db.json file already contains some films registered to test.

<br>

3. List movies

<img src="./assets/exemplo-listar.png">

This example shows how the list of all films in the application is presented, with pagination displaying 5 results at a time and page count at the end of the print.

<br>

4. Deleting movies

<img src="./assets/exemplo-deletar.png">

Here the user chooses a film id to be deleted from the database, in this case, id number 1. The information about the film in question is displayed on the screen to confirm whether or not this is the right movie to be deleted.
