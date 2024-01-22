import sys

input = sys.stdin.readline

def generate_permutations(sequence, chosen, m):
    if len(chosen) == m:  # 원하는 길이의 순열이 완성됐으면
        print(' '.join(map(str, chosen)))  # 순열을 출력하고
        return  # 이 경로는 끝났으니 돌아가기
      
    for i in sequence:
        if i in chosen:
            continue
        chosen.append(i)
        generate_permutations(sequence, chosen, m)
        chosen.pop() # 다른 숫자를 시도하기 위해 마지막 숫자 제거

n, m = map(int, input().split())
generate_permutations(range(1, n+1), [], m)
