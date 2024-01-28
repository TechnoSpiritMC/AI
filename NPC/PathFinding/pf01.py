import turtle
import heapq

turtle.speed(0)

# Créer une carte avec des couloirs représentés par une liste de True et de False
# True : couloir disponible, False : mur
map = [
    [True, True, True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, False, False, True],
    [True, True, True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, False, False, True],
    [True, True, True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, False, False, True],
    [True, True, True, True, True, True, True, True, True, True]
]


# Fonction pour dessiner la carte
def draw_map():
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-150, 150)
    turtle.pendown()
    for row in map:
        for cell in row:
            if cell:
                turtle.fillcolor("white")
            else:
                turtle.fillcolor("black")
            for _ in range(4):
                turtle.forward(10)
                turtle.right(90)
            turtle.forward(10)
        turtle.backward(10 * len(row))
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
    turtle.hideturtle()


# Fonction pour trouver le chemin le plus court entre deux points
def find_shortest_path(start, end):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == end:
            break

        for next_node in get_neighbors(current_node):
            new_cost = cost_so_far[current_node] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(end, next_node)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current_node

    path = []
    while current_node != start:
        path.append(current_node)
        current_node = came_from[current_node]
    path.append(start)
    path.reverse()
    return path


# Fonction pour calculer la distance entre deux points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Fonction pour obtenir les voisins d'une cellule
def get_neighbors(cell):
    x, y = cell
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < len(map) and 0 <= y + dy < len(map[0]) and map[x + dx][y + dy]:
                neighbors.append((x + dx, y + dy))
    return neighbors


# Dessiner la carte
draw_map()

# Coordonnées de départ et d'arrivée
start = (0, 0)
end = (6, 9)

# Trouver le chemin le plus court
path = find_shortest_path(start, end)

# Dessiner le chemin trouvé
turtle.penup()
turtle.color("red")
turtle.pensize(3)
turtle.setpos((start[1] * 10) - 145, 145 - (start[0] * 10))
turtle.pendown()
for cell in path:
    turtle.setpos((cell[1] * 10) - 145 + 5, 145 - (cell[0] * 10) - 5)
turtle.hideturtle()

turtle.done()
