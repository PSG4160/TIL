def solution(n, m):
    a = n
    b = m
    while m != 0:
        n, m = m, n % m
    
    gcd_value = n  # 최대공약수
    lcm_value = (a * b) // gcd_value  # 최소공배수 계산

    return [gcd_value, lcm_value]    
