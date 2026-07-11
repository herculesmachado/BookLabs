from crud import adicionar_livro, editar_livro, buscar_livro
from menu import menu

while True:

    menu()
    op = int(input("Digite uma das opções: "))

    match op:
        case 1:
            isbn = int(input("Digite o ISBN: "))
            titulo = input("Digite o titulo: ").upper()
            autor = input("Digite o nome do autor: ").capitalize()
            editora = input("Digite a editora: ").capitalize()
            genero = input("Digite o genero: ").capitalize()
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o valor do livro: R$"))

            adicionar_livro(isbn, titulo, autor, editora, genero, quantidade, preco)

        case 2:
            isbn = int(input("Digite o ISBN para editar: "))
            editar_livro(isbn)

        case 3:
            buscador = input("Digite o ISBN ou autor para buscar informações: ")
            buscar_livro(buscador)

        case 4:
            print("="*50)
            print("Obrigado por utilizar o nosso sistema")
            print("="*50)
            break

















