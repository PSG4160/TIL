a, b = map(int, input().strip().split(' '))
answer = ''
for i in range(b):
    answer += '*' * a + '\n'  # 각 줄마다 `*`을 `a`만큼 찍고 줄바꿈 추가
print(answer)
