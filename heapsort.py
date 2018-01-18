def heapSort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0)
    return(array)

def heapify(array, n, i):
    largest = i  
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and array[largest] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # swap
        heapify(array, n, largest)

lista=[2,3,1,5,4]
print(heapSort(lista))