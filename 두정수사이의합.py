def solution(a, b):
    answer = 0
    for i in range(a,b+1):
        answer += i
    print(answer)
    return answer