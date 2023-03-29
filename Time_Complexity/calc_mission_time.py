# 알고리즘 수업 - 알고리즘의 수행 시간 6
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
import sys


def mission_time_vers6():
    n = int(sys.stdin.readline().rstrip())
    # 코드1 수행 횟수
    print(int((n * (n - 1) * (n - 2)) / 6))
    # 코드1 수행횟수 다항식으로 표현시, 최고차항 차수
    print(3)


mission_time_vers6()

# 알고리즘 수업 - 알고리즘의 수행 시간 5
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
import sys


def mission_time_vers5():
    n = int(sys.stdin.readline().rstrip())
    # 코드1 수행 횟수
    print(n**3)
    # 코드1 수행횟수 다항식으로 표현시, 최고차항 차수
    print(3)


mission_time_vers5()

# 알고리즘 수업 - 알고리즘의 수행 시간 4
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
import sys


def mission_time_vers4():
    n = int(sys.stdin.readline().rstrip())
    # 코드1 수행 횟수
    print(int((n**2 - n) / 2))
    # 코드1 수행횟수 다항식으로 표현시, 최고차항 차수
    print(2)


mission_time_vers4()

# 알고리즘 수업 - 알고리즘의 수행 시간 3
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
import sys


def mission_time_vers3():
    n = int(sys.stdin.readline().rstrip())
    # 코드1 수행 횟수
    print(n * n)
    # 코드1 수행횟수 다항식으로 표현시, 최고차항 차수
    print(2)


mission_time_vers3()

# 알고리즘 수업 - 알고리즘의 수행 시간 2
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }

import sys


def mission_time_vers2():
    n = int(sys.stdin.readline().rstrip())
    # 코드1 수행 횟수
    print(1 * n)
    # 코드1 수행횟수 다항식으로 표현시, 최고차항 차수
    print(1)
