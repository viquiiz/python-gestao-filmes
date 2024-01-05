import gerenciador_db
import unicodedata

#função para atualizar dados de um filme
def atualizar_filme():
    lista_filmes = gerenciador_db.abrir_db()

    print('\n=== Atualizar filme ===\n')
    while True:
        try:
            atualizar = int(input('Digite o id do filme que deseja atualizar ou digite no número "0" para voltar ao menu principal: '))
            if atualizar == 0:
                break
            elif not any(filme['id'] == atualizar for filme in lista_filmes['filmes']):
                print('Id não encontrado, tente novamente.')
                continue
            else:
                for filme in lista_filmes['filmes']:
                    if atualizar == filme['id']:
                        gerenciador_db.print_padrao(filme)
                        while True:
                            opcao = input('Deseja atualizar o nome deste filme? [S/N] ')
                            if opcao.lower() == 's':
                                nome = input('Digite o nome do filme: ')
                                if len(nome) < 1:
                                    print('O nome não pode ficar em branco.')
                                    continue
                                else:
                                    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII') #Armazena o nome sem caracteres especiais
                                    break
                            if opcao.lower() == 'n':
                                nome = filme['nome']
                                break
                            else:
                                print('Você digitou uma opção inválida.')
                                continue
                        while True:
                            opcao = input('Deseja atualizar o gênero deste filme? [S/N] ')
                            if opcao.lower() == 's':
                                genero = input('Digite o gênero do filme: ')
                                if len(nome) < 1:
                                    print('O gênero não pode ficar em branco.')
                                    continue
                                else:
                                    genero = unicodedata.normalize('NFKD', genero).encode('ASCII', 'ignore').decode('ASCII') #Armazena o gênero sem caracteres especiais
                                    break
                            if opcao.lower() == 'n':
                                genero = filme['genero']
                                break
                            else:
                                print('Você digitou uma opção inválida.')
                                continue
                        while True:
                            opcao = input('Deseja atualizar o ano deste filme? [S/N] ')
                            if opcao.lower() == 's':
                                try:
                                    ano = int(input('Digite o ano do filme: '))
                                    if len(str(ano)) != 4:
                                        print('Digite um ano válido.')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print('O ano só aceita números.')
                                    continue
                            if opcao.lower() == 'n':
                                ano = filme['ano']
                                break
                            else:
                                print('Você digitou uma opção inválida.')
                                continue                            
                        while True:
                            opcao = input('Deseja atualizar a nota deste filme? [S/N] ')
                            if opcao.lower() == 's':
                                try:
                                    nota = float(input('Digite a nota do filme: '))
                                    if nota < 0 or nota > 10:
                                        print('A nota precisa ser de 0 a 10.')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print('A nota só aceita números.')
                            if opcao.lower() == 'n':
                                nota = filme['nota']
                                break
                            else:
                                print('Você digitou uma opção inválida.')
                                continue
                        filme.update({'nome': nome, 'genero': genero, 'ano': ano, 'nota': nota})
                        gerenciador_db.atualizar_db(lista_filmes)
                        print('\nFilme atualizado com sucesso!')
                        gerenciador_db.print_padrao(filme) 
        except ValueError:
            print('Digite apenas números.')