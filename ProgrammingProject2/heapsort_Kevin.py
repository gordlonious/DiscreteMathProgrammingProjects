import math
# Python function to print permutations of a given list
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
  # Driver program to test above function 
data1 = list('0123') 
data2 = list('012345') 
data3 = list('01234567') 

#HeapSort Algorithm
def heapify(arr, n, i):
    count = 0
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        count += 1
        arr[i],arr[largest] = arr[largest],arr[i]
        count += heapify(arr, n, largest)
    return count
 
def heapSort(arr):
    n = len(arr)
    count = 0
    for i in range(n, -1, -1):
        heapify(arr, n, i)  
        count += heapify(arr, i, 0)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        count += heapify(arr, i, 0)
 
    return count


if __name__ == '__main__':

        comparisons = []
        totalcomparisons = 0
        for p in permutation(data3):
            arr = p
        
            comparisons.append(heapSort(arr))
#print(comparisons)
        comparisons.sort(reverse = True)
        print('Worst 10: ')
        print(comparisons[:10])
        comparisons.sort()
        print('Best 10: ')
        print(comparisons[:10])
        totalcomparisons = sum(comparisons)
        print('Average = ' + str(totalcomparisons/math.factorial(8)))

