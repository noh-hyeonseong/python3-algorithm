def solution(n):
    """
    정수 판별
    int로 변환 한 수를 뺐을 때 0일 때
    나머지가 0일 때
    """
    if (n ** 0.5) - int(n ** 0.5) == 0:
        answer = int((n ** 0.5 + 1) ** 2)
    else:
        answer = -1
    print(answer)
    return answer