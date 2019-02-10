import numpy as np

def NumpyBoolArrayToString(nba):
    
    s = ''
    
    for b in nba:
        if(b):
            s += '1'
        else:
            s += '0'
            
    return s

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
