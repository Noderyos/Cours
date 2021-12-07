class Ex1:
    # 1.
    def multiplie_objet(objet,n):
        return [objet]*n
    
    
    # 2.
    def chaine2liste(objet):
        return [i for i in objet]
    
    #3. fait un tableau de tout les code ascii entre 65 et 123 sauf si il est entre 91 et 97

class Ex2:
    #1.
    def somme_ligne(carre,l):
        j = 0
        for i in carre[l]:
            j += i
        return j
    
    #2.
    def somme_colonne(carre,l):
        j = 0
        for i in range(len(carre)):
            j += carre[i][l]
        return j
    
    def somme_diag1(carre):
        j = 0
        for i in range(len(carre)):
            j += carre[i][i]
        return j
    
    def somme_diag2(carre):
        j = 0
        k = len(carre) - 1
        for i in range(len(carre)):
            j += carre[k - i][k - i]
        return j
    
    #3.
    def verif(carre):
        u = Ex2.somme_ligne(carre,0)
        for i in range(3):
            if Ex2.somme_ligne(carre,i) != u:
                return -1
            if Ex2.somme_colonne(carre,i) != u:
                return -1
        if Ex2.somme_diag1(carre) != u:
                return -1
        if Ex2.somme_diag2(carre) != u:
                return -1
        return u
    
    #5.
    
class Ex3:
    #a.
    def total_ventes(dic):
        i = 0;
        for j in dic.values():
            i += j
        return i
    #b.
    def vendeur_max_ventes(dic):
        v = list(dic)[0]
        for i in dic.keys():
            if dic[i] > dic[v]:
                v = i
        return v
    
    #2.
    def dict_occurences_lettres(a):
        a = a.upper()
        b = {}
        for i in a:
            b[i] = a.count(i)
        return b
    
    
    
class Ex4:
    #2.
    def list_cases_vide(sudoku):
        c = []
        for a in range(len(sudoku)):
            for b in range(len(sudoku[a])):
                if sudoku[a][b] == 0:
                    c.append((a,b))
        return c
        
print(Ex1.multiplie_objet("Salut",12))
print(Ex1.chaine2liste("Salut"))

print(Ex2.somme_ligne([[2,7,6],[9,5,1],[4,3,8]],1))
print(Ex2.somme_colonne([[2,7,6],[9,5,1],[4,3,8]],0))
print(Ex2.somme_diag1([[2,7,6],[9,5,1],[4,3,8]]))
print(Ex2.somme_diag2([[2,7,6],[9,5,1],[4,3,8]]))
print(Ex2.verif([[2,7,6],[9,5,1],[4,3,8]]))
print(Ex2.verif([[11,24,7,20,3],[4,12,25,8,16],[17,5,13,21,9],[10,18,1,14,22],[23,6,19,2,15]]))
print(Ex3.total_ventes({"Dupont":14,"Hervy":19,"Geoffroy":15,"Layec":21}))
print(Ex3.vendeur_max_ventes({"Dupont":14,"Hervy":19,"Geoffroy":15,"Layec":21}))
print(Ex3.dict_occurences_lettres("dictionnaire"))
print(Ex4.list_cases_vide([[0,0,0,0,2,0,7,0,8],[5,2,0,0,0,0,0,6,0],[1,0,4,0,0,9,0,5,0],[0,0,0,1,7,8,0,0,6],[0,0,0,0,4,0,8,0,0],[0,0,0,9,5,6,0,0,0],[6,0,0,0,0,5,2,0,7],[0,9,0,0,0,3,0,8,0],[0,3,2,7,0,4,5,9,0]]))