from elemento import Elemento

#algoritmo selection sort para ordenação de dados, aprendido nas grandes aulas do De Lucca ;)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j].id < arr[min_index].id:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]


class Tabela:
    def __init__(self):
        self.__elementos = []
        self.__dirComida = DiretorioComida()
        self.__dirCidade = DiretorioCidade()
        self.__dirAltura = DiretorioAltura()

    @property
    def elementos(self):
        return self.__elementos
    
    @property
    def dirComida(self):
        return self.__dirComida
    
    @property
    def dirCidade(self):
        return self.__dirCidade
    
    @property
    def dirAltura(self):
        return self.__dirAltura
    
    def addElemento(self, elemento):
        self.__elementos.append(elemento)
        self.__dirComida.add(elemento)
        self.__dirCidade.add(elemento)
        self.__dirAltura.add(elemento)
        selection_sort(self.__elementos)

    def delElemento(self, NomeElemento):
        for elemento in self.__elementos:
            if elemento.nome == NomeElemento:
                self.__elementos.pop(elemento)

    def getElementos(self):
        return self.__elementos

    
class DiretorioCidade:
    def __init__(self):
        self.__lista_floripa = []
        self.__lista_biguacu= []
        self.__lista_palhoca = []

    @property
    def lista_floripa(self):
        return self.__lista_floripa
    
    @property
    def lista_biguacu(self):
        return self.__lista_biguacu
    
    @property
    def lista_palhoca(self):
        return self.__lista_palhoca

    def add(self, elemento):
        if elemento.cidade == "floripa":
            self.__lista_floripa.append(elemento.id)
        elif elemento.cidade == "biguacu":
            self.__lista_biguacu.append(elemento.id)
        else:
            self.__lista_palhoca.append(elemento.id)


class DiretorioComida:
    def __init__(self):
        self.__lista_macarrao = []
        self.__lista_feijao = []
        self.__lista_arroz = []

    @property
    def lista_macarrao(self):
        return self.__lista_macarrao
    
    @property
    def lista_feijao(self):
        return self.__lista_feijao
    
    @property
    def lista_arroz(self):
        return self.__lista_arroz


    def add(self, elemento):
        if elemento.comida == "macarrao":
            self.__lista_macarrao.append(elemento.id)
        elif elemento.comida == "feijao":
            self.__lista_feijao.append(elemento.id)
        else:
            self.__lista_arroz.append(elemento.id)

class DiretorioAltura:
    def __init__(self):
        self.__lista_ate_169 = []
        self.__lista_170_179 = []
        self.__lista_180_mais = []

    @property
    def lista_ate_169(self):
        return self.__lista_ate_169
    
    @property
    def lista_170_179(self):
        return self.__lista_170_179
    
    @property
    def lista_180_mais(self):
        return self.__lista_180_mais


    def add(self, elemento):
        if elemento.altura <= 1.69:
            self.__lista_ate_169.append(elemento.id)
        elif 1.70 <= elemento.altura <= 1.79:
            self.__lista_170_179.append(elemento.id)
        elif 1.80 <= elemento.altura:
            self.__lista_180_mais.append(elemento.id)

def print_tabela(tabela):
    # Imprime cabeçalho da tabela
    print(f"| {'ID':^3} | {'Nome':^10} | {'Cidade':^15} | {'Comida':^10} | {'Altura':^7} |")
    print("-" * 55)

    # Imprime cada linha da tabela
    for pessoa in tabela.elementos:
        altura_formatada = f"{pessoa.altura: .2f}"
        print(f"| {pessoa.id:^3} | {pessoa.nome:^10} | {pessoa.cidade:^15} | {pessoa.comida:^10} | {altura_formatada:^7} |")

    print("-" * 55)

def print_lista_comida(diretorio):
    print("macarrao:", diretorio.lista_macarrao)
    print("feijao:", diretorio.lista_feijao)
    print("arroz:", diretorio.lista_arroz)

def print_lista_cidade(diretorio):
    print("floipa:", diretorio.lista_floripa)
    print("biguacu:", diretorio.lista_biguacu)
    print("palhoca:", diretorio.lista_palhoca)

def print_lista_altura(diretorio):
    print("até 169:", diretorio.lista_ate_169)
    print("1,70 - 1,79:", diretorio.lista_170_179)
    print("1,80 +:", diretorio.lista_180_mais)


def cargaDados(tabela):
    
    e1 = Elemento("Jabes", "biguacu", "macarrao", 1.70)
    e2 = Elemento("DeLuca","floripa", "arroz", 1.73)
    e3 = Elemento("Lucas", "palhoca", "feijao", 1.65)
    e4 = Elemento("Joao", "biguacu", "macarrao", 1.67)
    e5 = Elemento("Gabriel", "palhoca", "feijao", 1.80)
    e6 = Elemento("Guilherme", "floripa", "arroz", 1.79)
    e7 = Elemento("Pedro", "biguacu", "feijao", 1.69)
    e8 = Elemento("Jorge", "palhoca", "macarrao", 1.70)
    e9 = Elemento("Maria", "floripa", "arroz", 1.50)
    e10 = Elemento("Cristina", "floripa", "macarrao", 1.89)

    tabela.addElemento(e1)
    tabela.addElemento(e2)
    tabela.addElemento(e3)
    tabela.addElemento(e4)
    tabela.addElemento(e5)
    tabela.addElemento(e6)
    tabela.addElemento(e7)
    tabela.addElemento(e8)
    tabela.addElemento(e9)
    tabela.addElemento(e10)

    print("----------------")
    print("cria a tabela")
    print("\n")
    print(print_tabela(tabela))
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