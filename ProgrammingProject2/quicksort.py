#Discrete Mathematics
#CSIS Programming Project 2
#Gordon Portzline
#Zhengyu Wu
#Brad Rohbock 

#QuickSort pulled from online repository 
# """https://gist.github.com/anirudhjayaraman/897ca0d97a249180a48b50d62c87f239"""


def quicksort(lista):

    def _quicksort(lista,start,end):
       i = start
       j = end
       pivot = lista[(start + end)//2]

       comparison_count = 0
       while i <= j:
          while lista[i] < pivot:
             comparison_count += 1;
             i += 1
          while pivot < lista[j]:
             comparison_count += 1;
             j -= 1
          if i <= j:
             aux = lista[i]
             lista[i] = lista[j]
             lista[j] = aux
             comparison_count += 1
             i += 1
             j -= 1

       if start < j:
          comparison_count += _quicksort(lista, start, j)
       if i < end:
          comparison_count += _quicksort(lista, i, end)

       return comparison_count

    return _quicksort(lista, 0, len(lista)-1)

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print(alist)
    count = quicksort(alist)
    print("Comparisons: ", count)
    print(alist)

