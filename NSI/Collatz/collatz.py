import matplotlib.pyplot as plt
from fonctions_collatz import *
Y = collatz_liste(127)
X = [i for i in range(len(Y))]
plt.plot(X,Y)
plt.show()