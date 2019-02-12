# Gordon Portzline and Zhengyu Wu
# CSIS-2430-402-Sp19

import numpy as np

def NumpyBoolArrayToString(nba):
    
    s = ''
    
    for b in nba:
        if(b):
            s += '1'
        else:
            s += '0'
            
    return s

def CsubsetToBitString(s, c):

    str = ''

    for i in range(0, len(c)):
        if c[i] in s:
            str += '1'
        else:
            str += '0'

    return str

# arbitrary set with n elements
C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# numbers in c that are evenly divisible by 3
A = [3, 6, 9, 12]

# bit string representation(s) of A
Astring = '0010010010010'
Abits = np.array([0,0,1,0,0,1,0,0,1,0,0,1,0], dtype=np.bool)

# prime numbers in C
B = [1, 2, 3, 5, 7, 11, 13]

# bit string representation(s) of B
Bstring = '1110101000101'
Bbits = np.array([1,1,1,0,1,0,1,0,0,0,1,0,1], dtype=np.bool)

# calculate bit string representation of A complement
print('A is:           ', Astring)

print('A complement is:', NumpyBoolArrayToString(~Abits))

print() # print new line

# A U B
aub = np.union1d(A, B)

print('A =    ', Astring)
print('B =    ', Bstring)

print('A U B =', CsubsetToBitString(aub, C))

print()

# A intersection B
aib = np.intersect1d(A, B)

print('A =            ', Astring)
print('B =            ', Bstring)

print('A intersect B =', CsubsetToBitString(aib, C))

print()

# A - B
adb = np.setdiff1d(A, B, True)

print('A =             ', Astring)
print('B =             ', Bstring)

print('A difference B =', CsubsetToBitString(adb, C))

print()

# A symmetric difference B
asdb = set(A).symmetric_difference(set(B))

print('A =                       ', Astring)
print('B =                       ', Bstring)

print('A symmetric difference B =', CsubsetToBitString(asdb, C))
