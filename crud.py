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

    db_livros = os.path.join(os.getcwd(), 'database\\arcevo_de_livros.json')

    if os.path.exists(db_livros):
        with open(db_livros, 'r', encoding="utf-8") as arq:
            try:
                livros = json.loads(arq.read())
            except json.decoder.JSONDecodeError:
                livros = []
    else:
        livros = []

    livros.append(livro)

    with open(db_livros, 'w', encoding='UTF-8') as arq:
        json.dump(livros, arq, ensure_ascii=False, indent=4)

    print()
    print('*' * 50)
    print('Livro adicionado com sucesso')
    print('*' * 50)
    print()

#ok
def editar_livro(isbn_livro):
    origem = os.path.join(os.getcwd(), 'database\\arcevo_de_livros.json')

    with open(origem, 'r', encoding='utf-8') as arq:
        livros = json.loads(arq.read())

    for livro in livros:
        if livro['isbn'] == isbn_livro:
            nova_quantidade = int(input("Digite o nova quantidade: "))
            livro['quantidade'] = nova_quantidade
            novo_preco = float(input("Digite o valor do livro: R$"))
            livro['preco'] = novo_preco

            with open(origem, 'w', encoding='UTF-8') as arq:
                json.dump(livros, arq, ensure_ascii=False, indent=4)

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
    listagem = os.path.join(os.getcwd(), 'database\\arcevo_de_livros.json')

    if not os.path.exists(listagem):
        print('Arquivo não encontrado')
        return


    with open(listagem, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    if len(dados) == 0:
        print('Nenhum tipo encontrado')
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






