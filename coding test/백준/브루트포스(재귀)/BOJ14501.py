# 앞에서부터 진행하려고 하면 더하는 값의 최적 값을 모름
import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i + table[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(table[i][1] + dp[i + table[i][0]], dp[i + 1])

print(dp[0])

""" dfs 코드
import sys; input = sys.stdin.readline
def consult(day, p_total):
    global answer
    # 퇴사일의 경우
    if day == N:
        answer = max(answer, p_total) # 최대이익으로 정산
        return
    t = Work[day][0] # 상담 소요일
    p = Work[day][1] # 상담 수입

    # 해당 일부터 상담하는 경우
    if t + day <= N:
        consult(t + day, p_total + p)
    # 해당 일의 다음 날부터 상담하는 경우
    consult(day + 1, p_total)

if __name__ == "__main__":
    N = int(input())
    Work = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    # 시작일 순차적으로 방문
    for day in range(N):
        consult(day, 0)
    print(answer) """
