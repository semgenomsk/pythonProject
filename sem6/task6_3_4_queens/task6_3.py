import random

def position_queens(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(
                    queens[i][1] - queens[j][1]):
                return False
    return True

def random_position_queens():
    def is_valid(queens):
        for i in range(8):
            for j in range(i + 1, 8):
                if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(
                        queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                    return False
        return True

    cool_positions = []
    while len(cool_positions) < 4:
        queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if is_valid(queens) and queens not in cool_positions:
            cool_positions.append(queens)
    return cool_positions

if __name__ == 'main':
    print(random_position_queens())