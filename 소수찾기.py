def solution(n):

    answer = 0
    for j in range(2,n+1):
        temp = 0
        for i in range(2,int(j**0.5)+1):
            if j % i == 0:
                temp = 1
                break
        if temp == 0:
            answer += 1
    print(answer)
    return answer