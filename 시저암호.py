def solution(s, n):
    """
    아스키 코드 활용 문제
    ord() : 문자 -> 숫자
    chr() : 숫자 -> 문자
    """
    answer = ''
    print(ord('a'),ord('z'),ord('A'),ord(('Z')))
    for i in s:
        if 65 <= ord(i) <= 90:
            changeWord = ord(i) + n
            if changeWord > 90:
                changeWord = 64 + changeWord - 90
            changeWord = chr(changeWord)
            answer += changeWord
        elif 97 <= ord(i) <= 122:
            changeWord = ord(i) + n
            if changeWord > 122:
                changeWord = 66 + changeWord - 97
            changeWord = chr(changeWord)
            answer += changeWord
        else:
            answer += " "
    return answer