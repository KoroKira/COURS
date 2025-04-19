# 🧠 Fiche de Révision – Transformée de Laplace & Équations Différentielles

---

## 🔷 Formules essentielles – Table de Laplace

| Fonction \( f(t) \) | \( \mathcal{L}\{f(t)\} \)         |
|---------------------|-----------------------------------|
| \( 1 \)             | \( \frac{1}{p} \)                 |
| \( t \)             | \( \frac{1}{p^2} \)               |
| \( t^n \)           | \( \frac{n!}{p^{n+1}} \)          |
| \( e^{at} \)        | \( \frac{1}{p - a} \)             |
| \( \sin(at) \)      | \( \frac{a}{p^2 + a^2} \)         |
| \( \cos(at) \)      | \( \frac{p}{p^2 + a^2} \)         |
| \( \sinh(at) \)     | \( \frac{a}{p^2 - a^2} \)         |
| \( \cosh(at) \)     | \( \frac{p}{p^2 - a^2} \)         |

---

## 🔁 Transformées des dérivées

- \( \mathcal{L}\{y'\} = pY(p) - y(0) \)
- \( \mathcal{L}\{y''\} = p^2Y(p) - py(0) - y'(0) \)

---

## 🛠️ Méthode générale pour résoudre une EDO

1. Appliquer \( \mathcal{L} \) à l'équation
2. Incorporer les conditions initiales
3. Isoler \( Y(p) \)
4. Décomposer (fractions simples)
5. Inverser avec la table

---

## 🧮 Intégrales généralisées

\[
\int_0^{+\infty} f(t) e^{-at} \, dt = \mathcal{L}\{f(t)\}\Big|_{p = a}
\]

---

# 📘 Exercices types et résolus

---

### ✅ Exercice 1 – EDO 1er ordre

\[
y' + 2y = 3,\quad y(0) = 1
\]
Transformée :
\[
Y(p) = \frac{3 + p}{p(p + 2)}
\]
Décomposition :
\[
Y(p) = \frac{3}{2}\cdot\frac{1}{p} - \frac{1}{2}\cdot\frac{1}{p+2}
\]
Résultat :
\[
\boxed{y(t) = \frac{3}{2} - \frac{1}{2}e^{-2t}}
\]

---

### ✅ Exercice 2 – EDO 2ème ordre

\[
y'' - 2y' - 8y = 0,\quad y(0) = 0,\; y'(0) = 1
\]
\[
Y(p) = \frac{1}{(p - 4)(p + 2)} \Rightarrow y(t) = \frac{1}{6}e^{4t} - \frac{1}{6}e^{-2t}
\]
\[
\boxed{y(t) = \frac{1}{6}e^{4t} - \frac{1}{6}e^{-2t}}
\]

---

### ✅ Exercice 3 – Intégrale par Laplace

\[
I = \int_0^{+\infty} \sin(4t)e^{-3t} \, dt = \mathcal{L}\{\sin(4t)\}\big|_{p = 3} = \frac{4}{25}
\]
\[
\boxed{I = \frac{4}{25}}
\]

---

### ✅ Exercice 4 – EDO avec sinus

\[
y'' + 4y = 0,\quad y(0) = 0,\quad y'(0) = 1
\]
\[
Y(p) = \frac{1}{p^2 + 4} \Rightarrow y(t) = \frac{1}{2}\sin(2t)
\]
\[
\boxed{y(t) = \frac{1}{2}\sin(2t)}
\]

---

### ✅ Exercice 5 – Fonction \( \cosh(t) \)

\[
y(t) = \cosh(t) = \frac{e^t + e^{-t}}{2}
\Rightarrow y'' = y
\]
\[
\boxed{y'' = y}
\]

---

### ✅ Exercice 6 – Système différentiel

\[
\begin{cases}
x' = x - y \\
y' = -x + y
\end{cases} \quad x(0) = y(0) = 1
\]
\[
\Rightarrow x(t) = y(t) = 1
\]
\[
\boxed{x(t) = y(t) = 1}
\]

---

### ✅ Exercice bonus – EDO mixte

\[
4y' - y = 1,\quad y(0) = 1
\Rightarrow Y(p) = \frac{1 + 4p}{p(4p - 1)}
\]
Décomposition :
\[
Y(p) = -\frac{1}{p} + \frac{4}{4p - 1} \Rightarrow y(t) = -1 + e^{\frac{1}{4}t}
\]
\[
\boxed{y(t) = -1 + e^{\frac{1}{4}t}}
\]

---

