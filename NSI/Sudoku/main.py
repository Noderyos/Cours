from sudoku import *
from PIL import Image, ImageFont, ImageDraw

def write_image(sudoku,file_in,file_out):
	img = Image.open(file_in)
	font = ImageFont.truetype("DejaVuSerif.ttf", size=40)
	draw = ImageDraw.Draw(img)

	coo_img = []
	for i in range(9):
		coo_img.append([(i*54 + 20,j*52 + 10) for j in range(9)])
	for i in range(len(coo_img)):
		for j in range(len(coo_img[i])):
			if sudoku[i][j] != 0:
				draw.text((coo_img[i][j]), str(sudoku[i][j]),0,font=font)
	img.save(file_out)

def main():
	sudokus = [
					[
						[4,5,1,0,3,0,0,9,8],
						[0,6,3,0,0,8,0,2,5],
						[8,0,2,7,5,9,1,0,6],
						[0,2,9,3,8,0,0,0,1],
						[0,4,0,0,6,1,0,5,9],
						[0,3,7,0,9,4,0,0,2],
						[9,0,6,5,7,0,2,8,4],
						[7,8,4,0,2,6,0,0,3],
						[0,0,5,9,0,3,7,0,0]
					]
				]
	vv = 0
	for sudoku in sudokus:
		i = 0
		while len(Final.liste_candidats(sudoku)) != 0:
			sudoku = Final.resolve(sudoku,Final.liste_candidats(sudoku))
			print(Final.liste_candidats(sudoku))
			i += 1
		Final.display(sudoku)

		write_image(sudoku,"sudoku.jpg","sudoku" + str(vv) + ".jpg")
		print(f"\n\nFOUND IN {str(i - 1)} TRIES\n\n")
		vv += 1
	


if __name__ == '__main__':
	main()