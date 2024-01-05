import gerenciador_db
import click

#função que mostra 5 resultados por página
def paginar_filmes(lista_filmes, filmes_por_pagina):
    numero_paginas = 0
    paginas = [lista_filmes[i:i + filmes_por_pagina] for i in range(0, len(lista_filmes), filmes_por_pagina)]
    for pagina in paginas:
        numero_paginas += 1
        for filme in pagina:
            click.echo(gerenciador_db.print_padrao(filme))
        click.pause(info='Página {} de {}. Mostrando {} filmes. Pressione qualquer tecla para mostrar a próxima página.'.format(numero_paginas, len(paginas), len(pagina)))


#função para listar todos os filmes
def listar_filmes():
    
    lista_filmes = gerenciador_db.abrir_db()

    print('=== Listando todos os filmes ===\n')
    if len(lista_filmes) > 0: #verifica se existem filmes cadastrados
            paginar_filmes(lista_filmes['filmes'], 5)
    else:
        print('\nNão há filmes cadastrados.')