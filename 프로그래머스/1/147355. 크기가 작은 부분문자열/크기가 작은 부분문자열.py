
def solution(t, p):
    k = len(p)
    j = 0
    answer = 0
    while j + k <= len(t):  # while 조건 수정
        t_p = ""  # for문이 실행될 때마다 초기화
        for i in range(j, j + k):
            t_p += t[i]
        if int(t_p) <= int(p):
            answer += 1
        j += 1  # j 값 증가
    return answer  # while 루프 밖에서 반환

        
        
        