lista = [10,302,3,19,11,38,29,45, 78,1]

def main():
    print(lista)
    bubbleSort(lista)
    print(lista)

def bubbleSort(lista: list):
    tamannio = len(lista)
    for posicion in range(tamannio):
        for lookahead in range(0, 
        tamannio - posicion - 1):
            if lista[lookahead] > lista[lookahead+1]:
                swap(lista, lookahead, lookahead+1)
                ordenado = False;
        if ordenado: 
            break
    

def swap(lista:list, posOrigen: int, posDestino: int):
    temp = lista[posDestino]
    lista[posDestino] = lista[posOrigen]
    lista[posOrigen] = temp

main()
