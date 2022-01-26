from functools import reduce
import numpy as np


INPUT_FILE = "advent.of.code.2021/Day 4: Giant Squid/input.txt"


def read_input(input_file=INPUT_FILE, bingo_board_dim=5):
    with open(input_file, "rt") as fp:
        # Read and process drawn numbers
        drawn_numbers = [int(number.strip()) for number in fp.readline().split(",")]

        # Read bingo boards
        bingo_boards = list()
        bingo_board = list()
        for line in fp:
            if line.strip() != "":
                bingo_board.append([int(number) for number in line.strip().split()])
                if len(bingo_board) == bingo_board_dim:
                    bingo_boards.append(np.array(bingo_board))
                    bingo_board = list()
                    
        return drawn_numbers, bingo_boards


def win_condition_met(marked_numbers):
    return any(marked_numbers.all(axis=0)) or any(marked_numbers.all(axis=1))


def play_bingo_t1(drawn_numbers, bingo_boards):
    for i, number in enumerate(drawn_numbers):
        for j, board in enumerate(bingo_boards):
            # Mark matching numbers with `-1`
            board[board == number] = -1
            # Check if win condition is met
            marked_numbers = board == -1
            if win_condition_met(marked_numbers):
                return np.sum(board, where=~marked_numbers, axis=(0,1)) * number, i, j


def task_one(drawn_numbers, bingo_boards):
    winning_result, number_idx, board_idx = play_bingo_t1(drawn_numbers, bingo_boards)
    print("Winning numbers: ", drawn_numbers[:number_idx+1])
    print("Winning board: \n", bingo_boards[board_idx])
    print("Winning result: ", winning_result)


def play_bingo_t2(drawn_numbers, bingo_boards):
    completed_boards = list()
    for i, number in enumerate(drawn_numbers):
        for j, board in enumerate(bingo_boards):
            # Skip completed boards
            if j in completed_boards:
                continue

            # Mark matching numbers with `-1`
            board[board == number] = -1

            # Check if win condition is met
            marked_numbers = board == -1
            if win_condition_met(marked_numbers):
                completed_boards.append(j)

                # Return final score if the last board is completed
                if len(completed_boards) == len(bingo_boards):
                    return np.sum(board, where=~marked_numbers, axis=(0,1)) * number, i, j


def task_two(drawn_numbers, bingo_boards):
    winning_result, number_idx, board_idx = play_bingo_t2(drawn_numbers, bingo_boards)
    print("Winning numbers: ", drawn_numbers[:number_idx+1])
    print("Winning board: \n", bingo_boards[board_idx])
    print("Winning result: ", winning_result)


def main():
    drawn_numbers, bingo_boards = read_input()
    task_one(drawn_numbers, bingo_boards)
    task_two(drawn_numbers, bingo_boards)


if __name__ == "__main__":
    main()