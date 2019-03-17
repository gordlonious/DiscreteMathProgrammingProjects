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
from ComparisonData import ComparisonData
import math
from Part4Data import Part4Data
from CallPrintMethods import CallAllPrintMethods

# PARAM sort: must give this function a sort function that returns a comparison count
# RETURNS: a ComparisonData object 
#### the Data member should have n!/(n-r)! items for n=4, n=6, and n=8, giving you a length of 4! + 6! + 8!
def RunComparisons(sort):
    
    ncomparperm = ComparisonData()
    
    for p in permutations(range(4)):
        ncomparperm.AddData(4, sort(list(p)), p)

    for p in permutations(range(6)):
        ncomparperm.AddData(6, sort(list(p)), p)

    for p in permutations(range(8)):
        ncomparperm.AddData(8, sort(list(p)), p)

    return ncomparperm


# the below code should use all sorting algorithms and data to answer part 4 

mergeSortData = Part4Data(RunComparisons(mergeSortCompare), "mergesort")
heapSortData = Part4Data(RunComparisons(heapsort_Kevin.heapSort), "heapsort")
quickSortData = Part4Data(RunComparisons(quicksort.quicksort), "quicksort")

CallAllPrintMethods(mergeSortData)
CallAllPrintMethods(heapSortData)
CallAllPrintMethods(quickSortData)
