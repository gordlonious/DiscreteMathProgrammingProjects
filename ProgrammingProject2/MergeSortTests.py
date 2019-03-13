#Discrete Mathematics
#CSIS Programming Project 2
#Gordon Portzline
#Zhengyu Wu
#Brad Rohbock 

import unittest
from mergesort import mergeSortCompare
import random

class MergeSortTests(unittest.TestCase):

    def test_mergesort_sortsarray_ascending(self):
        
        alist = [54,26,93,17,77,31,44,55,20]

        comparisonCount = mergeSortCompare(alist)

        self.assertEqual([17, 20, 26, 31, 44, 54, 55, 77, 93], alist)
        

if __name__ == '__main__':
    unittest.main()
