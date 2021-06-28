import numpy as np

def solution(arr1, arr2):
    """
    행렬은 numpy 모듈을 활용하면 더 쉽게 풀 수 있음
    import numpy as np
    """

    #numpy 사용 코드
    A = np.array(arr1)
    B = np.array(arr2)
    answer = (A + B).tolist()
    print(answer)
    return answer

    #기존 코드
    # answer = []
    # for i, j in zip(arr1, arr2):
    #     tempArr = []
    #     for k, p in zip(i, j):
    #         tempArr.append(k+p)
    #     answer.append(tempArr)
    # return answer