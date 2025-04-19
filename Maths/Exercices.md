1. Equations différentielles d'ordre 1

Décomposer la fraction rationnelle: 3 / p(p+2)
Résoudre l'EDO par transformation de laplace: 
y' + 2y = 3
y(0) = 1

### Résolution

3 / p(p+2) = a/p + b/(p+2)
Méthode du cache possible, ou résolution de bourrin, mais là on a une EDO à résoudre.
On établi deux cas, p=0 et p=-2, et on résout le système d'équations.
a = 3/2 et b = -3/2.
On a donc 3 / p(p+2) = 3/2 * 1/p - 3/2 * 1/(p+2)
On remplace dans l'EDO:
y' + 2y = 3/2 * 1/p - 3/2 * 1/(p+2)
On applique la transformée de Laplace:
L{y'} + 2L{y} = 3/2 * L{1/p} - 3/2 * L{1/(p+2)}
On a donc:
L{y'} = pL{y} - y(0) + 2L{y} = 3/2 * L{1/p} - 3/2 * L{1/(p+2)}
L{y'} = pL{y} - 1 + 2L{y} = 3/2 * 1/p - 3/2 * e^(-2t)
L{y'} = (p + 2)L{y} - 1 = 3/2 * 1/p - 3/2 * e^(-2t)
L{y'} = 3/2 * 1/p - 3/2 * e^(-2t) + 1


2. Equations différentielles d'ordre 2

Décomposer la fraction rationnelle: 3 / (p-4)(p+2)
Résoudre l'EDO par transformation de laplace:
y'' - 2y' - 8y = 0
y(0) = 0 et y'(0) = 1

### Résolution

3 / (p-4)(p+2) = a/(p-4) + b/(p+2)
Méthode du cache possible, ou résolution de bourrin, mais là on a une EDO à résoudre.
On établi deux cas, p=4 et p=-2, et on résout le système d'équations.
a = 1/2 et b = -1/2.
On a donc 3 / (p-4)(p+2) = 1/2 * 1/(p-4) - 1/2 * 1/(p+2)
On remplace dans l'EDO:

y'' - 2y' - 8y = 1/2 * 1/(p-4) - 1/2 * 1/(p+2)
On applique la transformée de Laplace:

L{y''} - 2L{y'} - 8L{y} = 1/2 * L{1/(p-4)} - 1/2 * L{1/(p+2)}
...
$y(t) = \frac{1}{6} e^{4t} - \frac{1}{6} e^{-2t}$

3. Calcul d'intégrales
Utiliser les transformées de Laplace pour calculer les intégrales suivantes:

I = Intégrale entre +infini et 0 de cos(2t)*e^(-3t) dt
J = Intégrale entre +infini et 0 de sin(t)*e^(-t) dt

### Résolution

I: On sait que $\mathcal{L}\{\cos(2t)\} = \frac{p}{p^2 + 4}$
L'intégrale peut donc être vue comme la transformée de Laplace de cos(2t) évaluée en p=-3.

4. Lecture table de Laplace

Donner la transformée de Laplace de: y(t) = sin(t)*e^(-t)

5. La fonction cosinus hyperbolique

y(t) = cosh(t) = e^(t) + e^(-t) / 2	
Par usage de la transformée de Laplace, déterminer une fonction égale à sa dérivée seconde

y'' = y
y(0) = 0 et y'(0) = 1

6. Résolution d'un système différentiel

Soit le système différentiel ci-dessous où x(t) et y(t) sont des fonctions dérivables, et x'(t) et y'(t) sont leurs dérivées respectives.
Résoudre ce système par Laplace:

x - y = x'
-x + y = y'

Avec les conditions initiales suivantes:
x(0) = 1 et y(0) = 1



Exercice 0

1. Déterminer les transformées des fonctions suivantes: 
a. f(t) = sin(3t) 
b. g(t) = e^(-2t)
c. h(t) = 3t^2 + 3t + 1

2. Déterminer les originaux des fonctions suivantes:

a. F(p) = 2/(p+3)
b. H(p) = p/(p^2 + 2)
c. G(p) = 2/(p^2 + 4)
d. I(p) = (p^2 + 1)/p^2 


Exercice 1

1. Déterminer l'original de G(p) = 4/(4p-1)
2. Déterminer a et b tels que 1/p(4p-1) = a/p + b/(4p-1)
3. Résoudre l'EDO:

4y' - y = 1
y(0) = 1


Exercice 2

1. Factoriser G(p) = p^2 + p - 2
2. Déterminer a et b tels que 1/(p^2 + p - 2) = a/(p-1) + b/(p+2)
3. Résoudre l'EDO:

y'' + y' - 2y = 0
y(0) = 0 et y'(0) = 1


Exercice 3

"Calculer" par la transformée de Laplace l'intégrale:

I = Intégrale entre 0 et +infini de sin(4t)e^(-3t) dt

Exercice 4

Résoudre par la méthode de Laplace

y'' + 4y = 0
y(0) = 0 et y'(0) = 1
