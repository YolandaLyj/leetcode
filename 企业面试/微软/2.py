import sys
def solution(N, A, B):
    # write your code in Python 3.6
    indegree = [0] * (N + 1)
    for i in range(len(A)):
        indegree[A[i]] += 1
        indegree[B[i]] += 1
    index = sorted(range(len(indegree)), key=lambda k: indegree[k])
    res = 0
    for i in range(N + 1):
        if i == 0:
            continue
        res += indegree[index[i]] * i
    return res

N=5
A=[2, 2, 1, 2]
B=[1, 3, 4, 4]
print(solution(N,A,B))