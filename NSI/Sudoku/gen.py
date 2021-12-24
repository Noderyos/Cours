from sudoku import *
from random import randint

def main():
	sudoku = [[0 for i in range(9)] for j in range(9)]
	for a in range(9):
		for b in range(9):
			for c in Final.liste_candidats(sudoku):
				if len(c[1]) > 0:
					sudoku[a][b] = c[1][randint(0,len(c[1]) - 1)]
	print(sudoku)

if __name__ == '__main__':
	main()