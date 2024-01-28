def transform_to_grid(bool_list):
    row_length = int(len(bool_list) ** 0.5)  # Calcul automatique de la longueur de la ligne
    grid = []
    for i in range(0, len(bool_list), row_length):
        row = bool_list[i:i + row_length]
        grid.append(row)
    print(grid)
    return grid


def parseSeed(seed):
    _seed = []
    for char in str(seed):
        _seed.append(True if char == "1" else False)
    return _seed


# Exemple d'utilisation
bool_list = [False, True, False, True, False, True, True, True, False, False, False, False, False, False, True, False,
             False, True, False, True, False, False, True, False, True, False, True, False, False, True, False, True,
             False, False, False, True, True, True, False, True, False, False, True, False, True, True, False, False,
             False, True, True, False, True, True, False, False, True, True, True, False, False, False, False, False,
             True, True, False, False, False, False, True, True, True, False, False, False, True, False, False, True,
             True, False, True, True, False, False, False, False, True, True, False, False, False, True, True, False,
             True, True, False, False, True, False, False, True, True, False, True, False, False, True, False, False,
             False, True, False, True, True, True, True, False, True, False, True, False, False, True, False, False,
             False, False, False, False, False, True, True, False, False, True, False, True, True, True, True, True,
             True, True, True, False, False, False, True, False, False, True, True, False, False, True, False, True,
             True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, False,
             False, True, True, False, False, True, True, False, False, False, True, True, True, True, False, False,
             False, False, False, True, True, True, True, False, True, False, True, True, False, False, True, True,
             False, False, False, False, True, False, True, False, False, False, True, False, True, True, True, False,
             False, True, False, True, False, False, False, False, False, False, False, False, False, False, True,
             False, True, False, True, True, True, False, False, False, False, True, True, True, False, True, False,
             False, True, True, False, False, True, True, False, False, True, False, False, True, True, False, False,
             False, True, False, False, False, False, True, True, True, False, False, True, False, True, False, True,
             False, True, True, False, True, False, True, False, True, False, False, False, False, True, True, True,
             False, True, False, True, True, False, True, True, False, True, True, False, True, True, True, False, True,
             True, True, True, True, False, False, True, True, False, False, False, True, False, True, False, False,
             False, True, False, False, True, True, True, False, True, True, True, False, False, True, True, False,
             False, False, False, False, False, False, True, True, True, False, True, True, False, True, False, True,
             True, False, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True,
             True, True, True, True, False, False, False, True, True, True, True, True, False, True, False, True, True,
             False, True, False, False, True, True, False, False, False, True, False, True, False, True, True, False,
             True, False, True, False, False, True, False, True, False, False, False, False, False, False, True, True,
             False, True, False, True, True, True, True, False, False, False, False, True, False, True, True, False,
             True, True, True, True, False, False, True, False, True, True, True, True, False, False, False, True,
             False, True, False, True, False, False, True, False, False, False, False, False, False, False, False, True,
             True, True, False, False, False, True, False, True, False, False, False, True, True, False, False, True,
             False, True, False, True, True, False, False, True, True, False, False, False, False, True, True, False,
             False, False, True, True, False, False, False, False, True, False, True, False, False, False, True, False,
             False, True, False, False, False, False, True, False, False, True, True, False, False, False, False, True,
             False, False, False, True, True, True, True, False, False, True, True, True, False, False, False, False,
             True, True, True, True, False, True, False, True, True, False, True, True, True, False, True, False, False,
             False, False, False, False, False, True, False, False, True, False, False, True, True, False, False, False,
             False, False, False, True, True, True, True, True, True, False, True, False, True, False, True, True, True,
             True, False, True, True, False, False, False, False, True, False, True, False, False, False, True, False,
             False, False, False, True, True, False, False, True, False, True, False, True, False, False, False, True,
             False, False, True, False, False, False, True, False, False, True, False, False, True, True, True, True,
             True, False, True, True, False, True, True, False, True, True, True, True, False, False, True, True, True,
             True, False, False, True, False, True, False, False, False, False, False, True, True, False, False, True,
             True, True, False, False, False, True, True, False, True, True, True, False, False, True, True, False,
             True, False, False, False, True, False, False, False, True, True, True, False, True, False, False, False,
             True, False, True, True, False, False, False, True, False, False, False, True, False, False, True, False,
             True, True, True, False, False, True, True, False, False, False, False, False, False, True, False, False,
             True, True, False, True, True, True, True, False, True, True, False, True, True, True, False, False, True,
             False, True, True, True, True, False, False, False, True, False, True, False, False, True, False, False,
             False, False, False, True, False, True, True, False, False, False, False, False, True, False, False, False,
             False, False, False, False, False, False, True, False, False, True, False, False, True, True, True, True,
             False, True, True, True, True, False, False, False, True, False, False, False, False, False, False, True,
             True, True, True, False, True, True, True, True, False, True, False, True, True, False, False, True, False,
             True, True, False, True, False, False, False, True, False, True, False, True, True, False, True, False,
             False, False, True, False, False, False, False, True, True, False, True, False, True, False, False, True,
             False, False, False, True, False, True, False, True, False, True, False, True, False, True, False, True,
             True, False, False, True, True, False, False, True, True, True, False, False, False, True, False, False,
             False, False, True, True, False, True, False, True, True, True, True, False, True, True, True, True, False,
             True, True, True, True, True, False, False, True, True, False, True, True, False, False, False, False,
             False, False, False, True, True, True, False, True, False, True, False, True, True, True, False, True,
             True, True, False, True, True, False, True, False, True, False, True, False, True, False, True, True, True,
             True, True, False, True, True, True, True, False, False, True, True, True, False, True, False, True, False,
             True, True, False, False, False, False, True, True, False, True, False, True, False, False, False, False,
             False, False, True, False, False, False, True, True, False, False, False, True, True, True, False, False,
             False, True, True, True, False, True, True, False, False, False, False, False, False, True, False, False,
             False, False, True, False, False, False, False, True, True, True, False, False, True, True, True, True,
             False, True, False, True, False, False, False, False, True, True, False, False, True, False, True, False,
             True, False, False, False, False, False, True, False, True, False, True, False, True, False, False, False,
             True, True, True, False, True, False, False, False, False, True, False, True, True, False, False, False,
             False, False, True, True, True, True, False, False, False, True, True, False, True, True, True, False,
             True, True, False, False, False, True, False, False, True, False, False, False, False, False, True, True,
             False, False, False, False, False, True, False, True, True, False, True, True, False, False, False, True,
             False, False, False, True, True, True, True, False, True, False, True, False, False, False, False, True,
             True, True, True, False, True, True, False, True, False, True, True, False, True, False, True, True, False,
             False, False, True, True, True, False, True, True, True, True, True, True, True, True, True, False, False,
             True, False, True, False, False, False, True, True, False, False, True, True, False, True, True, True,
             False, False, True, False, False, False, False, True, True, True, True, False, True, False, True, False,
             False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, False,
             True, False, False, True, False, False, False, True, False, True, True, True, False, False, False, True,
             False, False, True, False, False, True, False, True, True, False, True, True, True, True, False, True,
             True, True, False, False, True, True, False, True, True, True, True, True, False, False, True, False,
             False, False, True, False, True, False, True, False, True, False, False, True, True, True, False, False,
             False, True, False, False, False, True, False, True, False, True, True, False, True, False, True, False,
             True, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False,
             False, True, True, False, True, True, False, True, True, True, False, False, False, False, True, True,
             False, True, True, True, True, False, True, True, True, False, False, True, True, True, True, False, True,
             True, False, False, True, True, False, False, True, False, True, True, True, False, False, False, False,
             False, False, False]

transform_to_grid(bool_list)
