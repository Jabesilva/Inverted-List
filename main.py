from elemento import Elemento
from lista_invertida import *

def opcao1(tabela):
    cargaDados(tabela)
    
def opcao2(tabela):
    try:
        nome = input("Nome: ")
        cidade = input("Cidade (escolha entre 'floripa', 'biguacu', 'palhoca'): ").lower()
        if cidade not in ['floripa', 'biguacu', 'palhoca']:
            raise ValueError("Cidade inválida! Escolha entre 'floripa', 'biguacu', 'palhoca'.")
        comida = input("Comida (escolha entre 'macarrao', 'feijao', 'arroz'): ").lower()
        if comida not in ['macarrao', 'feijao', 'arroz']:
            raise ValueError("Comida inválida! Escolha entre 'macarrao', 'feijao', 'arroz'.")
        altura = float(input("Altura (tipo: float): "))
        if altura <= 0:
            raise ValueError("Altura inválida! Deve ser um número positivo.")

        elemento = Elemento(nome, cidade, comida, altura)

        tabela.addElemento(elemento)

        return [print_tabela(tabela), print_lista_cidade(tabela.dirCidade), print_lista_comida(tabela.dirComida), print_lista_altura(tabela.dirAltura)]

    except ValueError as e:
        print(f"Erro de valor: {e}")

def opcao3(tabela):
    nome = input("digite o nome: ")
    
    if not tabela.delElemento(nome):
        print(f"Elemento com o nome '{nome}' não encontrado.")
    else:
        tabela.delElemento(nome)
    print_tabela(tabela)

def opcao4(tabela):
    try:
        print_tabela(tabela)
        coluna = input("Coluna: ")
        espec = input("especifícação (no caso de altura, escolha entre 'ate_169', '_170_179', '_180_mais'): ")
        resultado = tabela.busca_simples(tabela, coluna, espec)
        if not resultado:
            raise ValueError("Nenhum resultado encontrado com os critérios fornecidos.")
        print(resultado)
    except ValueError as e:
        print(f"Erro de valor: {e}")

def opcao5(tabela):
    try: 
        print_tabela(tabela)
        print("no caso de selecionar uma altura específica, coloque o número em float type, ex: 0.00")
        criterio1 = input("criterio 1: ").lower()
        criterio2 = input("criterio 2: ").lower()
        resultado = tabela.busca_composta(criterio1, criterio2)
        if not resultado:
                raise ValueError("Nenhum resultado encontrado com os critérios fornecidos.")
        print(resultado)
    except ValueError as e:
        print(f"Erro de valor: {e}")

def opcao6(tabela):
    print_tabela(tabela)
    print("----------------")
    print("\n")
    print("Lista Invertida")
    print("\n")
    print("Ref Comidas")
    print(print_lista_comida(tabela.dirComida))
    print("\n")
    print(print_lista_cidade(tabela.dirCidade))
    print("\n")
    print(print_lista_altura(tabela.dirAltura))
    print('\n')


def mostrar_menu():
    print("Escolha uma das opções abaixo:")
    print("1. Carga de dados (cria a tabela e as listas invertidas)")
    print("2. Adiciona Usuário")
    print("3. Deletar Usuário (pelo nome)")
    print("4. Busca Simples")
    print("5. Busca Composta")
    print("6. exibir tabela")
    print("0. Sair")

#Menu principal
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
        elif escolha == '4':
            opcao4(tabela)
        elif escolha == '5':
            opcao5(tabela)
        elif escolha == '6':
            opcao6(tabela)
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
