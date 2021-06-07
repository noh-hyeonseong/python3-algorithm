def solution(numbers, hand):
    answer = ''
    left = {1:[0,0], 4:[1,0], 7:[2,0]}
    right = {3:[0,2], 6:[1,2], 9:[2,2]}
    dial = {2:[0,1], 5:[1,1], 8:[2,1], 0:[3,1] }
    leftF = [3,0]
    rightF = [3,2]
    for i in numbers:
        if i in left:
            answer = answer + "L"
            leftF = left[i]
        elif i in right:
            answer = answer + "R"
            rightF = right[i]
        else:
            leftFD = abs(leftF[0]-dial[i][0]) + abs(leftF[1]-dial[i][1])
            rightFD = abs(rightF[0]-dial[i][0]) + abs(rightF[1]-dial[i][1])
            if leftFD > rightFD:
                answer = answer + "R"
                rightF = dial[i]
            elif leftFD < rightFD:
                answer = answer + "L"
                leftF = dial[i]
            elif hand == "right":
                answer = answer + "R"
                rightF = dial[i]
            else:
                answer = answer + "L"
                leftF = dial[i]

    print(answer)
    return answer