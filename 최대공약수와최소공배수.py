def solution(n, m):
    """
    유클리드 호제법으로 풀면 좋다.
    최대 공약수는 x,y의 최대 공약수는 x%y 와 y의 최대공약수와 같다.
    x    y    x%y
    10 % 12 -> 10
    12 % 10 -> 2
    10 % 2  -> 0    >>>> 나머지의 값이 "0"일 때의 y값(2) 가 최대 공약수
    최소공배수 = x * y / 최대공약수
    """
    #유클리드 호제법
    answer = [1,m]
    a, b = n, m
    while a % b:
        temp = a % b
        a = b
        b = temp
    answer = [b, n * m / b]
    return answer

    # 기존 날코딩
    # answer = [1, 1]
    # minNum = min(n, m)
    # maxNum = max(n, m)
    # if minNum == 1:
    #     answer = [1, maxNum]
    # else:
    #     for i in range(2, minNum+1):
    #         if n % i == 0 and m % i == 0:
    #             answer[0] = i
    #     if maxNum % minNum == 0:
    #         answer[1] = maxNum
    #     else:
    #         answer[1] = answer[0] * (n/answer[0]) * (m/answer[0])
    # return answer