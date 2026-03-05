1class Solution:
2    def findJudge(self, n: int, trust: List[List[int]]) -> int:
3        score = [0] * (n + 1)
4
5        for a, b in trust:
6            score[a] -= 1
7            score[b] += 1
8
9        for i in range(1, n + 1):
10            if score[i] == n - 1:
11                return i
12
13        return -1