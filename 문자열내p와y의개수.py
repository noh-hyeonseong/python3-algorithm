def solution(s):
    answer = True
    pNum = s.count('p') + s.count('P')
    yNum = s.count('y') + s.count('Y')
    if pNum == 0 and yNum == 0:
        answer = True
    elif pNum != yNum:
        answer = False

    return answer