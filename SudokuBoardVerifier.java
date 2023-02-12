package test4;

public class SudokuBoardVerifier {

	public static void main(String[] args) {
		int[][] board = new int[][] { { 1, 2, 3, 4, 5, 6, 7, 8, 9 }, { 2, 3, 4, 5, 6, 7, 8, 9, 1 },
				{ 3, 4, 5, 6, 7, 8, 9, 1, 2 }, { 4, 5, 6, 7, 8, 9, 1, 2, 3 }, { 5, 6, 7, 8, 9, 1, 2, 3, 4 },
				{ 6, 7, 8, 9, 1, 2, 3, 4, 5 }, { 7, 8, 9, 1, 2, 3, 4, 5, 6 }, { 8, 9, 1, 2, 3, 4, 5, 6, 7 },
				{ 9, 1, 2, 3, 4, 5, 6, 7, 8 } };

		int[][] board2 = new int[][] { { 1, 3, 2, 5, 7, 9, 4, 6, 8 }, { 4, 9, 8, 2, 6, 1, 3, 7, 5 },
				{ 7, 5, 6, 3, 8, 4, 2, 1, 9 }, { 6, 4, 3, 1, 5, 8, 7, 9, 2 }, { 5, 2, 1, 7, 9, 3, 8, 4, 6 },
				{ 9, 8, 7, 4, 2, 6, 5, 3, 1 }, { 2, 1, 4, 9, 3, 5, 6, 8, 7 }, { 3, 6, 5, 8, 1, 7, 9, 2, 4 },
				{ 8, 7, 9, 6, 4, 2, 1, 5, 3 } };

		int[][] board3 = new int[][] { { 9, 2, 6, 5, 8, 3, 4, 7, 1 }, { 7, 1, 3, 4, 2, 6, 9, 8, 5 },
				{ 8, 4, 5, 9, 7, 1, 3, 6, 2 }, { 3, 6, 2, 8, 5, 7, 1, 4, 9 }, { 4, 7, 1, 2, 6, 9, 5, 3, 8 },
				{ 5, 9, 8, 3, 1, 4, 7, 2, 6 }, { 6, 5, 7, 1, 3, 8, 2, 9, 4 }, { 2, 8, 4, 7, 9, 5, 6, 1, 3 },
				{ 1, 3, 9, 6, 4, 2, 8, 5, 7 } };

		int[][] board4 = new int[][] { { 8, 4, 7, 2, 6, 5, 1, 0, 3 }, { 1, 3, 6, 7, 0, 8, 2, 4, 5 },
				{ 0, 5, 2, 1, 4, 3, 8, 6, 7 }, { 4, 2, 0, 6, 7, 1, 5, 3, 8 }, { 6, 7, 8, 5, 3, 2, 0, 1, 4 },
				{ 3, 1, 5, 4, 8, 0, 7, 2, 6 }, { 5, 6, 4, 0, 1, 7, 3, 8, 2 }, { 7, 8, 1, 3, 2, 4, 6, 5, 0 },
				{ 2, 0, 3, 8, 5, 6, 4, 7, 1 } };

		System.out.println(SudokuBoardVerifier.validate(board) == false);
		System.out.println(SudokuBoardVerifier.validate(board2) == true);
		System.out.println(SudokuBoardVerifier.validate(board4) == false);
		System.out.println(SudokuBoardVerifier.validate(board3) == true);

	}

	public static boolean validate(int[][] board) {
		// use squares array to verify whether each 3x3 square is valid (all cells have
		// unique values)
		int[][][] squares = new int[9][3][3];

		// use test array verify uniqueness of rows, columns, and squares
		int[] test_arr = new int[9];

		int start_ri = 0;
		int start_ci = 0;

		// check all rows to see if they have unique values

		while (start_ci < 9) {
			for (int i = 0; i < 9; i++) {
				if (board[start_ci][i] == 0) {
					return false;
				}
				test_arr[board[start_ci][i] - 1] += 1;
			}
			for (int i = 0; i < 9; i++) {
				if (test_arr[i] > 1) {
					return false;
				}
			}
			start_ci += 1;
			for (int k = 0; k < 9; k++) {
				test_arr[k] = 0;
			}
		}

		// check all columns to see if they have unique values
		start_ci = 0;

		while (start_ri < 9) {
			for (int i = 0; i < 9; i++) {
				if (board[i][start_ri] == 0) {
					return false;
				}
				test_arr[board[i][start_ri] - 1] += 1;
			}
			for (int i = 0; i < 9; i++) {
				if (test_arr[i] > 1) {
					return false;
				}
			}
			start_ri += 1;
			for (int k = 0; k < 9; k++) {
				test_arr[k] = 0;
			}
		}

		start_ri = 0;

		int index_j = 0;
		int index_k = 0;
		int square_i = 0;

		for (int i = 0; i < 3; i++) {
			while (start_ci < 9) {
				for (int j = start_ri; j < start_ri + 3; j++) {
					for (int k = start_ci; k < start_ci + 3; k++) {
						index_j = j;
						index_k = k;
						// adjust j, k indices since squares array is 9x3x3 whereas board is 9x9
						if (j > 2 && j < 6) {
							index_j = j - 3;
						}
						if (k > 2 && k < 6) {
							index_k = k - 3;
						}
						if (j > 5 && j < 9) {
							index_j = j - 6;
						}
						if (k > 5 && k < 9) {
							index_k = k - 6;
						}
						squares[square_i][index_j][index_k] = board[j][k];
					}
				}
				square_i += 1;
				start_ci += 3;
			}
			start_ri += 3;
			start_ci = 0;

		}

		// check all squares to see if they have unique values
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 3; j++) {
				for (int k = 0; k < 3; k++) {
					if (squares[i][j][k] == 0) {
						return false;
					}
					test_arr[squares[i][j][k] - 1] += 1;
				}
			}
			for (int l = 0; l < 9; l++) {
				if (test_arr[l] > 1) {
					return false;
				}
			}
			for (int l = 0; l < 9; l++) {
				test_arr[l] = 0;
			}

		}
		return true;

	}

}
