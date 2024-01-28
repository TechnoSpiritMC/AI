import random

# Taille du labyrinthe
rows = 20
cols = 20

# Générer une grille vide remplie de murs (False)
grid = [[False] * cols for _ in range(rows)]


# Fonction pour générer le labyrinthe
def generate_maze(grid, start, end):
    # Marquer le début et la fin du labyrinthe
    grid[start[0]][start[1]] = True
    grid[end[0]][end[1]] = True

    # Fonction pour vérifier si une cellule est valide pour placer un mur
    def is_valid_cell(row, col):
        return 0 < row < rows - 1 and 0 < col < cols - 1 and not grid[row][col]

    # Liste des directions possibles (haut, bas, gauche, droite)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Fonction pour creuser le labyrinthe
    def dig(row, col):
        grid[row][col] = True
        random.shuffle(directions)
        for dr, dc in directions:
            if is_valid_cell(row + (dr * 2), col + (dc * 2)):
                grid[row + dr][col + dc] = True
                dig(row + (dr * 2), col + (dc * 2))

    # Creuser à partir du point de départ
    dig(start[0], start[1])


# Point de départ et d'arrivée
start = (1, 1)
end = (rows - 2, cols - 2)

# Générer le labyrinthe
generate_maze(grid, start, end)

# Afficher le labyrinthe
for row in grid:
    print("".join("#" if cell else " " for cell in row))

print(grid)