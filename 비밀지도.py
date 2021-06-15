def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        map1_temp = bin(i)[2:]
        map2_temp = bin(j)[2:]
        while len(map1_temp) < n:
            map1_temp = "0" + map1_temp
        while len(map2_temp) < n:
            map2_temp = "0" + map2_temp
        temp = ""
        for k,q in zip(map1_temp,map2_temp):
            if k == '1' or q == '1':
                temp = temp + "#"
            else:
                temp = temp + " "
        answer.append(temp)
    print(answer)
    return answer