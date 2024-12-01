import random

def print_grid(grid):
    for row in grid:
        print(" ---" * 3)
        print("| " + " | ".join(row) + " |")
    print(" ---" * 3)

def check_winner(grid):
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return grid[0][2]
    return None

def make_move(grid, player):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if grid[row][col] == ' ':
            grid[row][col] = player
            break

def main():
    grid = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_grid(grid)
        make_move(grid, players[turn])
        winner = check_winner(grid)
        if winner:
            print_grid(grid)
            print(f"Player {winner} wins")
            break
        if all(cell != ' ' for row in grid for cell in row):
            print_grid(grid)
            print("Draw")
            break
        turn = 1 - turn
        input("Press Enter to continue...")

main()