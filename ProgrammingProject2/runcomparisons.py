# Discrete Mathematics
# CSIS Programming Project 2
# Gordon Portzline
# Zhengyu Wu
# Brad Rohbock

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
def RunComparisons4(sort):
    ncomparperm = ComparisonData()

    for p in permutations(range(4)):
        ncomparperm.AddData(4, sort(list(p)), p)


    return ncomparperm

def RunComparisons6(sort):
    ncomparperm = ComparisonData()

    for p in permutations(range(6)):
        ncomparperm.AddData(6, sort(list(p)), p)

    return ncomparperm

def RunComparisons8(sort):
    ncomparperm = ComparisonData()

    for p in permutations(range(8)):
        ncomparperm.AddData(8, sort(list(p)), p)

    return ncomparperm
# the below code should use all sorting algorithms and data to answer part 4


mergeSortData4 = Part4Data(RunComparisons4(mergeSortCompare), "mergesort")
heapSortData4 = Part4Data(RunComparisons4(heapsort_Kevin.heapSort), "heapsort")
quickSortData4 = Part4Data(RunComparisons4(quicksort.quicksort), "quicksort")

CallAllPrintMethods(mergeSortData4)
CallAllPrintMethods(heapSortData4)
CallAllPrintMethods(quickSortData4)

mergeSortData6 = Part4Data(RunComparisons6(mergeSortCompare), "mergesort")
heapSortData6 = Part4Data(RunComparisons6(heapsort_Kevin.heapSort), "heapsort")
quickSortData6 = Part4Data(RunComparisons6(quicksort.quicksort), "quicksort")

CallAllPrintMethods(mergeSortData6)
CallAllPrintMethods(heapSortData6)
CallAllPrintMethods(quickSortData6)

mergeSortData8 = Part4Data(RunComparisons8(mergeSortCompare), "mergesort")
heapSortData8 = Part4Data(RunComparisons8(heapsort_Kevin.heapSort), "heapsort")
quickSortData8 = Part4Data(RunComparisons8(quicksort.quicksort), "quicksort")

CallAllPrintMethods(mergeSortData8)
CallAllPrintMethods(heapSortData8)
CallAllPrintMethods(quickSortData8)