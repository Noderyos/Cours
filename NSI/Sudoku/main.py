from sudoku import *
def main():
	sudokus = [
					[
						[0,0,0,0,2,0,7,0,8],
						[5,2,0,0,0,0,0,6,0],
						[1,0,4,0,0,9,0,5,0],
						[0,0,0,1,7,8,0,0,6],
						[0,0,0,0,4,0,8,0,0],
						[0,0,0,9,5,6,0,0,0],
						[6,0,0,0,0,5,2,0,7],
						[0,9,0,0,0,3,0,8,0],
						[0,3,2,7,0,4,5,9,0]
					],
					[
						[0,8,0,0,0,0,9,2,0],
						[4,1,0,0,0,8,0,7,0],
						[0,5,0,0,0,0,3,8,0],
						[0,9,0,4,8,1,2,6,0],
						[7,0,2,3,0,0,1,0,0],
						[0,0,0,0,2,0,0,0,0],
						[5,0,6,0,0,2,8,9,0],
						[0,0,8,7,0,0,0,1,6],
						[0,3,0,0,0,0,7,5,0]
					],
					[
						[1,0,0,0,0,0,3,0,0],
						[0,2,0,0,4,3,5,7,0],
						[0,3,0,0,0,8,9,0,2],
						[0,5,6,8,0,1,0,3,4],
						[7,0,0,0,6,5,2,0,0],
						[0,0,1,0,0,0,0,0,0],
						[0,0,0,6,2,4,0,0,3],
						[0,0,0,0,3,0,0,0,0],
						[0,0,9,0,0,0,0,0,6]
					],
					[
						[0,2,9,0,6,0,8,7,5],
						[4,0,0,0,7,0,6,0,3],
						[3,0,0,0,0,5,1,0,4],
						[0,0,0,0,0,1,0,8,0],
						[8,0,0,2,0,0,9,5,0],
						[5,9,0,0,0,8,0,6,1],
						[0,0,6,3,5,7,2,0,0],
						[0,1,0,0,0,0,0,0,6],
						[0,8,0,6,0,2,0,4,0]
					]
				]

	for sudoku in sudokus:
		i = 0
		while len(Final.liste_candidats(sudoku)) != 0:
			sudoku = Final.resolve(sudoku,Final.liste_candidats(sudoku))
			i += 1
		Final.display(sudoku)
		print(f"\n\nFOUND IN {str(i - 1)} TRIES\n\n")

if __name__ == '__main__':
	main()