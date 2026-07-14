import json
import os

#ok
def adicionar_livro(isbn, titulo, autor, editora, genero, quantidade ,preco):

    livro = {
        'isbn': isbn,
        'titulo': titulo,
        'autor': autor,
        'editora': editora,
        'genero': genero,
        'quantidade': quantidade,
        'preco': preco
    }

    db_livros = os.path.join(os.getcwd(), 'database\\acervo_de_livros.json')

    if os.path.exists(db_livros):
        with open(db_livros, 'r', encoding="utf-8") as arquivo:
            try:
                livros = json.loads(arquivo.read())
            except json.decoder.JSONDecodeError:
                livros = []
    else:
        livros = []

    livros.append(livro)

    with open(db_livros, 'w', encoding='UTF-8') as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)

    print()
    print('*' * 50)
    print('Livro adicionado com sucesso')
    print('*' * 50)
    print()

#ok
def editar_livro(isbn_livro):
    origem = os.path.join(os.getcwd(), 'database\\acervo_de_livros.json')

    with open(origem, 'r', encoding='utf-8') as arquivo:
        livros = json.loads(arquivo.read())

    for livro in livros:
        if livro['isbn'] == isbn_livro:

            alterar_quantidade = input("Deseja alterar a quantidade (S/N)?: ").upper()

            if alterar_quantidade == 'S':
                nova_quantidade = int(input("Digite uma nova quantidade: "))
                livro['quantidade'] = nova_quantidade

                print()
                print('*' * 50)
                print("Quantidade alterada com sucesso")
                print('*' * 50)
                print()
            else:
                print()
                print('*' * 50)
                print("Nenhuma quantidade foi alterada")
                print('*' * 50)
                print()


            alterar_preco = input("Deseja alterar o valor (S/N)?: ").upper()

            if alterar_preco == 'S':
                novo_valor = float(input("Digite um novo valor: "))
                livro['preco'] = novo_valor

                print()
                print('*' * 50)
                print("Preço alterado com sucesso")
                print('*' * 50)
            else:
                print()
                print('*' * 50)
                print("Nenhum preço foi alterado")
                print('*' * 50)


            with open(origem, 'w', encoding='UTF-8') as arquivo:
                json.dump(livros, arquivo, ensure_ascii=False, indent=4)

            print()
            print('*' * 50)
            print('Livro editado com sucesso')
            print('*' * 50)
            print()
        else:
            print()
            print('*' * 50)
            print("Livro não encontrado")
            print('*' * 50)
            print()

        break

#ok
def buscar_livro(buscador):
    listagem = os.path.join(os.getcwd(), 'database\\acervo_de_livros.json')

    if not os.path.exists(listagem):
        print('Arquivo não encontrado')
        return


    with open(listagem, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    if len(dados) == 0:
        print()
        print('*' * 50)
        print("Livro não encontrado")
        print('*' * 50)
        print()
        return


    for livro in dados:
        if buscador.isdigit():
            encontrado = livro['isbn'] == int(buscador)
        else:
            encontrado = livro['autor'] == buscador.capitalize()


        if encontrado:
            print()
            print('*' * 50)
            print(f"Dados do livro {livro['titulo']}")
            print('*' * 50)
            print(f"ISBN: {livro['isbn']}")
            print(f"Nome: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Editora: {livro['editora']}")
            print(f"Genero: {livro['genero']}")
            print(f"Quantidade: {livro['quantidade']}")
            print(f"Preço: {livro['preco']}")
            print("*" * 50)
            print()

#ok
def excluir_livro(isbn_para_deletar ):
    listagem = os.path.join(os.getcwd(), 'database\\acervo_de_livros.json')

    with open(listagem, 'r', encoding='UTF-8') as arquivo:
        livros = json.load(arquivo)

    if len(livros) == 0:
        print()
        print('*' * 50)
        print("Livro não encontrado")
        print('*' * 50)
        print()
        return

    for livro in livros:
        if livro['isbn'] == isbn_para_deletar:
            livros.remove(livro)

            print()
            print('*' * 50)
            print('Livro excluido com sucesso')
            print('*' * 50)
            print()
        else:
            print()
            print('*' * 50)
            print("Livro não encontrado")
            print('*' * 50)
            print()


    with open(listagem, 'w', encoding='UTF-8') as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)










