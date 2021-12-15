def combine(left, right):
    orderedList = []
    i = k = 0
    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            orderedList.append(left[i])
            i += 1
        else:
            orderedList.append(right[k])
            k += 1
    orderedList += left[i:]
    orderedList += right[k:]
    return orderedList

def mergeSort(unorderedlist):
    if len(unorderedlist) < 2:
          return unorderedlist
    b = int(len(unorderedlist) / 2)
    return combine(mergeSort(unorderedlist[:b]), mergeSort(unorderedlist[b:]))



def partition(arr,low,high): 
	i = ( low-1 )		 
	pivot = arr[high]	 

	for j in range(low , high): 

		 
		if arr[j] < pivot: 
		
			
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

def quickSort(arr,low,high): 
	if low < high:
		pi = partition(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i])
