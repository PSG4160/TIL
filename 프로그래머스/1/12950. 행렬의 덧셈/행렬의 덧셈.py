import numpy as np

def solution(A,B):
    A_np = np.array(A)
    B_np = np.array(B)
    result = A_np + B_np
    return result.tolist()
    # return [[c + d for c, d in zip(a, b)] for a, b, in zip(A, B)]
