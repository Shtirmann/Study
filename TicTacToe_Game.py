import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Размер окна
SCREEN_SIZE = (600, 600)

# Создание окна
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Крестики-нолики")

# Размеры клеток и сетки
CELL_SIZE = 200
GRID_SIZE = 3
GRID_WIDTH = 10

# Создание сетки
def create_grid():
    grid = []
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            row.append(0)
        grid.append(row)
    return grid

grid = create_grid()

# Рисование сетки
def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), GRID_WIDTH)
            if grid[i][j] == 1:
                pygame.draw.line(screen, BLUE, (x+20, y+20), (x+CELL_SIZE-20, y+CELL_SIZE-20), GRID_WIDTH)
                pygame.draw.line(screen, BLUE, (x+CELL_SIZE-20, y+20), (x+20, y+CELL_SIZE-20), GRID_WIDTH)
            elif grid[i][j] == 2:
                pygame.draw.circle(screen, RED, (x+CELL_SIZE//2, y+CELL_SIZE//2), CELL_SIZE//2-20, GRID_WIDTH)

# Проверка победы
def check_win():
    for i in range(GRID_SIZE):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]
    return 0

# Ход игрока
def player_move(x, y):
    i = y // CELL_SIZE
    j = x // CELL_SIZE
    if grid[i][j] == 0:
        grid[i][j] = 1
        return True
    return False

# Ход компьютера
def computer_move():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                grid[i][j] = 2
                if check_win() == 2:
                    return
                grid[i][j] = 0

    best_score = -float("inf")
    best_move = None

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                grid[i][j] = 2
                score = minimax(grid, False)
                grid[i][j] = 0
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    grid[best_move[0]][best_move[1]] = 2

def minimax(grid, is_maximizing):
    winner = check_win()
    if winner == 2:
        return 1
    elif winner == 1:
        return -1
    elif is_board_full(grid):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    score = minimax(grid, False)
                    grid[i][j] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    score = minimax(grid, True)
                    grid[i][j] = 0
                    best_score = min(score, best_score)
        return best_score

def is_board_full(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

#Обработка событий
def handle_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if not check_win():
				x, y = pygame.mouse.get_pos()
				if player_move(x, y):
					computer_move()

#Очистка экрана и рисование объектов
def draw():
	screen.fill(WHITE)
	draw_grid()
	pygame.display.flip()

#Главный игровой цикл
def main_loop():
	while True:
		handle_events()
		draw()

#Запуск игры
if __name__ == '__main__':
	main_loop()