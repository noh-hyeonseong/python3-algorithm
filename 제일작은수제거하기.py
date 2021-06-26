def solution(arr):
    minNum = min(arr)
    while minNum in arr:
        arr.remove(minNum)
    answer = arr
    if len(arr) == 0:
        answer = [-1]
    return answer