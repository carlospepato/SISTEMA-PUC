"""
Nome: Carlos Eduardo Belber Braga Pepato
Curso: Raciocínio computacional
Turma: 11100010563_20231_02
"""

# Importando outro arquivo .py que contém as funções utilizadas neste arquivo
import funcoes

# Inicio do SISTEMA PUC
while True:
    funcoes.inicializacao()
    funcoes.crud()
    crud = int(input('Quais das opções acima deseja acessar:'))

    # Acessando a opção Listar
    if crud == 1:
        funcoes.acessando_menu(funcoes.menu_[crud])
        funcoes.opcao()
        opcao = str(input('Quais das opções acima deseja acessar:')).lower()

        if opcao == 'v':
            print("Você escolheu voltar!")


        elif opcao in funcoes.menu_opcoes.keys():
            funcoes.acessando_opcoes(funcoes.menu_[crud], funcoes.menu_opcoes[opcao])
            funcoes.listar(funcoes.menu_opcoes[opcao])

        else:
            funcoes.opcao_invalida()

    # Acessando a opção Criar
    elif crud == 2:
        funcoes.acessando_menu(funcoes.menu_[crud])
        funcoes.opcao()
        opcao = str(input('Quais das opções acima deseja acessar:')).lower()

        # Acessando a opção Estudante

        if opcao == 'v':
            print("Você escolheu voltar!")

        elif opcao in funcoes.menu_opcoes.keys():
            funcoes.acessando_opcoes(funcoes.menu_[crud], funcoes.menu_opcoes[opcao])
            funcoes.criar(funcoes.menu_opcoes[opcao])

        else:
            funcoes.opcao_invalida()

    # Acessando a opção Alterar
    elif crud == 3:
        funcoes.acessando_menu(funcoes.menu_[crud])
        funcoes.opcao()
        opcao = str(input('Quais das opções acima deseja acessar:')).lower()

        if opcao == 'v':
            print("Você escolheu voltar!")

        elif opcao in funcoes.menu_opcoes.keys():
            funcoes.acessando_opcoes(funcoes.menu_[crud], funcoes.menu_opcoes[opcao])
            funcoes.alterar(funcoes.menu_opcoes[opcao])

        else:
            funcoes.opcao_invalida()

    # Acessando a opção Deletar
    elif crud == 4:
        funcoes.acessando_menu(funcoes.menu_[crud])
        funcoes.opcao()
        opcao = str(input('Quais das opções acima deseja acessar:')).lower()

        if opcao == 'v':
            print("Você escolheu voltar!")

        elif opcao in funcoes.menu_opcoes.keys():
            funcoes.acessando_opcoes(funcoes.menu_[crud], funcoes.menu_opcoes[opcao])
            funcoes.deletar(funcoes.menu_opcoes[opcao])

        else:
            funcoes.opcao_invalida()

    # Encerrando o SISTEMA PUC
    elif crud == 0:
        print('Até mais!')
        break

    # Caso tenha alguma opção inválida ele passa uma mensagem e volta a mostrar as opções.
    else:
        funcoes.opcao_invalida()
