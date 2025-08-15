livros = ["Dom Casmurro", "1984", "O Pequeno Príncipe"]
livrarias = ["Saraiva", "Moderna", "Rocco", "Intrinseca"]

matrizExemplares = [[0 for _ in livrarias] for _ in livros]
matrizValores = [[0 for _ in livrarias] for _ in livros]

def mostrar_integrantes():
    print("\nCriado por: Gabriel Péla, Johann\n")

def menu():
    print("\n==== Sistema de Gerenciamento de Biblioteca ====")
    print("1. Cadastrar quantidade e valor dos livros")
    print("2. Listar acervo")
    print("3. Buscar por livro e livraria")
    print("4. Atualizar dados")
    print("5. Relatório: Livros acima de determinado valor")
    print("0. Sair")

def menu_livros():
    print("========= Livros =========")
    for i, livro in enumerate(livros):
        print(f"{i+1}. {livro}")

def menu_livrarias():
    print("========= Livrarias =========")
    for i, livraria in enumerate(livrarias):
        print(f"{i+1}. {livraria}")


def cadastrar():
    for i, livro in enumerate(livros):
        print(f"\nLivro: {livro}")
        for j, livraria in enumerate(livrarias):
            qtd = int(input(f"Quantidade de exemplares em {livraria}: "))
            matrizExemplares[i][j] = qtd
            while True:
                try:
                    valor = float(input(f"Valor do livro em {livraria}: "))
                    if 0 < valor:
                        matrizValores[i][j] = valor
                        break
                    else:
                        print("O valor deve ser acima de 0.")
                except ValueError:
                    print("Entrada inválida. Digite números válidos.")

def listar():
    print("\n== QUANTIDADE DE EXEMPLARES ==")
    print(f"{'':20}", end='')
    for livraria in livrarias:
        print(f"{livraria:>20}", end='')
    print()
    for i, livro in enumerate(livros):
        print(f"{livro:20}", end='')
        for qtd in matrizExemplares[i]:
            print(f"{qtd:20}", end='')
        print()

    print("\n== VALOR ==")
    print(f"{'':20}", end='')
    for livraria in livrarias:
        print(f"{livraria:>20}", end='')
    print()
    for i, livro in enumerate(livros):
        print(f"{livro:20}", end='')
        for valor in matrizValores[i]:
            print(f"{valor:20.1f}", end='')
        print()

def buscar():
    menu_livros()
    livro = int(input("Selecione o livro: "))
    menu_livrarias()
    livraria = int(input("Selecione a livraria: "))

    if livro in range(1, 4) and livraria in range(1, 5):
        i = livro - 1
        j = livraria - 1
        print(f"Exemplares: {matrizExemplares[i][j]}, Valor: {matrizValores[i][j]:.2f}")
    else:
        print("Livro ou valor não encontrados.")

def atualizar():
    menu_livros()
    livro = int(input("Selecione o livro: "))
    menu_livrarias()
    livraria = int(input("Selecione a livraria: "))

    if livro in range(1, 4) and livraria in range(1, 5):
        i = livro - 1
        j = livraria - 1
        try:
            novo_qtd = int(input("Nova quantidade de exemplares: "))
            novo_valor = float(input("Novo valor: "))
            if 0 < novo_valor:
                matrizExemplares[i][j] = novo_qtd
                matrizValores[i][j] = novo_valor
                print("Dados atualizados com sucesso.")
            else:
                print("Valor inválido.")
        except ValueError:
            print("Entrada inválida.")
    else:
        print("Livro ou livraria não encontrados.")

def relatorio():
    try:
        limite = float(input("Listar livros acima de qual valor? "))
        print(f"\nLivros com valor acima de R${limite}:\n")
        for i, livro in enumerate(livros):
            for j, livraria in enumerate(livrarias):
                if matrizValores[i][j] > limite:
                    print(f"{livraria} - {livro}: R${matrizValores[i][j]}")
    except ValueError:
        print("Entrada inválida.")

mostrar_integrantes()
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        buscar()
    elif opcao == '4':
        atualizar()
    elif opcao == '5':
        relatorio()
    elif opcao == '0':
        print("Saindo do sistema. Até a próxima!")
        mostrar_integrantes()
        break
    else:
        print("Opção inválida. Tente novamente.")