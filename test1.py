"""
작성자 : 이승준
작성일 : 2024.10.07
작성내용 : x만큼 간격이 있는 n개의 숫자
제한조건 :
● x는 -10000000 이상, 10000000 이하인 정수입니다.
● n은 1000 이하인 자연수입니다.
"""

def solution(x, n):

    # 제한조건 체크
    if not (-10000000 <= x <= 10000000):
        raise ValueError("x는 -10000000 이상, 10000000 이하의 정수여야 합니다.")
    if not (1 <= n <= 1000):
        raise ValueError("n은 1 이상, 1000 이하의 자연수여야 합니다.")
    
    answer = []
    for i in range(n):
        answer.append(x + x * i)
    return answer

# 입출력 예시
# x, n = map(int, input().split())
# print(solution(x, n))
