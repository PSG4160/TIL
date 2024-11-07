def solution(n):
    answer = "" 
    while n > 0: # n을 3으로 나눴을 때 몫이 0일때 까지
        answer += str(n % 3) # n을 3으로 나눴을 때 나머지
        n //= 3
        
        
    

    return int(answer,3)