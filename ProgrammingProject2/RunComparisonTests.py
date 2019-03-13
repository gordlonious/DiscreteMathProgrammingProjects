import unittest
import runcomparisons
from mergesort import mergeSortCompare

class RunComparisonTests(unittest.TestCase):

    def test_print_mergesortcomparisondata(self):
       
       data = runcomparisons.RunComparisons(mergeSortCompare)

       for x in data:
           print(x)

if __name__ == '__main__':
    unittest.main()
