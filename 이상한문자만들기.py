def solution(s):
    answer = ''
    temp = s.split(' ')
    for i in temp:
        for idx,j in enumerate(i):
            if idx % 2:
                answer += j.lower()
            else:
                answer += j.upper()
        answer += ' '
    answer = answer[:-1]
    return answer