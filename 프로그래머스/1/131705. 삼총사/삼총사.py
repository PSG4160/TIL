from itertools import combinations
def solution(number):
    zero_sum_count = sum(1 for triplet in combinations(number, 3) if sum(triplet) == 0)
    return zero_sum_count