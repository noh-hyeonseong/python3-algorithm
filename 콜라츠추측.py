def solution(num):
    answer = 0
    while num != 1 and answer < 500:
        num = collatz(num)
        answer += 1
        if num != 1 and answer == 500:
            answer = -1
            break
    return answer

def collatz(n):
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    return int(n)