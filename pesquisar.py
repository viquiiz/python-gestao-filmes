import gerenciador_db

#função para pesquisar filmes
def pesquisar_filmes():
    lista_filmes = gerenciador_db.abrir_db()

    print('\n=== Pesquisar por filme ===\n')
    while True:
        try:
            pesquisar = int(input('''
Escolha o número da opção desejada:
1. Filtrar por título
2. Filtrar por ano
3. Filtrar por gênero
4. Filtrar por avaliação
5. Voltar ao menu principal                                                               
'''))
            if pesquisar == 5:
                break
            elif pesquisar == 1:
                nome = input('Digite o título do filme a ser pesquisado: ')
                if not any(nome.lower() in filme['nome'].lower() for filme in lista_filmes['filmes']):
                    print('\nFilme não encontrado, tente novamente.')
                    continue
                else:
                    for filme in lista_filmes['filmes']:
                        if nome.lower() in filme['nome'].lower():
                            gerenciador_db.print_padrao(filme) 
                    continue
            elif pesquisar == 2:
                ano = int(input('Digite o ano a ser pesquisado: '))
                if not any(filme['ano'] == ano for filme in lista_filmes['filmes']):
                    print('\nNenhum filme registrado com este ano.')
                    continue
                else:
                    for filme in lista_filmes['filmes']:
                        if ano == filme['ano']:
                            gerenciador_db.print_padrao(filme)
                    continue
            elif pesquisar == 3:
                genero = input('Digite o gênero a ser pesquisado: ')
                if not any(filme['genero'].lower() == genero.lower() for filme in lista_filmes['filmes']):
                    print('\nNenhum filme registrado com este gênero.')
                    continue
                else:
                    for filme in lista_filmes['filmes']:
                        if genero.lower() == filme['genero'].lower():
                            gerenciador_db.print_padrao(filme) 
                    continue
            elif pesquisar == 4:
                notas = {'a': [0, 2.9], 'b': [3, 5.9], 'c':[6, 8.9], 'd':[9, 10]}
                while True:
                    nota = input('''
Digite a letra da opção desejada:
a. filmes com nota de 0 a 2,9
b. filmes com nota de 3 a 5,9
c. filmes com nota de 6 a 8,9
d. filmes com nota de 9 a 10
e. voltar ao menu anterior                                                                                                                    
''')
                    if nota.lower() == 'e':
                        break
                    elif nota.lower() in ['a', 'b', 'c', 'd']:
                        nota_inf = notas[nota][0]
                        nota_sup = notas[nota][1]
                        filmes_selecionados = []

                        for filme in lista_filmes['filmes']:
                            if (filme['nota'] >= nota_inf) and (filme['nota'] <= nota_sup):
                                filmes_selecionados.append(filme)

                        if len(filmes_selecionados) == 0:
                            print('\nNenhum filme registrado tem notas de {} a {}.'.format(nota_inf, nota_sup))
                            continue
                        else:
                            for filme in filmes_selecionados:
                                gerenciador_db.print_padrao(filme)
                                continue
                    else:
                        print('\nVocê digitou uma opção inválida. Tente novamente.')
                        continue      
        except ValueError:
            print('\nDigite apenas números por favor.')
            continue