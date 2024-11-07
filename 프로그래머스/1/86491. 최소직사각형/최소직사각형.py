def solution(sizes):
    max_value = max(max(row) for row in sizes)
    next_value = max(min(row) for row in sizes)

    return max_value * next_value




# 가로 세로 길이중 가장 길이가 큰 값 하나, 두 값 중 하나를 제외한 값이 가장 큰 값의 곱을 구하면 된다.