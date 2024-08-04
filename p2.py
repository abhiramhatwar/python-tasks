import sys

def getLIS(N, A):
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[i] >= A[j] and (A[i] - A[j] == 0 or ((A[i] - A[j]) & (A[i] - A[j] - 1)) == 0):
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    N = int(sys.stdin.readline().strip())
    A = []
    for _ in range(N):
        A.append(int(sys.stdin.readline().strip()))
    result = getLIS(N, A)
    print(result)

if __name__ == "__main__":
    main()