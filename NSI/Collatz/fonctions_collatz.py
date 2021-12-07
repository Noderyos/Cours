def temps_vol(x : int):
    """
    Retourne en sortie le plus petit indice n tel que un= 1
    Paramètre
    ----------
    x : int
    Nombre entier étant u0
    Sortie
    -------
    : int
    Valeur du nombre d'itérations avant que un = 1'
    Exemples :
    ---------
    >>> temps_vol(15)
    10
    >>> temps_vol(127)
    25
    """
    
    if not isinstance(x, int):
        raise TypeError("la variable x doit être un entier")
    if x <= 0:
        raise ValueError("la variable x doit être strictement positive")
        
    i = 0
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
        i += 1
    return i


def collatz_liste(x : int):
    """
    Retourne en sortie la liste des valeur avant le plus petit indice n tel que un= 1
    Paramètre
    ----------
    x : int
    Nombre entier étant u0
    Sortie
    -------
    : list
    Liste des valeurs de un avant que un = 1'
    Exemples :
    ---------
    >>> collatz_liste(15)
    [15 ,46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    
    if not isinstance(x, int):
        raise TypeError("la variable x doit être un entier")
    if x <= 0:
        raise ValueError("la variable x doit être strictement positive")
        
    i = []
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
        i.append(int(x))
    return i

def altitude_max(x : int):
    """
    Retourne en sortie la valeur un la plus élevée avant que un = 1
    Paramètre
    ----------
    x : int
    Nombre entier étant u0
    Sortie
    -------
    : int
    Valeur max de un avant que un = 1'
    Exemples :
    ---------
    >>> altitude_max(15)
    160
    """
    
    return(sorted(collatz_liste(x)))[-1]


def vol_altitude(x : int):
    """
    Retourne la valeur max de n avant que un <= u0
    Paramètre
    ----------
    x : int
    Nombre entier étant u0
    Sortie
    -------
    : int
    Valeur max de n avant que un <= u0'
    Exemples :
    ---------
    >>> vol_altitude(15)
    10
    """
    
    u = collatz_liste(x)
    for i in range(len(u)):
        if u[i] < x:
            return i