#Discrete Mathematics
#CSIS Programming Project 2
#Gordon Portzline
#Zhengyu Wu
#Brad Rohobck 

import MergeSortTests

# here 'all' is referring to n=4, n=6, and n=8 for the given sort function
# param: comparisonFunc | should run a sort algorithm that returns an integer representing the number of comparisons made during the sort
def RunAllComparisons(comparisonFunc):

    comparisons = []

    comparisons.append(comparisonFunc(4))

    comparisons.append(comparisonFunc(6))

    comparisons.append(comparisonFunc(8))

    return comparisons

# this is basically 'main', just execute it by passing the script name to the python interpreter
mergeSortComparisons = RunAllComparisons(MergeSortTests.RunComparison)

print("Running MERGESORT comparisons...")
print()
for i,x in enumerate(mergeSortComparisons):

    if(i == 0):
        print("  with {0} items: {1}".format(4, x))

    elif (i == 1):
        print("  with {0} items: {1}".format(6, x))

    elif (i == 2):
        print("  with {0} items: {1}".format(8, x))

    else:
        raise Exception()

