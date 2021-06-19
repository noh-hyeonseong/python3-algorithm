def solution(nums):

    answer = 0
    max = len(nums)/2
    set_nums = set(nums)
    nums = list(set_nums)

    print(len(nums))
    if max <= len(nums):
        answer = max
    else:
        answer = len(nums)

    return answer