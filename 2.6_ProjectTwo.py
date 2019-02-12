# Gordon Portzline and Zhengyu Wu
# CSIS-2430-402-Sp19

from collections import Counter

A = Counter(['a', 'a', 'a', 'b', 'b', 'c'])

B = Counter(['a', 'a', 'b', 'b', 'b', 'd', 'd', 'd', 'd'])

# A U B
aub = A | B

print('A is:        ', sorted(A.items()))
print('B is:        ', sorted(B.items()))
print('A union B is:', sorted(aub.items()))
print()

# A intersection B
aib = A & B

print('A is:               ', sorted(A.items()))
print('B is:               ', sorted(B.items()))
print('A intersection B is:', sorted(aib.items()))
print()

# A - B
adb = A - B

print('A is:    ', sorted(A.items()))
print('B is:    ', sorted(B.items()))
print('A - B is:', sorted(adb.items()))
print()

# A + B
asb = A + B

print('A is:    ', sorted(A.items()))
print('B is:    ', sorted(B.items()))
print('A + B is:', sorted(asb.items()))
