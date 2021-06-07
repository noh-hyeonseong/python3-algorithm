def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer = answer + countAck(i)*i
    return answer

def countAck(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
    if count % 2 == 0:
        ackNum = 1
    else:
        ackNum = -1
    return ackNum