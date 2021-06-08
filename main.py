#!/bin/python3

# Complete the 'solution' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
import poketmon
import budget
import 음양더하기
import 소수만들기
import 내적
import 로또순위
import 신규아이디추천
import 키패드누르기
import 약수의개수와덧셈
import 실패율

if __name__ == '__main__':
    print("==========main start==========")

    # 프로그래머스 레벨 1 내적
    # a = [1,2,3,4]
    # b = [-3,-1,0,2]
    # 내적.solution(a,b)

    # 프로그래머스 레벨1 소수 만들기 문제
    # nums = [1,2,3,4]
    # 소수만들기.solution(nums)

    # 프로그래머스 레벨1 음양더하기기문제
    # absolutes = [4,7,12]
    # signs = [True,False,True]
    # 음양더하기.solution(absolutes, signs)

    #프로그래머스 레벨1 포켓몬 문제
    #poketmon_nums = [3,3,3,2,2,4]
    #poketmon.solution(poketmon_nums)

    # 프로그래머스 레벨1 예산 문제
    #budget_d = [1,3,2,5,4]
    #budget_budget = 9
    #budget.solution(budget_d,budget_budget)

    # 프로그래머스 레벨1 로또의 최고 순위와 최저 순위 문제
    #lottos = [44, 1, 0, 0, 31, 25]
    #win_nums = [31, 10, 45, 1, 6, 19]
    #로또순위.solution(lottos,win_nums)

    # 프로그래머스 레벨1 신규 아이디 추천 문제
    # new_id = "..........."
    # 신규아이디추천.solution(new_id)

    # 프로그래머스 레벨1 키패드 누르기
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # hand = "right"
    # 키패드누르기.solution(numbers, hand)

    # 프로그래머스 레벨1 약수의 개수와 덧셈 문제
    # left = 13
    #right = 17
    # 약수의개수와덧셈.solution(left, right)

    # 프로그래머스 레벨1 실패율 문제
    N = 5
    stages = [2,1,2,4,2,4,3,3]
    실패율.solution(N, stages)