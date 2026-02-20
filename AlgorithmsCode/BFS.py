"""
BFS算法
"""
# from collections import deque

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# def bfs(graph, start_node):
#     visited = set()

#     queue = deque([start_node])
#     visited.add(start_node)

#     print("BFS 遍历顺序：", end="")

#     while queue:
#         current = queue.popleft()
#         print(current, end="")

#         for neighbor in graph[current]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)

# result = bfs(graph, 'A')
# print(result)

#例题

from collections import deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    N, M = int(data[0]), int(data[1])
    grid = [list(row) for row in data[2:]]

    queue = deque()
    dist = [[-1] * M for _ in range(N)]
    empty_land_count = 0

    # 1. 初始化队列，将所有初始生长的力量加入 BFS
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'G':
                dist[r][c] = 0
                queue.append((r, c))
            elif grid[r][c] == 'S':
                dist[r][c] = 1 # 种子在第1天变G，之后才能传播
                queue.append((r, c))
            elif grid[r][c] == '.':
                empty_land_count += 1

    # 如果初始就没有空地，且有种子或作物，天数取决于种子变G的时间
    if empty_land_count == 0:
        max_d = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 'S': max_d = max(max_d, 1)
        print(max_d)
        return

    # 2. 开始 BFS 传播
    max_days = 0
    filled_count = 0

    while queue:
        r, c = queue.popleft()

        # 遍历四个方向
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # 如果是空地且未被覆盖
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == '.' and dist[nr][nc] == -1:
                # 空地变 S 需要 1 天，S 变 G 又需要 1 天
                # 所以到达新空地的时间是当前 G 的时间 + 1
                dist[nr][nc] = dist[r][c] + 1
                max_days = max(max_days, dist[nr][nc])
                filled_count += 1
                queue.append((nr, nc))

    # 3. 结果判断
    # 所有的 'S' 最终也会变 'G'，所以要考虑初始种子长成的时间
    initial_s_max = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'S':
                initial_s_max = max(initial_s_max, 1)

    final_res = max(max_days, initial_s_max)

    if filled_count < empty_land_count:
        print("-1")
    else:
        print(final_res)

solve()
