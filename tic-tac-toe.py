board = [" "] * 9

win = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

player = "X"
moves = 0

while True:
    print()
    print("TIC TAC TOE")
    print("---*---*---*")

    for i in range(9):
        if board[i] == " ":
            print(i + 1, end=" ")
        else: 
            print(board[i], end=" ")

        if i % 3 == 2:
            print()

    print("---*---*---*")

    choice = int(input("Player " + player + ", enter number (1-9): "))

    if choice < 1 or choice > 9:
        print("Invalid number! Try again.")
        continue

    if board[choice - 1] != " ":
        print("Space already filled! Try again.")
        continue

    board[choice - 1] = player
    moves += 1

    won = False

    for a, b, c in win:
        if board[a] == board[b] == board[c] == player:
            won = True

    if won:
        print("Player", player, "wins!")
        break

    if moves == 9:
        print("Game is a draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

print()
print("Final Board:")

for i in range(9):
    print(board[i], end=" ")
    if i % 3 == 2:
        print()