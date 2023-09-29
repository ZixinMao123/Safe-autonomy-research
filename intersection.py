from z3 import *

def is_intersection_nonempty(H_A, b_A, H_B, b_B):

    m = len(H_A[0])
    
    x = [Real(f'x_{i}') for i in range(m)]

    s = Solver()

    for i in range(len(H_A)):
        s.add(Sum([H_A[i][j] * x[j] for j in range(m)]) <= b_A[i])

    for i in range(len(H_B)):
        s.add(Sum([H_B[i][j] * x[j] for j in range(m)]) <= b_B[i])

    if s.check() == sat:
        return True
    else:
        return False

#true case:
# H_A = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# b_A = [0, 1, 0, 1]
# H_B = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# b_B = [0, 2, 1, 3]

# false case:
H_A = [[-1, 0], [1, 0], [0, -1], [0, 1]]
b_A = [0, 3, 0, 3] 
H_B = [[-1, 0], [1, 0], [0, -1], [0, 1]]
b_B = [-4, -1, -4, -1]

print(is_intersection_nonempty(H_A, b_A, H_B, b_B))