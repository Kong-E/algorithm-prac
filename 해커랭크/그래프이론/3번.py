def tasks(n, a, b):
  result = n
  tasks_dict = {i + 1: [] for i in range(n)}
  
  # tasks_dict 구성
  for i in range(len(b)):
      tasks_dict[b[i]].append(a[i])

  # 순환 의존성 찾기
  visited = set()
  for key in tasks_dict.keys():
      if key not in visited:
          cycle = set()
          stack = [key]
          while stack:
              node = stack.pop()
              if node in cycle:
                  # 순환 의존성 발견됨
                  while stack:
                      result -= 1
                      stack.pop()
                  break
              cycle.add(node)
              stack.extend(tasks_dict[node])
              visited.add(node)

  return int(result)

# 입력 받기
n = int(input())
m = int(input())
a = [int(input()) for _ in range(m)]
m = int(input())
b = [int(input()) for _ in range(m)]

# 결과 출력
print(tasks(n, a, b))
