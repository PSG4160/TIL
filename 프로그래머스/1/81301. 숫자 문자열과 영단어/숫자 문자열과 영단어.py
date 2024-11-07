def solution(s):
    k = ""
    answer = ""
    alp = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in s:
        if i in alp.values():
            answer += i
        else:
            k += i
            if k in alp:
                answer += alp[k]
                k = ""
            
                
    return int(answer) # 나중에 int 붙이자
        

    
