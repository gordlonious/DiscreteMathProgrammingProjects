
class Part4Data:

    def __init__(self, comparisonData, name):
        
        self.Data = comparisonData

        self.Data.Name = name

    def PrintTenBest(self):

        tenBest = self.Data.GetTenBest()

        print("{0} 10 best:".format(self.Data.Name))
        
        for x in tenBest:

            print("    N={0}, ComparisonCount={1}, Permutation={2}".format(x[0], x[1], x[2]))

    def PrintTenWorst(self):

        tenWorst = self.Data.GetTenWorst()

        print("{0} 10 worst:".format(self.Data.Name))
        
        for x in tenWorst:

            print("    N={0}, ComparisonCount={1}, Permutation={2}".format(x[0], x[1], x[2]))

    def PrintNClassAverages(self):

        averages = []

        averages.append((4, self.Data.GetNClassAverage(4)))

        averages.append((6, self.Data.GetNClassAverage(6)))

        averages.append((8, self.Data.GetNClassAverage(8)))

        print("Averages for {0}".format(self.Data.Name))

        for x in averages:

            print("    N={0}, Average={1}".format(x[0], x[1]))

        
