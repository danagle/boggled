# cli_solver.py
import argparse
import os

from boggled import BoggleBoard, BoggleSolver, BoggleWords


def solve_board(board, words):
    solver = BoggleSolver(board, words)
    solver.solve()
    return solver


def display_board_details(board):
    print("Board details:")
    print("Columns: ", board.columns)
    print("Rows: ", board.rows)
    s = '\n'
    for pos in board.tiles:
        s += '  ' if len(board.tiles[pos]) == 2 else '   '
        s += board.tiles[pos]
        if (pos % board.columns) == 0:
            s += '\n'
    print(s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("letters", type=str,
                        help="Board letters")
    parser.add_argument("dictionary", type=str,
                        help="The text file containing the dictionary word list.")
    parser.add_argument("-m", "--min", type=int,
                        help="The minimum word size.")
    parser.add_argument("-p", "--paths", action="store_true",
                        help="Include the path followed for each word found.")

    args = parser.parse_args()

    if os.path.isfile(args.dictionary):
        if isinstance(args.min, int):
            words = BoggleWords(args.min)
        else:
            words = BoggleWords()
        words.loadFromFile(args.dictionary)

        board = BoggleBoard(args.letters)
        display_board_details(board)
        solved_board = solve_board(board, words)

        print('Found:', len(solved_board.found))
        if args.paths:
            for word in solved_board.found:
                print('{} : {}'.format(word, solved_board.found[word]))
        else:
            print(solved_board.foundWords)
    else:
        print("Error: Unable to find the dictionary.")
