
class Part4Data:

    def __init__(self, comparisonData, name):
        
        self.Data = comparisonData

        self.Data.Name = name

    def PrintTenBest(self):

        tenBest = self.Data.GetTenBest()

        print("{0} 10 best:".format(self.Data.Name))
        
        for x in tenBest:

            print("    N={0}, ComparisonCount={1}, Permutation={2}".format(x[0], x[1], x[2]))
