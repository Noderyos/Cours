from sudoku import *


def test():
	print("\n---- Ex1 ----\n")
	print(Ex1.multiplie_objet("NSI",3))
	print(Ex1.chaine2liste("Python"))

	print("\n---- Ex2 ----\n")
	carre = [[11, 24, 7, 20, 3],[4, 12, 25, 8, 16],[17, 5, 13, 21, 9],[10, 18, 1, 14, 22],[23, 6, 19, 2, 15]]
	print(Ex2.somme_ligne(carre,0))
	print(Ex2.somme_colonne(carre,0))
	print(Ex2.somme_diag_a(carre))
	print(Ex2.somme_diag_b(carre))
	print(Ex2.valide(carre))

	print("\n---- Ex3 ----\n")
	print(Ex3.total_ventes({"Dupond": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}))
	print(Ex3.vendeur_max_ventes({"Dupond": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}))
	print(Ex3.dict_occurence_lettres("dictionnaire"))

	print("\n---- Ex4 ----\n")
	sudoku = [[0, 0, 0, 0, 2, 0, 7, 0, 8], 
			  [5, 2, 0, 0, 0, 0, 0, 6, 0], 
			  [1, 0, 4, 0, 0, 9, 0, 5, 0], 
			  [0, 0, 0, 1, 7, 8, 0, 0, 6], 
			  [0, 0, 0, 0, 4, 0, 8, 0, 0], 
			  [0, 0, 0, 9, 5, 6, 0, 0, 0], 
			  [6, 0, 0, 0, 0, 5, 2, 0, 7], 
			  [0, 9, 0, 0, 0, 3, 0, 8, 0], 
			  [0, 3, 2, 7, 0, 4, 5, 9, 0]]
	print(Sudoku.liste_cases_vide(sudoku))
	print(Sudoku.est_dans_ligne(sudoku,0,3))
	print(Sudoku.est_dans_colonne(sudoku,0,7))
	print(Sudoku.est_dans_bloc(sudoku,0,1))
	print(Sudoku.liste_candidats_case(sudoku,(4,1)))
	print(Sudoku.liste_candidats(sudoku))
def main():
	sudoku = [[0, 0, 0, 0, 2, 0, 7, 0, 8], 
			  [5, 2, 0, 0, 0, 0, 0, 6, 0], 
			  [1, 0, 4, 0, 0, 9, 0, 5, 0], 
			  [0, 0, 0, 1, 7, 8, 0, 0, 6], 
			  [0, 0, 0, 0, 4, 0, 8, 0, 0], 
			  [0, 0, 0, 9, 5, 6, 0, 0, 0], 
			  [6, 0, 0, 0, 0, 5, 2, 0, 7], 
			  [0, 9, 0, 0, 0, 3, 0, 8, 0], 
			  [0, 3, 2, 7, 0, 4, 5, 9, 0]]
	Final.display(sudoku)





if __name__ == '__main__':
	main()