def solution(n):
    answer = []
    for i in list(str(n)):
        answer.insert(0,int(i))
    return answer