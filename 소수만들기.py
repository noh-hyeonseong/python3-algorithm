def solution(nums):
    answer = 0

    for i in range(0,len(nums)):
        temp = nums[i]
        for j in range(i + 1,len(nums)):
            temp2 = temp + nums[j]
            for k in range(j + 1, len(nums)):
                temp3 = temp2 + nums[k]
                if testNum(temp3) == True:
                    answer = answer + 1
                temp3 = temp2
    return answer

def testNum(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True