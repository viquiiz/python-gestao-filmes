import gerenciador_db

#função para deletar um filme
def deletar_filme():
    lista_filmes = gerenciador_db.abrir_db()

    print('\n=== Deletar filme ===\n')
    while True:
        try:
            remover = int(input('Digite o id do filme a ser removido ou digite o número "0" para voltar ao menu principal: '))
            if remover == 0:
                break
            elif not any(filme['id'] == remover for filme in lista_filmes['filmes']):
                print('Id não encontrado, tente novamente.')
                continue
            else:
                for filme in lista_filmes['filmes']:
                    if remover == filme['id']:
                        gerenciador_db.print_padrao(filme)
                        confirma = input('Tem certeza que deseja deletar o filme acima? [S/N] '.format(filme.get('id'), filme.get('nome'), filme.get('genero'), filme.get('ano'), filme.get('nota')))
                        if confirma.lower() == 's':
                            print('\nFilme {} deletado com sucesso.\n'.format(filme.get('nome')))
                            lista_filmes['filmes'].remove(filme)
                            gerenciador_db.atualizar_db(lista_filmes)
                            break
                        else:
                            print('O filme {} não foi deletado da lista.'.format(filme.get('nome')))
                            break
        except ValueError:
            print('Digite apenas números.')
            continue