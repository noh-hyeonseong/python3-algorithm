def solution(x, n):
    answer = []
    plusNum = x
    for i in range(0,n):
        answer.append(x)
        x += plusNum
    return answer