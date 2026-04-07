#Сортировка пузырьком
def BubbleSort(arr):
    isSorted = False
    while(not isSorted):
        isSorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False
    return arr



#Сортировка вставками
def InsertSort(arr):
    for i in range(1, len(arr)):
        el = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] >= el:
                arr[j + 1] = arr[j]
                arr[j] = el
            else:
                arr[j + 1] = el
                break
    
    return arr

#Сортировка выбором
def SelectionSort(arr):
    print(arr)
    lo = 0
    hi = len(arr)
    while(hi > lo):
        print(arr[lo:hi])
        maxid = arr.index(max(arr[lo: hi]), lo, hi)
        minid = arr.index(min(arr[lo: hi]), lo, hi)
        arr[hi-1], arr[maxid] = arr[maxid], arr[hi-1]
        arr[lo], arr[minid] = arr[minid], arr[lo]
        print(arr[lo], arr[minid])
        hi -= 1
        lo += 1
        print(arr)
        
    return arr

#Слияние
def merge(left, right):
    i = 0
    j = 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

#Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

#Быстрая сортировка
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    el = arr[0]
    left = [x for x in arr if x < el]
    middle = [x for x in arr if x == el]
    rigth = [x for x in arr if x > el]
    return quicksort(left) + middle + quicksort(rigth)

array = [3, 5, 20, 6, 1, 8, 2, 4, 11]

print(BubbleSort(array))

