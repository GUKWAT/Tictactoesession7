# Fixed the win condition checks in the is_win function. Changed not all to all to properly check for winning conditions.
# Corrected the diagonal win condition in the is_win function. Changed board[1][0] to board[0][0].
# Added an explicit return False statement at the end of the is_win function to handle cases where no win condition is met.
# Wrapped the input reading in a try-except block to handle invalid input (e.g., non-integer input) gracefully.
# Added an except IndexError bl
# ock to handle cases where the user enters row and column values outside the range (0-2).

"""A 3x3 board is initialized"""
board = [[' ' for _ in range(3)] for _ in range(3)]


def print_board():
    """Function draws a 3x3 tictactoe board game"""
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def is_win(player):
    """

    Checks for the win conditions for the rows, columns and diagonals for player O OR X

    Arg: player

    Returns:
    bool True if a player wins but if not it returns false

    """

    for i in range(3):
        if all([cell == player for cell in board[i]]):  # 1. Changed 'not all' to 'all'
            return True
        if all([board[j][i] == player for j in range(3)]):  # 2. Changed 'not all' to 'all'
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:  # 3. Changed 'board[1][0]' to 'board[0][0]'
        return True
    return False  # 4. Added explicit return False if no win condition is met


def tally_wins(results):
    """
    Checks for draw


    arg:results : an empty list

    returns
    the sum of the empty list, if full without a win condition being met the result is a draw

    """
    return sum(results)


def main():
    """Main game loop where all the functions are called and where the user is validated """
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()
        try:
            row, col = map(int,
                           input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
            if board[row][col] == ' ':
                board[row][col] = current_player
                win = is_win(current_player)
                results.append(win)
                if win:
                    print_board()
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
                moves += 1
            else:
                print("Cell already occupied! Try again.")
        except ValueError:
            print("Invalid input! Please enter two integers separated by space.")
        except IndexError:
            print("Invalid input! Please enter row and column values within the range (0-2).")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()
