def solution(n):
    """
    ::: => Array[A:B:n] 사용
    A 번째 부터 B index까지 n 간격으로 배열을 만들어라

    """
    answer = []
    for i in list(str(n)):
        answer.insert(0,int(i))
    return answer