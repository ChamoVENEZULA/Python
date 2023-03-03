def main():
    data = [11,99,20,40, 32,1,12,45,18,75,4,13]
    print(f"Estado inicial: {data}")

    for indice in range(1,len(data)):
        valor = data[indice]
        pivote = indice -1
        while pivote >= 0 and data[pivote] > valor:
            swap(data, pivote, pivote+1) # data[pivote+1] = data[pivote]
            pivote = pivote - 1
        data[pivote+1] = valor
    print(f"Estado final {data}")

def swap(lista:list, posOrigen: int, posDestino: int):
    temp = lista[posDestino]
    lista[posDestino] = lista[posOrigen]
    lista[posOrigen] = temp

main()