def solution(strings, n): # 인덱스 n에 해당하는 문자를 맨 앞으로 보내고, 오름차순 정렬 후 삭제하기.
    answer = []
    for i in strings:
        answer.append(i[n] + i)
    answer.sort()

    return [j[1:] for j in answer]