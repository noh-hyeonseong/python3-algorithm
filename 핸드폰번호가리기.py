def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number)-4):
        answer += '*'
    answer += phone_number[-4:]
    print(answer)
    return answer