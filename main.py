import cadastrar
import listar
import atualizar
import deletar
import pesquisar

#programa principal
print('=== Streamberry ===')
while True:
    try:
        opcao = int(input('''
Digite o número da opção desejada:
                          
1. Cadastrar filme
2. Listar todos os filmes
3. Atualizar filme
4. Deletar filme
5. Pesquisar por filme
6. Sair do programa
'''))

        if opcao == 1:
            cadastrar.cadastrar_filme()
            continue
        elif opcao == 2:
            listar.listar_filmes()
            continue
        elif opcao == 3:
            atualizar.atualizar_filme()
            continue
        elif opcao == 4:
            deletar.deletar_filme()
            continue
        elif opcao == 5:
            pesquisar.pesquisar_filmes()
            continue
        elif opcao == 6:
            print('\n=== Saindo do programa. Obrigado por usar o Streamberry :) ===\n')
            break
        else:
            print('\nVocê digitou uma opção inválida.')
            continue
    except ValueError:
        print('\nDigite apenas números por favor.')
        continue
