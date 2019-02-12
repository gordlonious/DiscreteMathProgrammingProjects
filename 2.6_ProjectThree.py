from collections import Counter

# famous people
A = Counter({'Alice': 0.6, 'Brian': 0.9, 'Fred': 0.4, 'Oscar': 0.1, 'Rita': 0.5})

# rich people
B = Counter({'Alice': 0.4, 'Brian': 0.8, 'Fred': 0.2, 'Oscar': 0.9, 'Rita': 0.7})

# to support the fuzzy set complement operation we must subtract from an identical set whose elements are all of degree 1
complementSupport = Counter({'Alice': 1, 'Brian': 1, 'Fred': 1, 'Oscar': 1, 'Rita': 1})

# complement of A
ac = complementSupport - A
ac['Brian'] = round(1 - A['Brian'], 1) # since Counter is doing floating point arithmetic

print('A is:             ', sorted(A.items()))
print ('A complement is:  ', sorted(ac.items()))
print()

# A U B
aub = A | B

print('A is:    ', sorted(A.items()))
print('B is:    ', sorted(B.items()))
print('A U B is:', sorted(aub.items()))
print()

# A intersection B
aib = A & B

print('A is:                 ', sorted(A.items()))
print('B is:                 ', sorted(B.items()))
print ('A intersection B is:  ', sorted(aib.items()))
