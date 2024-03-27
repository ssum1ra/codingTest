import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

res = 0

def dfs():
    