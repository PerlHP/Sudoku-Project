from sudoku_generator import SudokuGenerator

def main():
    # assign 'size' and 'removed'
    size = 9
    removed = 30

    # create instance of SudokuGenerator
    sudoku = SudokuGenerator(size, removed)

    # call provided function to fill values
    sudoku.fill_values()

    # call provided function to get board
    board = sudoku.get_board()

    # call function to remove cells
    sudoku.remove_cells()

    # call function to get board
    board = sudoku.get_board()

    sudoku.print_board()

if __name__ == '__main__':
    main()