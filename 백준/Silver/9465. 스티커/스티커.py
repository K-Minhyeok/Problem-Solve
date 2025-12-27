import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    l = [[int(x) for x in input().split()] for _ in range(2)]
    if N == 1:
        print(max(l[0][0],l[1][0]))
        continue
    
    dp = [[0]*N for _ in range(2)] # 0번부터 i번 열의 스티커를 뗄 때, 각 행에서 취할 수 있는 최대 점수
    dp[0][0] = l[0][0]
    dp[1][0] = l[1][0]
    dp[0][1] =  dp[1][0]+ l[0][1]
    dp[1][1] =  dp[0][0]+ l[1][1]
    for i in range(2,N):
        # 각 레벨에서 취할 수 있는 최댓값을 정한다.
        # 앞 단계 or 그 앞 대각선 중에 하나 골라온다.
        dp[0][i] = max(dp[1][i-1],dp[1][i-2]) + l[0][i]
        dp[1][i] = max(dp[0][i-1],dp[0][i-2]) + l[1][i]
        # for j in range(2):
        #     print(*dp[j])
        # print()

    print(max(dp[0][-1],dp[1][-1]))


