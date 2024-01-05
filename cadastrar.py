import gerenciador_db
import unicodedata

#função que gera automaticamente um novo id a partir do último id da lista atual
def novo_id():
    lista_filmes = gerenciador_db.abrir_db()
    ultimo_filme = lista_filmes['filmes'][-1]
    id_atual = ultimo_filme.get('id')
    return id_atual + 1

#função para cadastrar filmes novos
def cadastrar_filme():
    lista_filmes = gerenciador_db.abrir_db()
    id = novo_id()

    print('\n=== Cadastrar novo filme ===\n')
    print('Id do filme: {}'.format(id))
    while True:
        nome = input('Digite o título do filme: ')
        if len(nome) < 1:
            print('O nome precisa ser informado.')
            continue
        else:
            nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII') #Armazena o nome sem caracteres especiais
            break
    while True:
        genero = input('Digite o gênero do filme: ')
        if len(genero) < 1:
            print('O gênero precisa ser informado.')
            continue
        else: 
            genero = unicodedata.normalize('NFKD', genero).encode('ASCII', 'ignore').decode('ASCII') #Armazena o gênero sem caracteres especiais
            break
    while True:
        try:
            ano = int(input('Digite o ano do filme: '))
            if len(str(ano)) != 4:
                print('Digite um ano válido.')
                continue
            else:
                break
        except ValueError:
            print('Digite apenas números.')
            continue
    while True:
        try:
            nota = float(input('Digite a nota do filme (de 0 a 10): ')) 
            if nota >= 0 and nota <= 10:
                break
            elif nota < 0 or nota > 10:
                print('Aceita apenas notas de 0 a 10.')
                continue
        except ValueError:
            print('Digite apenas números.')
            continue


    filme = {'id': id, 'nome': nome, 'genero': genero, 'ano': ano, 'nota': nota} #criando o dicionário

    lista_filmes['filmes'].append(filme)
    
    gerenciador_db.atualizar_db(lista_filmes) #adicionando o dicionário na lista
    print('\nFilme {} adicionado à lista com sucesso! Voltando ao menu principal.'.format(filme.get('nome')))