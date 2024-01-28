from turtle import *

tracer(False)

def draw_grid_and_path(grid, path):

    penup()
    goto((0-len(grid[0]))*10, (len(grid[0]))*10)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(i, j)
            if grid[i][j]:
                fillcolor("white")
            else:
                fillcolor("black")
            begin_fill()
            for _ in range(4):
                forward(20)
                right(90)
            end_fill()
            forward(20)
        backward(20 * len(grid[0]))
        right(90)
        forward(20)
        left(90)

    if path:
        goto((0 - len(grid[0])) * 10, (len(grid[0])) * 10)
        color("red")
        width(2)
        penup()
        goto((path[0][1] * 20) - 160, 110 - (path[0][0] * 20))
        pendown()
        for node in path:
            goto((node[1] * 20) - 160, 110 - (node[0] * 20))
    update()


def find_shortest_path(grid, start, end):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]

    visited = set()
    queue = [(start, [start])]

    while queue:
        current, path = queue.pop(0)
        visited.add(current)

        if current == end:
            return path

        for dx, dy in directions:
            next_x, next_y = current[0] + dx, current[1] + dy
            if (next_x, next_y) not in visited and is_valid_move(next_x, next_y):
                queue.append(((next_x, next_y), path + [(next_x, next_y)]))
                visited.add((next_x, next_y))

    return None


grid = [[True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, True, False, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, False, False], [False, True, False, True, False, True, False, True, False, False, False, False, False, True, False, True, False, True, False, False], [False, True, False, True, False, True, True, True, True, True, True, True, False, True, False, True, False, True, False, False], [False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, True, False, True, False, False], [False, True, True, True, True, True, False, True, False, True, True, True, False, True, True, True, False, True, False, False], [False, False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, False, False], [False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False], [False, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, False, False], [False, True, False, True, False, False, False, False, False, True, False, True, False, True, False, True, False, False, False, False], [False, True, False, True, True, True, True, True, False, True, False, True, False, True, False, True, True, True, False, False], [False, True, False, False, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, False], [False, True, True, True, False, True, False, True, False, True, False, True, True, True, True, True, False, True, False, False], [False, False, False, True, False, True, False, True, False, True, False, False, False, False, False, False, False, True, False, False], [False, True, False, True, False, True, False, True, False, True, True, True, True, True, False, True, True, True, False, False], [False, True, False, True, False, True, False, True, False, False, False, False, False, True, False, True, False, False, False, False], [False, True, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True]]


start = (0, 0)
end = (len(grid[0])-1, len(grid[0])-1)

setup(400, 300)
bgcolor("lightgray")
speed(0)
hideturtle()

path = find_shortest_path(grid, start, end)

draw_grid_and_path(grid, path)

done()
