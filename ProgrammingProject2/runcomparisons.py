#Discrete Mathematics
#CSIS Programming Project 2
#Gordon Portzline
#Zhengyu Wu
#Brad Rohbock 

import quicksort
import heapsort_Kevin
import quicksort_Kevin
from itertools import permutations
from mergesort import mergeSortCompare

# PARAM sort: must give this function a sort function that returns a comparison count
# RETURNS: a list of pairs where (x,y,z) = (n,comparisonCount,permutation)
#### the list will return one n!/(n-r)! pairs for n=4, n=6, and n=8, giving you a length of 4! + 6! + 8!
def RunComparisons(sort):
    
    ncomparperm = []
    
    for p in permutations(range(4)):
        ncomparperm.append([4, sort(list(p)), p])

    for p in permutations(range(6)):
        ncomparperm.append([6, sort(list(p)), p])

    for p in permutations(range(8)):
        ncomparperm.append([8, sort(list(p)), p])

    return ncomparperm

# PARAM: data | the comparison data in the form [(n, comparisonCount)]
# PARAM: n | the class of comparison you would like the wors case of (i.e 4, 6, 8)
# PARAM: data | a list in the form [n, comparison count for a permutation ran through the sort, the permutation]
def GetWorstCaseComparison(n, data):
    
    nonly = list(filter(lambda x: x[0] == n, data))

    justcomparisons = []

    for x in nonly:
        justcomparisons.append(x[1])

    return max(justcomparisons)

# PARAM: data | the comparison data in the form [(n, comparisonCount)]
# PARAM: n | the class of comparison you would like the wors case of (i.e 4, 6, 8)
# PARAM: data | a list in the form [n, comparison count for a permutation ran through the sort, the permutation]
def GetTenBest(n, data):

    nonly = list(filter(lambda x: x[0] == n, data))

    justcomparisons = []

    for x in nonly:
        justcomparisons.append(x[1])

    tenbest = []

    for i in range(10):
        tenbest.append(justcomparisons[i])

    return tenbest
    

# the below code should use all sorting algorithms and data to answer part 4 

mergeSortData = RunComparisons(mergeSortCompare)
heapSortData = RunComparisons(heapsort_Kevin.heapSort)
quickSortData = RunComparisons(quicksort.quicksort)
quickSortData_Kevin = RunComparisons(quicksort_Kevin.quicksort)

print('mergesort worst case for n=4:')
print(GetWorstCaseComparison(4, mergeSortData))

#print('mergesort ten best cases for n=8')
#print(GetTenBest(8, mergeSortData))

print('heapsort worst case for n=8')
print(GetWorstCaseComparison(8, heapSortData))

print('Brad\'s quicksort worst case for n=8')
print(GetWorstCaseComparison(8, quickSortData))

print('Kevin\'s quicksort worse case for n=8')
print(GetWorstCaseComparison(8, quickSortData_Kevin))
