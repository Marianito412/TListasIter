#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto.
#Fecha de creacion: 13/4/2023 6:52pm
#Ultima version:  13/4/2023 8:31pm
#Version: 3.10.6

#Importación de librerias
import random

#Definición de funciones

#Reto 2
def validarBuscarElemento(pListaVal, pBuscar):
    """
    Funcionalidad: Valida las entradas de buscar elemento
    Entradas:
    -pListaVal(list): Lista a validar
    -pBuscar(int): Entero a validar
    Salidas:
    -return(bool): True si todos los elementos son enteros
    """
    for i in pListaVal + [pBuscar]:
        if not isinstance(i,int):
            try:
                if not i.is_integer():
                    return False
            except AttributeError:
                return False
    return True

def buscarElemento(pLista, pBuscar):
    """
    Funcionalidad: Busca pBuscar y cuenta sus ocurrencias
    Entradas:
    -pListaVal(list): Lista en la que buscar
    -pBuscar(int): Entero a buscar
    Salidas:
    -cuenta(int): La cantidad de ocurrrencias
    """
    cuenta = 0
    for valor in pLista:
        if valor == pBuscar:
            cuenta += 1
    return cuenta

def ESBuscarElemento(pLista, pBuscar):
    """
    Funcionalidad: Llama a buscarElemento si la entrada es válida
    Entradas:
    -pListaVal(list): Lista en la que buscar
    -pBuscar(int): Entero a buscar
    Salidas:
    -return(): True si todos los elementos son enteros
    """
    if validarBuscarElemento(pLista, pBuscar):
        return buscarElemento(pLista, pBuscar)
    else:
        return "La lista y el buscable solo pueden ser enteros"

#Reto 4
def validarListaRandom(pTammano):
    """
    Funcionalidad: Valida la entrada de listaRandom
    Entradas:
    -pTamanno(int): Entero a validar
    Salidas:
    -return(bool): True si es un entero positivo
    """
    if not isinstance(pTammano, int):
        try:
            if pTammano.is_integer():
                return False
        except AttributeError:
            return False
    return pTammano>=0

def listaRandom(pTamanno):
    """
    Funcionalidad: Crea una lista de tamaño pTamanno
    Entradas:
    -pTamanno(int): Tamaño de la lista
    Salidas:
    -lista(list): La lista generada
    """
    lista = []
    for i in range(pTamanno):
        lista.append(random.randint(1,99))
    return lista

def ESListaRandom(pTamanno):
    """
    Funcionalidad: Llama listaRandom si la entrada es válida
    Entradas:
    -pTamanno(int): Tamaño de la lista
    Salidas:
    -return(list): La lista generada
    """
    if validarListaRandom(pTamanno):
        return listaRandom(pTamanno)
    else:
        return "El tamaño de la lista debe ser un entero positivo"

#Reto 6
def validarEliminarRepetidos(pLista):
    """
    Funcionalidad: Valida la entrada de eliminarRepetidos
    Entradas:
    -pLista(list): Lista a validar
    Salidas:
    -return(bool): True si pLista es una lista
    """
    if not isinstance(pLista, list):
        return False
    return True

def eliminarRepetidos(pLista: list):
    """
    Funcionalidad: elimina los elementos repetidos en pLista
    Entradas:
    -pLista(list): Lista a limpiar
    Salidas:
    -lista(list): La lista limpia
    """
    lista = []
    i = 0
    tamannoLista = len(pLista)
    while i < tamannoLista:
        valor = pLista.pop(0)
        while valor in pLista:
            pLista.remove(valor)
            i+=1
        lista.append(valor)
        i+=1
    return lista

def ESEliminarRepetidos(pLista):
    """
    Funcionalidad: Llama a eliminarRepetidos si la entrada es válida
    Entradas:
    -pLista(list): Lista a limpiar
    Salidas:
    -return(list): La lista limpia
    """
    if validarEliminarRepetidos(pLista):
        return eliminarRepetidos(pLista)
    else:
        return "Se esperaba una lista como argumento"

#Reto 8
def validarAlternada(pLista):
    """
    Funcionalidad: Valida la entrada de alternada
    Entradas:
    -pLista(list): Lista a validar
    Salidas:
    -return(bool): True si pLista solo contiene enteros
    """
    for i in pLista:
        if not isinstance(i,int):
            try:
                if not i.is_integer():
                    return False
            except AttributeError:
                return False
    return True

def alternada(pLista):
    """
    Funcionalidad: Verifica que los enteros de una lista alterne entre pares e impares
    Entradas:
    -pLista(list): Lista a verificar
    Salidas:
    -return(bool): True si pLista se apega al patrón descrito
    """
    par = pLista[0] %2 == 0
    for i in pLista:
        if par and i%2!=0: #Si se necesita que sea par y no lo es
            return False
        if not par and i%2==0: #Si se necesita que sea impar y no lo es
            return False
        par = not par
    return True

def ESAlternada(pLista):
    """
    Funcionalidad: Llama a alternada
    Entradas:
    -pLista(list): Lista a verificar
    Salidas:
    -return(bool): True si pLista se apega al patrón descrito
    """
    if validarAlternada(pLista):
        return alternada(pLista)
    else:
        return "Los valores de la lista deben ser enteros"

#Reto 10
def validarReplicar(pLista,pNum):
    """
    Funcionalidad: Valida la entrada de replicar
    Entradas:
    -pLista(list): Lista a validar
    -pNum(int): Entero a validar
    Salidas:
    -return(bool): True si pLista es una lista y pNum es un entero mayor a cero
    """
    if not isinstance(pNum, int):
        try:
            if not pNum.is_integer():
                return False
        except AttributeError:
            return False
    return pNum>0 and isinstance(pLista, list)

def replicar(pLista, pCopia):
    """
    Funcionalidad: Replica los elementos de una lista pCopia veces
    Entradas:
    -pLista(list): Lista a modificar
    -pNum(int): Numero de copias por elemento
    Salidas:
    -lista(list): La lista modificada
    """
    lista = []
    for num in pLista:
        for i in range(pCopia):
            lista.append(num)
    return lista

def ESReplicar(pLista, pCopia):
    """
    Funcionalidad: Llama a replicar si la entrada es válida
    Entradas:
    -pLista(list): Lista a modificar
    -pNum(int): Numero de copias por elemento
    Salidas:
    -lista(list): La lista modificada
    """
    if validarReplicar(pLista, pCopia):
        return replicar(pLista, pCopia)
    else:
        return "La cantidad de copias debe ser un entero mayor que cero y pLista debe ser una lista"

#Reto 12
def validarUnion(pConjuntoA, pConjuntoB):
    """
    Funcionalidad: valida que dos conjuntos sean listas
    Entradas:
    -pConjuntoA(list): El primer conjunto
    -pConjuntoB(list): El segundo conjunto
    Salidas:
    -return(bool): True si ambos conjuntos son listas
    """
    return isinstance(pConjuntoA, list) and isinstance(pConjuntoB, list)

def union(pConjuntoA, pConjuntoB):
    """
    Funcionalidad: Crea la union de ambos conjuntos
    Entradas:
    -pConjuntoA(list): El primer conjunto
    -pConjuntoB(list): El segundo conjunto
    Salidas:
    -lista(list): La union de ambos conjuntos
    """
    lista = []
    for a in pConjuntoA:
        if a not in lista:
            lista.append(a)
        for b in pConjuntoB:
            if b not in lista:
                lista.append(b)
    return lista

def ESUnion(pConjuntoA, pConjuntoB):
    """
    Funcionalidad: Llama a union si la entrada es válida
    Entradas:
    -pConjuntoA(list): El primer conjunto
    -pConjuntoB(list): El segundo conjunto
    Salidas:
    -return(list): La union de ambos conjuntos
    """
    if validarUnion(pConjuntoA, pConjuntoB):
        return union(pConjuntoA, pConjuntoB)
    else:
        return "Se esperaba listas como conjuntos A y B"

#Reto 14
def validarMultiplicarLista(pConjuntoA, pConjuntoB):
    """
    Funcionalidad: valida que dos conjuntos sean listas
    Entradas:
    -pConjuntoA(list): El primer conjunto
    -pConjuntoB(list): El segundo conjunto
    Salidas:
    -return(bool): True si ambos conjuntos son listas
    """
    return isinstance(pConjuntoA, list) and isinstance(pConjuntoB, list)

def multiplicarLista(pConjuntoA, pConjuntoB):
    """
    Funcionalidad: Crea el producto de ambos conjuntos
    Entradas:
    -pConjuntoA(list): El primer conjunto
    -pConjuntoB(list): El segundo conjunto
    Salidas:
    -lista(list): El producto de ambos conjuntos
    """
    #return [[a,b] for a in pConjuntoA for b in pConjuntoB] 
    lista = []
    for a in pConjuntoA:
        for b in pConjuntoB:
            lista.append([a,b])
    return lista

def ESMultiplicarLista(pConjuntoA, pConjuntoB):
    """
    Funcionalidad: Llama a multiplicarLista si la entrada es válida
    Entradas:
    -pConjuntoA(list): El primer conjunto
    -pConjuntoB(list): El segundo conjunto
    Salidas:
    -return(list): El producto de ambos conjuntos
    """
    if validarMultiplicarLista(pConjuntoA, pConjuntoB):
        return multiplicarLista(pConjuntoA, pConjuntoB)
    else:
        return "Se esperaba listas como conjuntos A y B"

#Progama principal
print("Reto 2")
print("Entrada: [12,32,434,45,32,45], 45")
print("Salida: ")
print(ESBuscarElemento([12,32,434,45,32,45], 45))
print("")
print("Entrada: [12,32,434,45,'as',45], 45")
print("Salida: ")
print(ESBuscarElemento([12,32,434,45,"as",45], 45))
print("_______________________________________")

print("Reto 4")
print("Entrada: 5")
print("Salida: ")
print(ESListaRandom(5))
print("")
print("Entrada: 'asdf'")
print("Salida: ")
print(ESListaRandom("asdf"))
print("_______________________________________")

print("Reto 6")
print("Entrada: ['a', 'c', 'm', 'c', 'a']")
print("Salida: ")
print(ESEliminarRepetidos(["a", "c", "m", "c", "a"]))
print("")
print("Entrada: 12")
print("Salida: ")
print(ESEliminarRepetidos(12))
print("_______________________________________")

print("Reto 8")
print("Entrada: [1,2,3,4,6]")
print("Salida: ")
print(ESAlternada([1,2,3,4,6]))
print("")
print("Entrada: [1,2,3,4,5]")
print("Salida: ")
print(ESAlternada([1,2,3,4,5]))
print("")
print("Entrada: [1,2,3,4,'a']")
print("Salida: ")
print(ESAlternada([1,2,3,4,'a']))
print("_______________________________________")

print("Reto 10")
print("Entrada: [1,2,3,4], 2")
print("Salida: ")
print(ESReplicar([1,2,3,4], 2))
print("")
print("Entrada: [1,2,3,4], -1")
print("Salida: ")
print(ESReplicar([1,2,3,4], -1))
print("_______________________________________")

print("Reto 12")
print("Entrada: [1,2,3,4], [4,5,6,7]")
print("Salida: ")
print(ESUnion([1,2,3,4], [4,5,6,7]))
print("")
print("Entrada: [1,2,3,4], 1")
print("Salida: ")
print(ESUnion([1,2,3,4], 1))
print("_______________________________________")

print("Reto 14")
print("Entrada: [1,2,3,4], [4,5,6,7]")
print("Salida: ")
print(ESMultiplicarLista([1,2,3,4], [4,5,6,7]))
print("")
print("Entrada: [1,2,3,4], 1")
print("Salida: ")
print(ESMultiplicarLista([1,2,3,4], 1))

#print(multiplicarLista([1,2,3,4], [4,5,6,7]))