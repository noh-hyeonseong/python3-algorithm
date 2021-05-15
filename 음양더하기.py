def solution(absolutes, signs):
    answer = 0
    for i,j in zip(absolutes, signs):
        if j == True:
            answer = answer + i
        elif j == False:
            answer = answer - i
    return answer