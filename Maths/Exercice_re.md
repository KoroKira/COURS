### 🔧 **Exercice 1 – Équation différentielle d’ordre 1**
Équation :  
> \( y' + 2y = 3 \), avec \( y(0) = 1 \)

**Transformée de Laplace:**
\[
\mathcal{L}\{y'\} + 2\mathcal{L}\{y\} = \mathcal{L}\{3\}
\]
\[
pY(p) - y(0) + 2Y(p) = \frac{3}{p}
\]
\[
(p + 2)Y(p) - 1 = \frac{3}{p}
\]
\[
(p + 2)Y(p) = \frac{3}{p} + 1 = \frac{3 + p}{p}
\]
\[
Y(p) = \frac{3 + p}{p(p + 2)}
\]

**Décomposition en éléments simples:**  
Il faut en fait faire la décomposition de :  
\[
\frac{3 + p}{p(p + 2)} = \frac{A}{p} + \frac{B}{p + 2}
\]

Multiplions par le dénominateur :
\[
3 + p = A(p + 2) + Bp
\]
Développons :
\[
3 + p = Ap + 2A + Bp = (A + B)p + 2A
\]

Identifions :
- \( A + B = 1 \)
- \( 2A = 3 \Rightarrow A = \frac{3}{2}, \quad B = -\frac{1}{2} \)

Donc :
\[
Y(p) = \frac{3}{2}\cdot\frac{1}{p} - \frac{1}{2}\cdot\frac{1}{p+2}
\]

**Retour dans le domaine temporel** :
\[
y(t) = \frac{3}{2} - \frac{1}{2}e^{-2t}
\]

✅ Résultat final :
\[
\boxed{y(t) = \frac{3}{2} - \frac{1}{2}e^{-2t}}
\]

---


---

### 🔧 **Exercice 2 – Équation différentielle d’ordre 2**

Équation :  
> \( y'' - 2y' - 8y = 0 \)  
> Conditions : \( y(0) = 0 \), \( y'(0) = 1 \)

---

#### 🔁 Étape 1 – Transformée de Laplace

\[
\mathcal{L}\{y''\} - 2\mathcal{L}\{y'\} - 8\mathcal{L}\{y\} = 0
\]
On remplace les transformées :
\[
(p^2 Y(p) - p y(0) - y'(0)) - 2(pY(p) - y(0)) - 8Y(p) = 0
\]
En remplaçant les conditions initiales :
\[
(p^2 Y(p) - 1) - 2pY(p) - 8Y(p) = 0
\]
\[
(p^2 - 2p - 8)Y(p) = 1
\]
\[
Y(p) = \frac{1}{p^2 - 2p - 8}
\]

---

#### 🔁 Étape 2 – Factorisation

On factorise le dénominateur :
\[
p^2 - 2p - 8 = (p - 4)(p + 2)
\Rightarrow Y(p) = \frac{1}{(p - 4)(p + 2)}
\]

---

#### 🔁 Étape 3 – Décomposition en éléments simples

On écrit :
\[
\frac{1}{(p - 4)(p + 2)} = \frac{A}{p - 4} + \frac{B}{p + 2}
\]

Multiplions :
\[
1 = A(p + 2) + B(p - 4)
\Rightarrow 1 = (A + B)p + (2A - 4B)
\]

Système :
- \( A + B = 0 \)
- \( 2A - 4B = 1 \)

Remplaçons \( A = -B \) dans la deuxième :
\[
2(-B) - 4B = 1 \Rightarrow -2B - 4B = 1 \Rightarrow -6B = 1 \Rightarrow B = -\frac{1}{6}, \quad A = \frac{1}{6}
\]

Donc :
\[
Y(p) = \frac{1}{6}\cdot\frac{1}{p - 4} - \frac{1}{6}\cdot\frac{1}{p + 2}
\]

---

#### 🔁 Étape 4 – Retour dans le domaine temporel

\[
\mathcal{L}^{-1}\left\{\frac{1}{p - a}\right\} = e^{at}
\]

Donc :
\[
y(t) = \frac{1}{6}e^{4t} - \frac{1}{6}e^{-2t}
\]

✅ Résultat final :
\[
\boxed{y(t) = \frac{1}{6}e^{4t} - \frac{1}{6}e^{-2t}}
\]

---

---

### 🔧 **Exercice 3 – Calculer l’intégrale suivante :**

\[
I = \int_0^{+\infty} \sin(4t)e^{-3t} \, dt
\]

---

#### 🧠 Astuce :

L'intégrale peut être interprétée comme **la transformée de Laplace de \( \sin(4t) \)** évaluée en \( p = 3 \).

\[
\mathcal{L}\{\sin(at)\} = \frac{a}{p^2 + a^2}
\]

Ici, \( a = 4 \), donc :
\[
\mathcal{L}\{\sin(4t)\} = \frac{4}{p^2 + 16}
\]

En multipliant \( \sin(4t) \) par \( e^{-3t} \), on obtient un **décalage de la transformée** :
\[
\mathcal{L}\{e^{-3t}\sin(4t)\} = \frac{4}{(p + 3)^2 + 16}
\]

Mais ici, on veut l’intégrale directe :
\[
I = \int_0^{+\infty} \sin(4t)e^{-3t} \, dt = \mathcal{L}\{\sin(4t)\} \big|_{p = 3}
\Rightarrow I = \frac{4}{3^2 + 16} = \frac{4}{25}
\]

✅ Résultat final :
\[
\boxed{I = \frac{4}{25}}
\]

---

---

### 🔧 **Exercice 4 – Équation différentielle**

\[
y'' + 4y = 0, \quad y(0) = 0, \quad y'(0) = 1
\]

---

#### 🔁 Étape 1 – Transformée de Laplace

\[
\mathcal{L}\{y''\} + 4\mathcal{L}\{y\} = 0
\]
\[
(p^2 Y(p) - p y(0) - y'(0)) + 4Y(p) = 0
\]
\[
(p^2 Y(p) - 1) + 4Y(p) = 0
\Rightarrow (p^2 + 4)Y(p) = 1
\]
\[
Y(p) = \frac{1}{p^2 + 4}
\]

---

#### 🔁 Étape 2 – Retour dans le domaine temporel

On reconnaît une forme classique :
\[
\mathcal{L}^{-1}\left\{\frac{a}{p^2 + a^2}\right\} = \sin(at)
\]

Ici :
\[
Y(p) = \frac{1}{p^2 + 2^2} \Rightarrow y(t) = \frac{1}{2}\sin(2t)
\]

✅ Résultat final :
\[
\boxed{y(t) = \frac{1}{2}\sin(2t)}
\]

---

---

### 🔧 **Exercice 6 – Résolution du système différentiel**

Système :
\[
\begin{cases}
x' = x - y \\
y' = -x + y
\end{cases}
\quad \text{avec} \quad x(0) = 1, \; y(0) = 1
\]

---

#### 🔁 Étape 1 – Transformée de Laplace

Notons \( X(p) = \mathcal{L}\{x(t)\} \), \( Y(p) = \mathcal{L}\{y(t)\} \)

**Première équation :**  
\[
\mathcal{L}\{x'\} = \mathcal{L}\{x - y\} \Rightarrow pX(p) - x(0) = X(p) - Y(p)
\Rightarrow pX(p) - 1 = X(p) - Y(p)
\Rightarrow (p - 1)X(p) + Y(p) = 1 \quad \text{(1)}
\]

**Deuxième équation :**
\[
\mathcal{L}\{y'\} = \mathcal{L}\{-x + y\} \Rightarrow pY(p) - y(0) = -X(p) + Y(p)
\Rightarrow pY(p) - 1 = -X(p) + Y(p)
\Rightarrow X(p) + (p - 1)Y(p) = 1 \quad \text{(2)}
\]

---

#### 🔁 Étape 2 – Résolution du système

On résout le système :
\[
\begin{cases}
(p - 1)X + Y = 1 \\
X + (p - 1)Y = 1
\end{cases}
\]

Méthode 1 : substitution ou combinaison linéaire  
Multiplions (1) par \( (p - 1) \) :
\[
(p - 1)^2 X + (p - 1)Y = (p - 1)
\]
Soustrayons (2) :
\[
[(p - 1)^2 X + (p - 1)Y] - [X + (p - 1)Y] = (p - 1) - 1
\Rightarrow [(p - 1)^2 - 1]X = p - 2
\]

\[
(p^2 - 2p + 1 - 1)X = p - 2 \Rightarrow (p^2 - 2p)X = p - 2
\Rightarrow X(p) = \frac{p - 2}{p(p - 2)}
\Rightarrow X(p) = \frac{1}{p}
\]

Puis on remplace dans (1) :
\[
(p - 1)\cdot\frac{1}{p} + Y(p) = 1
\Rightarrow \frac{p - 1}{p} + Y(p) = 1 \Rightarrow Y(p) = 1 - \frac{p - 1}{p} = \frac{1}{p}
\]

Donc :
\[
X(p) = Y(p) = \frac{1}{p}
\Rightarrow x(t) = y(t) = 1
\]

✅ Résultat final :
\[
\boxed{x(t) = 1 \quad ; \quad y(t) = 1}
\]

---

---

### 🔧 **Exercice 0.1 – Transformées de Laplace**

Déterminer la transformée de :

#### a. \( f(t) = \sin(3t) \)

Formule :
\[
\mathcal{L}\{\sin(at)\} = \frac{a}{p^2 + a^2}
\Rightarrow \boxed{\mathcal{L}\{\sin(3t)\} = \frac{3}{p^2 + 9}}
\]

---

#### b. \( g(t) = e^{-2t} \)

Formule :
\[
\mathcal{L}\{e^{-at}\} = \frac{1}{p + a}
\Rightarrow \boxed{\mathcal{L}\{e^{-2t}\} = \frac{1}{p + 2}}
\]

---

#### c. \( h(t) = 3t^2 + 3t + 1 \)

On décompose et applique :

- \( \mathcal{L}\{t^2\} = \frac{2}{p^3} \)
- \( \mathcal{L}\{t\} = \frac{1}{p^2} \)
- \( \mathcal{L}\{1\} = \frac{1}{p} \)

Donc :
\[
\boxed{\mathcal{L}\{3t^2 + 3t + 1\} = \frac{6}{p^3} + \frac{3}{p^2} + \frac{1}{p}}
\]

---

### 🔧 **Exercice 0.2 – Originaux (transformées inverses)**

#### a. \( F(p) = \frac{2}{p + 3} \)

\[
\mathcal{L}^{-1}\left\{\frac{a}{p + a}\right\} = ae^{-at}
\Rightarrow \boxed{f(t) = 2e^{-3t}}
\]

---

#### b. \( H(p) = \frac{p}{p^2 + 2} \)

Forme de la dérivée de cosinus :
\[
\mathcal{L}^{-1}\left\{\frac{p}{p^2 + a^2}\right\} = \cos(at)
\Rightarrow \boxed{h(t) = \cos(\sqrt{2}t)}
\]

---

#### c. \( G(p) = \frac{2}{p^2 + 4} \)

\[
\mathcal{L}^{-1}\left\{\frac{a}{p^2 + a^2}\right\} = \sin(at)
\Rightarrow \boxed{g(t) = \sin(2t)}
\]

---

#### d. \( I(p) = \frac{p^2 + 1}{p^2} \)

On sépare :
\[
\frac{p^2 + 1}{p^2} = 1 + \frac{1}{p^2}
\Rightarrow \mathcal{L}^{-1} = \delta(t) + t
\Rightarrow \boxed{i(t) = 1 + t}
\]

---

---

### 🔧 **Exercice 1 – Décomposition & EDO**

---

#### ✅ 1. Trouver l’original de :

\[
G(p) = \frac{4}{4p - 1}
\]

On factorise pour que ça ressemble à une transformée standard :

\[
\frac{4}{4p - 1} = \frac{4}{4(p - \frac{1}{4})} = \boxed{\frac{1}{p - \frac{1}{4}}}
\]

Donc :
\[
\mathcal{L}^{-1}\left\{\frac{1}{p - a}\right\} = e^{at}
\Rightarrow \boxed{g(t) = e^{\frac{1}{4}t}}
\]

---

#### ✅ 2. Trouver \( a \) et \( b \) tels que :

\[
\frac{1}{p(4p - 1)} = \frac{a}{p} + \frac{b}{4p - 1}
\]

On met au même dénominateur :

\[
1 = a(4p - 1) + bp
\Rightarrow 1 = 4ap - a + bp
\Rightarrow 1 = (4a + b)p - a
\]

Comparaison des coefficients :

- Terme en \( p \) : \( 4a + b = 0 \)
- Terme constant : \( -a = 1 \Rightarrow a = -1 \)

Donc :
\[
b = -4a = -4(-1) = 4
\Rightarrow \boxed{\frac{1}{p(4p - 1)} = \frac{-1}{p} + \frac{4}{4p - 1}}
\]

---

#### ✅ 3. Résoudre l’EDO :

\[
4y' - y = 1, \quad y(0) = 1
\]

---

##### 🌀 Étape 1 – Transformée de Laplace

\[
\mathcal{L}\{4y'\} - \mathcal{L}\{y\} = \mathcal{L}\{1\}
\Rightarrow 4(pY(p) - y(0)) - Y(p) = \frac{1}{p}
\Rightarrow 4pY(p) - 4 - Y(p) = \frac{1}{p}
\Rightarrow (4p - 1)Y(p) = \frac{1}{p} + 4
\]

On écrit \( Y(p) \) :

\[
Y(p) = \frac{1/p + 4}{4p - 1} = \frac{1 + 4p}{p(4p - 1)}
\]

Et c’est exactement la fonction de tout à l’heure. On a déjà fait la décomposition :

\[
Y(p) = \frac{-1}{p} + \frac{4}{4p - 1}
\]

---

##### 🌀 Étape 2 – Retour dans le domaine temporel

\[
y(t) = -1 + e^{\frac{1}{4}t}
\]

✅ Résultat final :
\[
\boxed{y(t) = -1 + e^{\frac{1}{4}t}}
\]

---

---

### 🔧 **Exercice 2 – Résolution d’une EDO**

---

#### ✅ 1. Factoriser :

\[
G(p) = p^2 + p - 2
\]

On cherche deux nombres dont le produit est \( -2 \) et la somme \( 1 \) → c’est \( +2 \) et \( -1 \)

\[
\boxed{G(p) = (p - 1)(p + 2)}
\]

---

#### ✅ 2. Décomposition en éléments simples :

\[
\frac{1}{(p - 1)(p + 2)} = \frac{a}{p - 1} + \frac{b}{p + 2}
\]

Multiplions :
\[
1 = a(p + 2) + b(p - 1)
\Rightarrow 1 = (a + b)p + (2a - b)
\]

Égalité des coefficients :
- \( a + b = 0 \)
- \( 2a - b = 1 \)

Substitution : \( b = -a \)  
\[
2a - (-a) = 1 \Rightarrow 3a = 1 \Rightarrow a = \frac{1}{3}, \quad b = -\frac{1}{3}
\]

✅ Résultat :
\[
\boxed{\frac{1}{(p - 1)(p + 2)} = \frac{1}{3(p - 1)} - \frac{1}{3(p + 2)}}
\]

---

#### ✅ 3. Résolution de l’EDO

\[
y'' + y' - 2y = 0, \quad y(0) = 0, \quad y'(0) = 1
\]

---

##### 🌀 Étape 1 – Transformée de Laplace

\[
\mathcal{L}\{y''\} + \mathcal{L}\{y'\} - 2\mathcal{L}\{y\} = 0
\Rightarrow (p^2 Y(p) - py(0) - y'(0)) + (pY(p) - y(0)) - 2Y(p) = 0
\]

En remplaçant :
\[
(p^2 Y(p) - 1) + pY(p) - 2Y(p) = 0
\Rightarrow (p^2 + p - 2)Y(p) = 1
\Rightarrow Y(p) = \frac{1}{(p - 1)(p + 2)}
\]

C’est exactement la fraction qu’on vient de décomposer :
\[
Y(p) = \frac{1}{3(p - 1)} - \frac{1}{3(p + 2)}
\]

---

##### 🌀 Étape 2 – Retour dans le domaine temporel

\[
\mathcal{L}^{-1}\left\{\frac{1}{p - a}\right\} = e^{at}
\Rightarrow y(t) = \frac{1}{3}e^{t} - \frac{1}{3}e^{-2t}
\]

✅ Résultat final :
\[
\boxed{y(t) = \frac{1}{3}e^{t} - \frac{1}{3}e^{-2t}}
\]

---

---

### 🔧 **Exercice 5 – Fonction \( \cosh(t) \)**

On nous donne :
\[
y(t) = \cosh(t) = \frac{e^t + e^{-t}}{2}
\]
Et on demande :  
> Par la transformée de Laplace, déterminer une fonction égale à sa dérivée seconde.

Avec en plus :
\[
y(0) = 1 \quad \text{et} \quad y'(0) = 0
\]

---

#### 🔁 Étape 1 – Transformée de Laplace de \( \cosh(t) \)

On utilise :
\[
\mathcal{L}\{\cosh(at)\} = \frac{p}{p^2 - a^2}
\Rightarrow \boxed{\mathcal{L}\{\cosh(t)\} = \frac{p}{p^2 - 1}}
\]

---

#### 🔁 Étape 2 – On applique Laplace sur l’équation \( y'' = ? \)

On fait simplement :
\[
\mathcal{L}\{y''\} = p^2 Y(p) - p y(0) - y'(0)
= p^2 \cdot \frac{p}{p^2 - 1} - p \cdot 1 - 0
= \frac{p^3}{p^2 - 1} - p
\]

On met au même dénominateur :
\[
\frac{p^3 - p(p^2 - 1)}{p^2 - 1}
= \frac{p^3 - (p^3 - p)}{p^2 - 1}
= \frac{p}{p^2 - 1}
\]

Donc :
\[
\mathcal{L}\{y''\} = \mathcal{L}\{y\}
\Rightarrow \boxed{y'' = y}
\]

✅ Résultat : **la fonction \( \cosh(t) \) est égale à sa dérivée seconde.**

---

### 2 mini-intégrales (début Exercice 3) :

#### 🔸 I = \( \int_0^{+\infty} \cos(2t)e^{-3t} \, dt \)

On utilise :
\[
\mathcal{L}\{\cos(2t)\} = \frac{p}{p^2 + 4}
\Rightarrow I = \text{Laplace de } \cos(2t) \text{ évaluée en } p = 3
\Rightarrow \boxed{I = \frac{3}{3^2 + 4} = \frac{3}{13}}
\]

---

#### 🔸 J = \( \int_0^{+\infty} \sin(t)e^{-t} \, dt \)

On utilise :
\[
\mathcal{L}\{\sin(t)\} = \frac{1}{p^2 + 1}
\Rightarrow J = \text{Laplace de } \sin(t) \text{ en } p = 1
\Rightarrow \boxed{J = \frac{1}{1^2 + 1} = \frac{1}{2}}
\]

---
