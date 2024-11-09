def solution(array, commands):
    answer = []
    
    for i in commands:
        k = sorted(array[i[0]-1:i[1]])
        answer.append(k[i[2]-1])
    return answer