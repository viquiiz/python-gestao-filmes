import click
import gerenciador_db

def paginar_filmes(lista_filmes, filmes_por_pagina=5):
    paginas = [lista_filmes[i:i + filmes_por_pagina] for i in range(0, len(lista_filmes), filmes_por_pagina)]

    for pagina in paginas:
        for filme in pagina:
            click.echo(gerenciador_db.print_padrao(filme))
        click.pause(info='Pressione qualquer tecla para mostrar a próxima página.')

if __name__ == '__main__':
    lista_filmes = gerenciador_db.abrir_db()

    paginar_filmes(lista_filmes['filmes'])
