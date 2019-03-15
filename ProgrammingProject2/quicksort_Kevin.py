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


def _partition(mylist, start, end):
    count = 0
    pos = start
    for i in range(start, end):
        count += 1
        if mylist[i] < mylist[end]:
            mylist[i], mylist[pos] = mylist[pos], mylist[i]
            pos += 1
    mylist[pos], mylist[end] = mylist[end], mylist[pos]
    return pos, count

def _quicksort(mylist, start, end):
    count = 0
    if start < end:
        pos, count = _partition(mylist, start, end)        
        count += _quicksort(mylist, start, pos - 1)
        count += _quicksort(mylist, pos + 1, end)
    return count

def quicksort(mylist, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(mylist) - 1
    return _quicksort(mylist, start, end)

if __name__ == '__main__':
    comparisons = []
    totalcomparisons = 0
    for p in permutation(data3):
        arr = p
    
        comparisons.append(quicksort(arr))
    print(comparisons)
    comparisons.sort(reverse = True)
    print(comparisons[:10])
    comparisons.sort()
    print(comparisons[:10])
    totalcomparisons = sum(comparisons)
    print('Average = ' + str(totalcomparisons/math.factorial(8)))
