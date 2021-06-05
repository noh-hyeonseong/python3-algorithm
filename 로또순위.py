def solution(lottos, win_nums):
    answer = []
    zeroNum = lottos.count(0)
    hitNum = len(set(lottos)&set(win_nums))
    result = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = [result[hitNum+zeroNum],result[hitNum]]
    return answer