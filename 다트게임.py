def solution(dartResult):
    answer = 0
    score = []
    for idx, i in enumerate(dartResult):
        if i == 'S':
            pass
        elif i == 'D':
            score[-1] = score[-1] ** 2
        elif i == 'T':
            score[-1] = score[-1] ** 3
        elif i == '*':
            if len(score) == 1:
                score[-1] = score[-1] * 2
            else:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = -score[-1]
        elif i == '0' and dartResult[idx-1] == '1':
            score[-1] = 10
        else:
            score.append(int(i))

    for i in score:
        answer += i

    print(answer)
    return answer
