class Ex1:
	#1
	def multiplie_objet(obj,n):
		return [obj] * n

	#2
	def chaine2liste(chaine):
		return [i for i in chaine]
	#3
	# crée un tabeau avec out les chars entre 65 et 127 exepté de 91 à 97
class Ex2:
	#1
	def somme_ligne(carre,n):
		i = 0
		for j in carre[n]:
			i += j
		return i

	#2
	def somme_colonne(carre,n):
		i = 0
		for j in carre:
			i += j[n]
		return i
	def somme_diag_a(carre):
		i = 0
		for j in range(len(carre)):
			i += carre[j][j]
		return i
	def somme_diag_b(carre):
		i = 0
		m = len(carre) - 1
		for j in range(len(carre)):
			i += carre[m - j][m - j]
		return i

	#3
	def valide(carre):
		if Ex2.somme_diag_a(carre) != 65 or Ex2.somme_diag_b(carre) != 65:
			return -1
		for i in range(len(carre) - 1):
			if Ex2.somme_ligne(carre,i) != 65:
				return -1
			if Ex2.somme_colonne(carre,i) != 65:
				return -1
		return Ex2.somme_diag_a(carre)

class Ex3:
	#1 a
	def total_ventes(dic):
		i = 0
		for j in dic.values():
			i += j
		return i

	#1 b
	def vendeur_max_ventes(dic):
		v = ""
		i = 0
		for j in dic:
			if i < dic[j]:
				i = dic[j]
				v = j
		return j

	#2
	def dict_occurence_lettres(chaine):
		dic = {}
		for i in chaine.upper():
			dic[i] = chaine.upper().count(i)
		return dic


class Sudoku:
	#1
	sudoku = [[0, 0, 0, 0, 2, 0, 7, 0, 8], 
			  [5, 2, 0, 0, 0, 0, 0, 6, 0], 
			  [1, 0, 4, 0, 0, 9, 0, 5, 0], 
			  [0, 0, 0, 1, 7, 8, 0, 0, 6], 
			  [0, 0, 0, 0, 4, 0, 8, 0, 0], 
			  [0, 0, 0, 9, 5, 6, 0, 0, 0], 
			  [6, 0, 0, 0, 0, 5, 2, 0, 7], 
			  [0, 9, 0, 0, 0, 3, 0, 8, 0], 
			  [0, 3, 2, 7, 0, 4, 5, 9, 0]]

	#2
	def liste_cases_vide(sudoku):
		cases = []
		for i in range(len(sudoku)):
			for j in range(len(sudoku)):
				if sudoku[i][j] == 0:
					cases.append((i,j))
		return cases

	#3
	def est_dans_ligne(sudoku,index,value):
		return value in sudoku[index]

	def est_dans_colonne(sudoku,index,value):
		for i in sudoku:
			if i[index] == value:
				return True
		return False

	def est_dans_bloc(sudoku,index,value):
		block = (index // 3,index % 3)
		for i in range(3):
			for j in range(3):
				if sudoku[block[0] * 3 + i][block[1] * 3 + j] == value:
					return True
		return False

	#4
	def liste_candidats_case(sudoku,coord):
		i = []
		for j in range(1,10):
			if not Sudoku.est_dans_ligne(sudoku,coord[0],j):
				if not Sudoku.est_dans_colonne(sudoku,coord[1],j):
					if not Sudoku.est_dans_bloc(sudoku,(coord[0] // 3) *3 + (coord[1] // 3),j):
						i.append(j)
		return i

	#5
	def liste_candidats(sudoku):
		i = []
		for j in Sudoku.liste_cases_vide(sudoku):
			i.append(Sudoku.liste_candidats_case(sudoku,j))
		return i


