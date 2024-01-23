import sys

input = sys.stdin.readline
n = int(input())

def solve_n_queens(row, n, posDiag, negDiag, cols, count):
    if row == n:
        count[0] += 1
        return

    for col in range(n):
        # 대각선과 열의 상태를 체크
        if cols[col] or posDiag[row + col] or negDiag[row - col + n - 1]:
            continue

        # 퀸을 배치하고 상태를 업데이트
        cols[col] = posDiag[row + col] = negDiag[row - col + n - 1] = True
        
        # 다음 행으로 넘어가기
        solve_n_queens(row + 1, n, posDiag, negDiag, cols, count)
        
        # 퀸을 제거하고 상태를 복원
        cols[col] = posDiag[row + col] = negDiag[row - col + n - 1] = False

count = [0]
# 각 열과 두 대각선 방향의 상태를 관리하는 배열
cols = [False] * n
posDiag = [False] * (2 * n - 1)
negDiag = [False] * (2 * n - 1)
solve_n_queens(0, n, posDiag, negDiag, cols, count)

print(count[0])