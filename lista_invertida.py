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
    
    #adiciona elemento à tabela
    def addElemento(self, elemento):
        self.__elementos.append(elemento)
        self.__dirComida.add(elemento)
        self.__dirCidade.add(elemento)
        self.__dirAltura.add(elemento)
        selection_sort(self.__elementos)

    #deleta elemento da tabela
    def delElemento(self, NomeElemento):
        for elemento in self.__elementos:
            if elemento.nome == NomeElemento:
                self.__elementos.remove(elemento)
                break

    def getElementos(self):
        return self.__elementos
    
    #método de busca simples
    def busca_simples(self, tabela, coluna, espec):
        if coluna == "comida":
            return getattr(tabela.dirComida, espec)
        elif coluna == "cidade":
            return getattr(tabela.dirCidade, espec)
        elif coluna == "altura":
            return getattr(tabela.dirAltura, espec)
    #funcao auxiliar  
    def buscar_por_ID(self, id, alt):
            for elemento in self.__elementos:
                if id == elemento.id and alt == elemento.altura:
                    return elemento.altura

    #método de busca composta  
    def busca_composta(self, criterio1, criterio2):
        listacriterio1 = None
        listacriterio2 = None

        if criterio1 == "macarrao" or criterio1 == "feijao" or criterio1 == "arroz":
            listacriterio1 = getattr(self.__dirComida, criterio1)
        elif criterio1 == "floripa" or criterio1 == "biguacu" or criterio1 == "palhoca":
            listacriterio1 = getattr(self.__dirCidade, criterio1)
        else:
            listaintervalo = None
            listacriterio1 = []
            if (1.69 >= float(criterio1)):
                listaintervalo = self.__dirAltura.ate_169

            elif (1.70 <= float(criterio1) <= 1.79):
                listaintervalo = self.__dirAltura._170_179

            elif (1.80 <= float(criterio1)):
                listaintervalo = self.__dirAltura._180_mais

            for id in listaintervalo:
                if float(criterio1) == self.buscar_por_ID(id, float(criterio1)):
                    listacriterio1.append(id)

            # listacriterio1 = getattr(self.__dirAltura, criterio1)

        if criterio2 == "macarrao" or criterio2 == "feijao" or criterio2 == "arroz":
            listacriterio2 = getattr(self.__dirComida, criterio2)
        elif criterio2 == "floripa" or criterio2 == "biguacu" or criterio2 == "palhoca":
            listacriterio2 = getattr(self.__dirCidade, criterio2)
        else:
            listaintervalo = None
            listacriterio2 = []
            if (1.69 >= float(criterio2)):
                listaintervalo = self.__dirAltura.ate_169

            elif (1.70 <= float(criterio2) <= 1.79):
                listaintervalo = self.__dirAltura._170_179

            elif (1.80 <= float(criterio2)):
                listaintervalo = self.__dirAltura._180_mais

            for id in listaintervalo:
                if float(criterio2) == self.buscar_por_ID(id, float(criterio2)):
                    listacriterio2.append(id)

        resultado = list(set(listacriterio1) & set(listacriterio2))

        return resultado

#classe do diretorio das cidades
class DiretorioCidade:
    def __init__(self):
        self.__floripa = []
        self.__biguacu= []
        self.__palhoca = []

    @property
    def floripa(self):
        return self.__floripa
    
    @property
    def biguacu(self):
        return self.__biguacu
    
    @property
    def palhoca(self):
        return self.__palhoca

    def add(self, elemento):
        try:
            cidade = elemento.cidade.lower()

            if cidade == "floripa":
                self.__floripa.append(elemento.id)
            elif cidade == "biguacu":
                self.__biguacu.append(elemento.id)
            elif cidade == "palhoca":
                self.__palhoca.append(elemento.id)
            else:
                raise ValueError(f"Valor de cidade inválido: {cidade}")
            
        except ValueError as e:
            print(f"Erro de valor: {e}")

#classe do diretorio das comidas
class DiretorioComida:
    def __init__(self):
        self.__macarrao = []
        self.__feijao = []
        self.__arroz = []

    @property
    def macarrao(self):
        return self.__macarrao
    
    @property
    def feijao(self):
        return self.__feijao
    
    @property
    def arroz(self):
        return self.__arroz


    def add(self, elemento):
        try:
            comida = elemento.comida.lower()

            if comida == "macarrao":
                self.__macarrao.append(elemento.id)
            elif comida == "feijao":
                self.__feijao.append(elemento.id)
            elif comida == "arroz":
                self.__arroz.append(elemento.id)
            else:
                raise ValueError(f"Valor de comida inválido: {comida}")
        
        except ValueError as e:
            print(f"Erro de valor: {e}")

#classe do diretório das alturas
class DiretorioAltura:
    def __init__(self):
        self.__ate_169 = []
        self.__170_179 = []
        self.__180_mais = []

    @property
    def ate_169(self):
        return self.__ate_169
    
    @property
    def _170_179(self):
        return self.__170_179
    
    @property
    def _180_mais(self):
        return self.__180_mais


    def add(self, elemento):
        if elemento.altura <= 1.69:
            self.__ate_169.append(elemento.id)
        elif 1.70 <= elemento.altura <= 1.79:
            self.__170_179.append(elemento.id)
        elif 1.80 <= elemento.altura:
            self.__180_mais.append(elemento.id)

#retorna a tabela principal
def print_tabela(tabela):
    # Imprime cabeçalho da tabela
    print(f"| {'ID':^3} | {'Nome':^10} | {'Cidade':^15} | {'Comida':^10} | {'Altura':^7} |")
    print("-" * 55)

    # Imprime cada linha da tabela
    for pessoa in tabela.elementos:
        altura_formatada = f"{pessoa.altura: .2f}"
        print(f"| {pessoa.id:^3} | {pessoa.nome:^10} | {pessoa.cidade:^15} | {pessoa.comida:^10} | {altura_formatada:^7} |")

    print("-" * 55)
    print('\n')

#retorna o diretório das comidas
def print_lista_comida(diretorio):
    print("macarrao:", diretorio.macarrao)
    print("feijao:", diretorio.feijao)
    print("arroz:", diretorio.arroz)
    print('\n')

#retorna o diretório das cidades
def print_lista_cidade(diretorio):
    print("floripa:", diretorio.floripa)
    print("biguacu:", diretorio.biguacu)
    print("palhoca:", diretorio.palhoca)
    print('\n')

#retorna o diretório das alturas dos usuários
def print_lista_altura(diretorio):
    print("até 169:", diretorio.ate_169)
    print("1,70 - 1,79:", diretorio._170_179)
    print("1,80 +:", diretorio._180_mais)
    print('\n')

#função de carga de dados
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
    print('\n')