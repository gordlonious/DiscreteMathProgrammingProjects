#Discrete Mathematics
#CSIS Programming Project 2
#Gordon Portzline
#Zhengyu Wu
#Brad Rohbock 

from functools import reduce
from itertools import permutations
from mergesort import mergeSortCompare

# PARAM sort: must give this function a sort function that returns a comparison count
# RETURNS: a list of pairs where (x,y) = (n,comparisonCount)
#### the list will return one n!/(n-r)! pairs for n=4, n=6, and n=8, giving you a length of 4! + 6! + 8!
def RunComparisons(sort):
    
    ncountpairs = []
    
    for p in permutations(range(4)):
        ncountpairs.append([4, sort(list(p)), p])

    for p in permutations(range(6)):
        ncountpairs.append([4, sort(list(p)), p])

    for p in permutations(range(8)):
        ncountpairs.append([4, sort(list(p)), p])

    return ncountpairs

# PARAM: data | the comparison data in the form [(n, comparisonCount)]
# PARAM: n | the class of comparison you would like the wors case of (i.e 4, 6, 8)
def GetWorstCaseComparison(n, data):
    
    nonly = list(filter(lambda x: x[0] == n, data))

    justcomparisons = []

    for x in nonly:
        justcomparisons.append(x[1])

    return max(justcomparisons)

# main script..

mergeSortData = RunComparisons(mergeSortCompare)

print(GetWorstCaseComparison(4, mergeSortData))
