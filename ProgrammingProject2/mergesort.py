#Discrete Mathematics
#CSIS Programming Project 2
#Gordon Portzline
#Zhengyu Wu
#Brad Rohobck 

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

    mergeSort(l, comparisonCount) # sort the list

    return comparisonCount[0]

