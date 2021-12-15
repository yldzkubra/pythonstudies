def selectionSort(list):
    for k in range(len(list)):
        min_idx = k
        for i in range(k + 1, len(list)):
            if list[i] < list[min_idx]:
                min_idx = i  
        (list[k], list[min_idx]) = (list[min_idx], list[k])

def boubleSort(list):
    for k in range(len(list)):
        for i in range(k+1,len(list)-k):
            if list[k]>list[i]:
                list[k],list[i]=list[i],list[k]

def insertionSort(list):
     for k in range(1,len(list)):
      key=list[k]
      j=k-1
      while j>=0 and key<list[j]:
        list[j + 1] = list[j]
        j = j - 1
        list[j + 1] = key



liste = [5,9,2,4,13,16]
print(selectionSort(liste))
print(boubleSort(liste))
print(insertionSort(liste))