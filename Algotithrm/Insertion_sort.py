

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


lista = [11, 13, 5, 12, 9]

insertion_sort(lista)
print("Lista Ordenanda", lista)
