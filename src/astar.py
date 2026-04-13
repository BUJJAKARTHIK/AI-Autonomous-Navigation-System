import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, end):
    rows = len(grid)
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

        for dx, dy in neighbors:
            neighbor = (current[0]+dx, current[1]+dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < rows:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                temp_g = g_score[current] + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g
                    f_score[neighbor] = temp_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None