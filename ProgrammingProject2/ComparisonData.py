from typing import Iterable

class ComparisonData:

    def __init__(self):

        self.Data = []

    def AddData(self, n: int, comparisonCount: int, permutation: Iterable[int]):
        
        self.Data.append([n, comparisonCount, permutation])

    def GetData(self):

        return self.Data

    def GetNClassData(self, n):

        return list(filter(lambda x: x[0] == n, self.Data))
       
    def GetPermutation(p: Iterable[int]):

        return list(filter(lambda x: x[2] == p), self.Data)

    def GetNClassComparisons(self, n):

        return list(map(lambda x: x[1], list(filter(lambda x: x[0] == n, self.Data))))

    def GetComparisons(self):

        return self.Data[1]

if __name__ == '__main__':

    cd = ComparisonData()

    cd.AddData(4, 16, [0,1,4,3])
    cd.AddData(4, 12, [1,0,4,3])

    print('should print [16, 12]:')
    print(cd.GetNClassComparisons(4))
