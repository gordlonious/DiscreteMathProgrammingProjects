def mergeSortCompare(l):

    comparisonCount = [0]

    def mergeSort(alist, cc):

        if len(alist)>1:

            mid = len(alist)//2

            lefthalf = alist[:mid]

            righthalf = alist[mid:]

            mergeSort(lefthalf, cc)

            mergeSort(righthalf, cc)

            (i,j,k) = (0,0,0)

            while i < len(lefthalf) and j < len(righthalf):

                # There could be two comparisons here
                cc[0] += 2

                if lefthalf[i] < righthalf[j]:

                    cc[0] += 1

                    alist[k]=lefthalf[i]

                    i=i+1

                else:

                    alist[k]=righthalf[j]

                    j=j+1

                k=k+1

            while i < len(lefthalf):

                cc[0] += 1

                alist[k]=lefthalf[i]

                i=i+1

                k=k+1

            while j < len(righthalf):

                cc[0] += 1

                alist[k]=righthalf[j]

                j=j+1

                k=k+1

    print("Executing MERGESORT and counting comparison operations...")            

    mergeSort(l, comparisonCount) # sort the list

    return comparisonCount[0]

alist = [54,26,93,17,77,31,44,55,20]

comparisonCount = mergeSortCompare(alist)

print("The number of items compared by mergesort was: {0}".format(comparisonCount))
