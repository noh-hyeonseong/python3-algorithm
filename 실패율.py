def solution(N, stages):
    rank = {}
    perNum = len(stages)
    for i in range(1,N+1):
        failNum = 0
        for j in stages:
            if j == i:
                failNum += 1
        failPer = failNum / perNum
        rank[i] = failPer
        perNum = perNum - failNum
        if perNum == 0:
            for k in range(i+1,N+1):
                rank[k] = 0
            break
    answer = [x[0] for x in sorted(rank.items(), key=lambda x: (-x[1],x[0]))]
    return answer