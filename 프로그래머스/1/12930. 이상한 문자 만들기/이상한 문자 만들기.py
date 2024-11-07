# def solution(s):
#     words = s.split()
#     # 각 단어에 대해 홀수 인덱스 위치의 문자만 대문자로 변환
#     transformed_words = [''.join([char.upper() if index % 2 == 0 else char.lower()
#                                   for index, char in enumerate(word)]) 
#                          for word in words]
#     # 공백을 넣어 문자열로 다시 합치기
#     return ' '.join(transformed_words)

def solution(s):
    words = s.split(' ')  # 공백을 기준으로 문자열을 단어로 나눕니다.
    transformed_words = []
    
    for word in words:
        transformed_word = ''.join(
            char.upper() if index % 2 == 0 else char.lower()
            for index, char in enumerate(word)
        )
        transformed_words.append(transformed_word)
    
    return ' '.join(transformed_words)  # 변환된 단어들을 공백으로 연결하여 반환합니다.


