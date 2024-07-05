from elemento import Elemento
from lista_invertida import *

def opcao1(tabela):
    cargaDados(tabela)
    
def opcao2(tabela):
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    comida = input("Comida: ")
    altura = float(input("Altura (float): "))

    elemento = Elemento(nome, cidade, comida, altura)

    tabela.addElemento(elemento)

    return [print_tabela(tabela), print_lista_cidade(tabela.dirCidade), print_lista_comida(tabela.dirComida), print_lista_altura(tabela.dirAltura)]
    

def opcao3(tabela):
    nome = input("digite o nome: ")
    tabela.delElemento(nome)

def mostrar_menu():
    print("Escolha uma das opções abaixo:")
    print("1. Carga de dados (cria a tabela e as listas invertidas)")
    print("2. Adiciona Usuário")
    print("3. Deletar Usuário (pelo nome)")
    print("0. Sair")

def main():
    tabela = Tabela()
    while True:
        mostrar_menu()
        escolha = input("Digite o número da sua escolha: ")
        
        if escolha == '1':
            opcao1(tabela)
        elif escolha == '2':
            opcao2(tabela)
        elif escolha == '3':
            opcao3(tabela)
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()

# tabela = Tabela()
# cargaDados(tabela)

# e1 = Elemento("Margot", "floripa", "macarrao", 1.71)

# tabela.addElemento(e1)

# print('---------- Adicionando novo objeto -----------')
# print("\n")
# print_tabela(tabela)