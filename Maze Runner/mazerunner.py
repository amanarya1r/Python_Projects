import random

def generate_maze(width, height, num_traps=5, num_rewards=5, num_enemies=3):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    def carve_path(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                maze[y + dy // 2][x + dx // 2] = ' '
                maze[ny][nx] = ' '
                carve_path(nx, ny)

    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '
    carve_path(start_x, start_y)

    maze[0][1] = 'S'  # Start
    maze[height-1][width-2] = 'E'  # End

    def place_items(symbol, count):
        placed = 0
        while placed < count:
            x, y = random.randint(1, width-2), random.randint(1, height-2)
            if maze[y][x] == ' ':
                maze[y][x] = symbol
                placed += 1

    place_items('T', num_traps)    # Traps
    place_items('R', num_rewards)  # Rewards
    place_items('X', num_enemies)  # Enemies

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

width, height = 30, 20  # Must be odd numbers
maze = generate_maze(width, height)
print_maze(maze)
