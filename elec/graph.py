import matplotlib.pyplot as plt

# Données du premier tableau
n1 = [1500, 1580, 1651, 1680, 1730, 1800, 1890, 1940, 2050, 2130]
Ie = [0.62, 0.54, 0.46, 0.44, 0.40, 0.36, 0.32, 0.30, 0.27, 0.25]

# Données du deuxième tableau
n2 = [934, 1035, 1155, 1283, 1337, 1435, 1542, 1653, 1826, 1972]
Um = [105, 118, 131, 145, 151, 161, 173, 185, 203, 220]

# Données du troisième tableau
n3 = [934, 1035, 1155, 1283, 1337, 1435, 1542, 1653, 1826, 1972]
Kphi = [1.0467, 1.0638, 1.0598, 1.0577, 1.0573, 1.0512, 1.0518, 1.0501, 1.0439, 1.0484]


# Rendement
rendement = [0.39, 0.53, 0.59, 0.63, 0.64, 0.65, 0.66, 0.65, 0.65, 0.64]

# Pu
Pu = [238, 445, 629, 805, 948, 1081, 1181, 1283, 1331, 1410]

plt.plot(rendement, Pu, marker='o', color='blue')
plt.title('Rendement vs Pu')
plt.xlabel('Rendement')
plt.ylabel('Pu')
plt.grid(True)
plt.show()

plt.plot(Pu, rendement, marker='o', color='blue')
plt.title('Rendement vs Pu BIS')
plt.xlabel('Rendement')
plt.ylabel('Pu')
plt.grid(True)
plt.show()

# Tracé de la première courbe : n(Ie)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(n1, Ie, marker='o', color='blue')
plt.title('n(Ie)')
plt.xlabel('n')
plt.ylabel('Ie')
plt.grid(True)

# Tracé de la deuxième courbe : n(Um)
plt.subplot(1, 2, 2)
plt.plot(n2, Um, marker='s', color='green')
plt.title('n(Um)')
plt.xlabel('n')
plt.ylabel('Um')
plt.grid(True)

# Tracé de la troisième courbe : n(Kphi)
# Formule: (U-RiIi) / Omega
# Avec RiIi = 4*Ii et Omega = n*3.14/30
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(n3, Kphi, marker='^', color='red')
plt.title('n(Kphi)')
plt.xlabel('n')
plt.ylabel('Kphi')
plt.grid(True)

plt.tight_layout()
plt.show()



