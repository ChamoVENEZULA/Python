def main():
    data = [11,99,20,40, 32,1,12,45,18,75,4,13]
    print(f"Estado inicial: {data}")
    mergeSort(data)
    print(f"Estado final {data}")


def mergeSort(array):
    if len(array) > 1:
        mitad = len(array)//2
        izq = array[:mitad]
        der = array[mitad:]
        mergeSort(izq)
        mergeSort(der)

        indice = sub1 = sub2 = 0
        while indice < len(izq) and sub1 < len (der):
            if izq[indice] < der[sub1]:
                array[sub2] = izq[indice]
                indice += 1
            else:
                array[sub2] = der[sub1]
                sub1 += 1
            sub2 += 1
        
        while indice < len(izq):
            array[sub2] = izq[indice]
            indice += 1
            sub2 += 1
        
        while sub1 < len(der):
            array[sub2] = der[sub1]
            sub1 += 1
            sub2 += 1

main()