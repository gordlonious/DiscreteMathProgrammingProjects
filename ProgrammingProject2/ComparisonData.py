from typing import Iterable

class ComparisonData:

    def __init__(self):

        self.Data = []

        self.Name = "Give this data a name!"

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

    def GetNClassWorstTenComparisons(self, n):
        
        return sorted(self.GetNClassComparisons(n))[-10:]

    def GetNClassTenBestComparisons(self, n):

        return sorted(self.GetNClassComparisons(n))[0:9]

    def GetNClassAverage(self, n):

        return sum(self.GetNClassComparisons(n))/math.factorial(n)

    def GetTenBest(self):

        tenBest = []

        sortedByComparisons = sorted(self.Data, key=lambda x: x[1])

        return sortedByComparisons[0:9]

if __name__ == '__main__':

    cd = ComparisonData()

    cd.AddData(4, 16, [0,1,4,3])
    cd.AddData(4, 12, [1,0,4,3])

    print('should print [16, 12]:')
    print(cd.GetNClassComparisons(4))
