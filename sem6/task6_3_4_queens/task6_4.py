from task6_3 import position_queens, random_position_queens

queens = [(1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2), (8, 8)]
result = position_queens(queens)
print(result)

cool_positions = random_position_queens()
for position in cool_positions:
    print(position)