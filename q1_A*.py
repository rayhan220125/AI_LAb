import heapq

start = (0, 0)
goal = (2, 2)
obstacle = (1, 1)

def h(p):
    return abs(goal[0] - p[0]) + abs(goal[1] - p[1])

pq = [(h(start), 0, start, [start])]
visited = set()

while pq:
    f, g, node, path = heapq.heappop(pq)

    if node in visited:
        continue
    visited.add(node)

    if node == goal:
        print("Optimal Path:", path)
        print("Cost:", g)
        break

    x, y = node
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3 and (nx, ny) != obstacle:
            new_g = g + 1
            new_f = new_g + h((nx, ny))
            heapq.heappush(pq, (new_f, new_g, (nx, ny),
                                path + [(nx, ny)]))
