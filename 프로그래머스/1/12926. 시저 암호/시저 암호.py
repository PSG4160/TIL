def solution(s, n):
    answer = ""
    for char in s:
    # 소문자 'a'에서 'z'까지 순환하며 이동
        if 'a' <= char <= 'z':
            answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
     # 대문자 'A'에서 'Z'까지 순환하며 이동
        elif 'A' <= char <= 'Z':
            answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += char  # 알파벳이 아닌 경우 그대로 반환
    return answer

