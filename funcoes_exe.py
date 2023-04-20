import json

menu_ = ['Sair', 'Listar', 'Criar', 'Alterar', 'Deletar']

database = {'Estudantes': [],
            'Disciplinas': [],
            'Professor': [],
            'Turmas': [],
            'Matriculas': []
            }

menu_opcoes = {
    'a': 'Estudantes',
    'b': 'Disciplinas',
    'c': 'Professor',
    'd': 'Turmas',
    'e': 'Matriculas'
}

def inicializacao():
    print('{0}***** |{1}{2}Bem Vindo ao SISTEMA PUC {3}{0}| *****{1}\n'.format(
        '\033[0;33m', '\033[m', '\033[4;34m', '\033[m'))


def crud():
    print("1 - Listar")
    print("2 - Criar")
    print("3 - Alterar")
    print("4 - Deletar")
    print("0 - Sair\n")


def opcao():
    print("a - Estudante")
    print("b - Disciplina")
    print("c - Professor")
    print("d - Turma")
    print("e - Matrícula")
    print("v - Voltar\n")


def listar(menu):
    dados = verifica_json(menu_[1])
    if menu == "Estudantes":
        if len(dados[menu]) == 0:
            print(f'Não há {menu} a serem listados!')
        else:
            encontrado = False
            for estudante in dados[menu]:
                print(f'- {estudante["nome"]}')
                nome_estudante = str(input("Digite o nome do estudante que deseja listar: "))
                if estudante['nome'] == nome_estudante:
                    print("Dados do estudante:")
                    print("ID: ", estudante['id'])
                    print("Nome: ", estudante['nome'])
                    print("Código: ", estudante['codigo'])
                    print("CPF: ", estudante['CPF'])
                    encontrado = True
                    break
            if not encontrado:
                print("Estudante não encontrado.")

    if menu == "Disciplinas":
        if len(dados[menu]) == 0:
            print(f'Não há {menu} a serem listadas!')
        else:
            encontrado = False
            for disciplina in dados[menu]:
                print(f'- {disciplina["nome da disciplina"]}')
                nome_disciplina = str(input("Digite o nome da disciplina que deseja listar: "))
                if disciplina['nome da disciplina'] == nome_disciplina:
                    print("Dados da Disciplina:")
                    print("ID: ", disciplina['id'])
                    print("Nome da disciplina: ", disciplina['nome da disciplina'])
                    print("Código da disciplina: ", disciplina['codigo da disciplina'])
                    encontrado = True
                    break
            if not encontrado:
                print("Disciplina não encontrada.")

    if menu == "Professor":
        if len(dados[menu]) == 0:
            print(f'Não há {menu} a serem listados!')
        else:
            encontrado = False
            for professor in dados[menu]:
                print(f'- {professor["nome do Professor"]}')
                nome_professor = str(input("Digite o nome do professor que deseja listar: "))
                if professor['nome do Professor'] == nome_professor:
                    print("Dados do Professor:")
                    print("ID: ", professor['id'])
                    print("Código do Professor: ", professor['codigo do Professor'])
                    print("Nome do Professor: ", professor['nome do Professor'])
                    print("CPF do Professor: ", professor['CPF do Professor'])
                    encontrado = True
                    break
            if not encontrado:
                print("Professor não encontrado.")

    if menu == "Turmas":
        if len(dados[menu]) == 0:
            print(f'Não há {menu} a serem listadas!')
        else:
            encontrado = False
            for turma in dados[menu]:
                print(f'- {turma["codigo da turma"]}')
                codigo_turma = int(input("Digite o código da turma que deseja listar: "))
                if turma['codigo da turma'] == codigo_turma:
                    print("Dados da turma:")
                    print("Codigo da turma: ", turma['codigo da turma'])
                    print("Codigo do professor: ", turma['codigo do professor'])
                    print("Codigo da disciplina: ", turma['codigo da disciplina'])
                    encontrado = True
                    break
            if not encontrado:
                print("Turma não encontrado.")

    if menu == "Matriculas":
        if len(dados[menu]) == 0:
            print(f'Não há {menu} a serem listadas!')
        else:
            encontrado = False
            for matricula in dados[menu]:
                print(f'- {matricula["codigo da turma"]}')
                codigo_matricula = int(input("Digite o código da turma que deseja listar: "))
                if matricula['codigo da turma'] == codigo_matricula:
                    print("Dados da matrícula:")
                    print("Codigo da turma: ", matricula['codigo da turma'])
                    print("Codigo do estudante: ", matricula['codigo do estudante'])
                    encontrado = True
                    break
            if not encontrado:
                print("Matrícula não encontrado.")


def criar(menu):
    dicionario = verifica_json(menu_[2])
    if menu == 'Estudantes':
        estudante = str(input('Nome do estudante:')).lower()
        codigo = int(input('Código do estudante: '))
        cpf_aluno = str(input('CPF do estudante: '))
        enter = input('Pressione ENTER para continuar.')
        dicionario[menu].append(
            {
                "id": int(cpf_aluno),
                "nome": estudante,
                "codigo": codigo,
                "CPF": cpf_aluno
            }
        )

        gravar_json(dicionario)

    elif menu == 'Disciplinas':
        nome_disciplina = str(input('Nome da disciplina:')).lower()
        codigo_disciplina = int(input('Código da disciplina: '))
        enter = input('Pressione ENTER para continuar.')
        dicionario[menu].append(
            {
                "id": int(codigo_disciplina),
                "nome da disciplina": nome_disciplina,
                "codigo da disciplina": codigo_disciplina
            }
        )

        gravar_json(dicionario)

    elif menu == 'Professor':
        codigo_professor = int(input('Código do Professor: '))
        nome_professor = str(input('Nome do Professor: ')).lower()
        cpf_professor = str(input("CPF do professor: "))
        enter = input('Pressione ENTER para continuar.')
        dicionario[menu].append(
            {
                "id": int(codigo_professor),
                "codigo do Professor": codigo_professor,
                "nome do Professor": nome_professor,
                "CPF do Professor": cpf_professor
            }
        )

        gravar_json(dicionario)

    elif menu == 'Turmas':
        codigo_turma = int(input('Código da Turma: '))
        codigo_professor = int(input('Código do Professor: '))
        codigo_disciplina = int(input("Código da Disciplina: "))
        enter = input('Pressione ENTER para continuar.')
        dicionario[menu].append(
            {
                "codigo da turma": codigo_turma,
                "codigo do professor": codigo_professor,
                "codigo da disciplina": codigo_disciplina
            }
        )
        gravar_json(dicionario)

    elif menu == 'Matriculas':
        codigo_turma = int(input('Código da Turma:'))
        codigo_estudante = int(input('Código do Estudante: '))
        enter = input('Pressione ENTER para continuar.')
        dicionario[menu].append(
            {
                "codigo da turma": codigo_turma,
                "codigo do estudante": codigo_estudante,
            }
        )
        gravar_json(dicionario)
    else:
        print('Em desenvolvimento...')


def alterar(menu):
    dicionario = verifica_json(menu_[3])
    if menu == 'Estudantes':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem alterados!')
        else:
            for estudante in dicionario[menu]:
                print(f'- {estudante["nome"]}')
                nome_estudante = str(input('Qual o nome do estudante que deseja editar os dados: '))
                if estudante["nome"] == nome_estudante:
                    estudante["nome"] = str(input('Nome do estudante: '))
                    estudante["codigo"] = int(input('Código do estudante: '))
                    estudante["CPF"] = str(input('CPF do estudante: '))
                    estudante["id"] = int(estudante["CPF"])
                    print(f'Os dados do estudante {estudante["nome"]} foram atualizados com sucesso!')
                    break
                else:
                    print(f'O estudante {nome_estudante} não foi encontrado!')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Disciplinas':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem alteradas!')
        else:
            for disciplina in dicionario[menu]:
                print(f'- {disciplina["nome da disciplina"]}')
                nome_disciplina = str(input('Qual o nome da disciplina que deseja editar os dados: '))
                if disciplina["nome da disciplina"] == nome_disciplina:
                    disciplina["nome da disciplina"] = str(input('Nome da Disciplina: '))
                    disciplina["nome do professor"] = str(input('Nome do professor: '))
                    disciplina["codigo da disciplina"] = str(input('Código da disciplina: '))
                    print(f'Os dados da disciplina {disciplina["nome da disciplina"]} foram atualizados com sucesso!')
                    break
                else:
                    print(f'A disciplina {nome_disciplina} não foi encontrado!')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Professor':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem alterados!')
        else:
            for professor in dicionario[menu]:
                print(f'- {professor["nome do Professor"]}')
                nome_professor = str(input('Qual o nome do professor que deseja editar os dados: '))
                if professor["nome do Professor"] == nome_professor:
                    professor["nome do Professor"] = str(input('Nome do Professor: '))
                    professor["codigo do Professor"] = int(input('Código do professor: '))
                    professor["CPF do Professor"] = str(input('CPF do professor: '))
                    print(f'Os dados do professor {professor["nome do Professor"]} foram atualizados com sucesso!')
                    break
                else:
                    print(f'O professor {nome_professor} não foi encontrado!')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Turmas':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem alteradas!')
        else:
            for turma in dicionario[menu]:
                print(f'- {turma["codigo da turma"]}')
                cod_turma = int(input('Qual o código da turma que deseja editar os dados: '))
                if turma["codigo da turma"] == cod_turma:
                    turma["codigo da turma"] = int(input('Código da turma: '))
                    turma["codigo do professor"] = int(input('Código do professor: '))
                    turma["codigo da disciplina"] = int(input('Código da disciplina: '))
                    print(f'Os dados da turma {turma["codigo da turma"]} foram atualizados com sucesso!')
                    break
                else:
                    print(f'A turma {cod_turma} não foi encontrado!')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Matriculas':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem alteradas!')
        else:
            for matricula in dicionario[menu]:
                print(f'- {matricula["codigo do estudante"]}')
                cod_estudante = int(input('Qual o código do estudante que deseja editar os dados: '))
                if matricula["codigo do estudante"] == cod_estudante:
                    matricula["codigo do estudante"] = int(input('Código do estudante: '))
                    matricula["codigo da turma"] = int(input('Código da turma: '))
                    print(f'Os dados da matrícula {matricula["codigo do estudante"]} foram atualizados com sucesso!')
                    break
                else:
                    print(f'A matrícula {cod_estudante} não foi encontrado!')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

def deletar(menu):
    dicionario = verifica_json(menu_[4])
    if menu == 'Estudantes':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem deletados!')
        else:
            for estudante in dicionario[menu]:
                print(f'- {estudante["nome"]}')
                nome_estudante = str(input('Qual o nome do estudante que deseja deletar: '))
                for i in range(len(dicionario[menu])):
                    if dicionario[menu][i]["nome"] == nome_estudante:
                        del dicionario[menu][i]
                        print(f'O estudante {nome_estudante} foi excluído com sucesso.')
                        break
                    else:
                        print(f'O estudante {nome_estudante} não foi encontrado.')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Disciplinas':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem deletadas!')
        else:
            for disciplina in dicionario[menu]:
                print(f'- {disciplina["nome da disciplina"]}')
                nome_disciplina = str(input('Qual o nome da disciplina que deseja deletar: ')).lower()
                for i in range(len(dicionario[menu])):
                    if dicionario[menu][i]["nome da disciplina"] == nome_disciplina:
                        del dicionario[menu][i]
                        print(f'A disciplina {nome_disciplina} foi excluída com sucesso.')
                        break
                    else:
                        print(f'A disciplina {nome_disciplina} não foi encontrada.')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Professor':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem deletados!')
        else:
            for professor in dicionario[menu]:
                print(f'- {professor["nome do Professor"]}')
                nome_professor = str(input('Qual o nome do professor que deseja deletar: ')).lower()
                for i in range(len(dicionario[menu])):
                    if dicionario[menu][i]["nome do Professor"] == nome_professor:
                        del dicionario[menu][i]
                        print(f'O professor {nome_professor} foi excluído com sucesso.')
                        break
                    else:
                        print(f'O professor {nome_professor} não foi encontrado.')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Turmas':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem deletadas!')
        else:
            for turma in dicionario[menu]:
                print(f'- {turma["codigo da turma"]}')
                cod_turma = int(input('Qual o código da turma que deseja deletar: '))
                for i in range(len(dicionario[menu])):
                    if dicionario[menu][i]["codigo da turma"] == cod_turma:
                        del dicionario[menu][i]
                        print(f'A turma {cod_turma} foi excluída com sucesso.')
                        break
                    else:
                        print(f'A turma {cod_turma} não foi encontrada.')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)

    if menu == 'Matriculas':
        if len(dicionario[menu]) == 0:
            print(f'Não há {menu} a serem deletadas!')
        else:
            for matricula in dicionario[menu]:
                print(f'- {matricula["codigo do estudante"]}')
                cod_estudante = int(input('Qual a matrícula que deseja deletar: '))
                for i in range(len(dicionario[menu])):
                    if dicionario[menu][i]["codigo do estudante"] == cod_estudante:
                        del dicionario[menu][i]
                        print(f'A matrícula {cod_estudante} foi excluída com sucesso.')
                        break
                    else:
                        print(f'A matrícula {cod_estudante} não foi encontrada.')

        # Salva o dicionário de volta no arquivo .json
        gravar_json(dicionario)


def em_desenvolvimento():
    print('Em desenvolvimento...')


def acessando_menu(item):
    print('\n')
    print("Você está acessando a página '{1}{0}{2}'!\n".format(
        item, '\033[4;34m', '\033[m'))


def acessando_opcoes(item1, item2):
    print('\n')
    print("Você está acessando a página '{2}{0}{3}' na tela de '{2}{1}{3}'!\n".format(
        item1, item2, '\033[4;34m', '\033[m'))


def opcao_invalida():
    print('\n')
    print('opção inválida, escolha novamente uma opção!')


def verifica_json(opcao):
    with open("database.json", "r", encoding="utf-8") as lerDataBase:
        database_ = lerDataBase.read()

    if not database_:
        print('Não há cadastros para listar!')
        database = {'Estudantes': [],
                    'Disciplinas': [],
                    'Professor': [],
                    'Turmas': [],
                    'Matriculas': []
                    }
        dados = json.dumps(database, indent=2)
        with open("database.json", "w") as gravarDados:
            gravarDados.write(dados)

        return database

    if not database_:
        print('Não há cadastros para listar!')
        database = {'Estudantes': [],
                    'Disciplinas': [],
                    'Professor': [],
                    'Turmas': [],
                    'Matriculas': []
                    }
        dados = json.dumps(database, indent=2)
        with open("database.json", "w") as gravarDados:
            gravarDados.write(dados)

        return database
    else:
        return json.loads(database_)


def gravar_json(dict):
    dados = json.dumps(dict, indent=2)
    with open("database.json", "w") as gravarDados:
        gravarDados.write(dados)
    gravarDados.close()


0