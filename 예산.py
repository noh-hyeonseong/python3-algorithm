def solution(d, budget):
    answer = 0
    d.sort()
    temp = 0
    for i in d:
        if budget >= (temp + i):
            temp = temp + i
            answer = answer + 1
    print("answer : ",answer)
    return answer