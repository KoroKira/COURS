DC Motors: principles, applications and sizing

## Introduction

Laplace Law

> Conductor
> Eletric current
> Magnetic field
> Perpendicular Force

Electromagnetic force: F in newton [N]

F = BIL sin(alpha)

B: Flux density [T]
I: Current [A]
L: Length of conductor [m]
alpha: Angle between B and I [rad]

Règle des 3 doigts (encore)

---

### Exercice wooclap:

Détermine the electromagnetc force F which is applied on the iron bar (L=1,5m) fowing a current equal to 200A. The bar is located into a magnetic field produced by a permanent magnet with a flux density B=0,5T.

1. When the bar is perpendicular to the magnetic field ?

2. When the bar is parallel to the magnetic field ?


To determine the electromagnetic force \( F \) applied on the iron bar, we use the formula for the force on a current-carrying conductor in a magnetic field:

\[
F = I \cdot L \cdot B \cdot \sin(\theta)
\]

where:
- \( I \) is the current (200 A),
- \( L \) is the length of the bar (1.5 m),
- \( B \) is the magnetic flux density (0.5 T),
- \( \theta \) is the angle between the direction of the current and the magnetic field.

### 1. When the bar is perpendicular to the magnetic field (\( \theta = 90^\circ \)):
\[
\sin(90^\circ) = 1
\]
\[
F = I \cdot L \cdot B \cdot \sin(90^\circ) = 200 \cdot 1.5 \cdot 0.5 \cdot 1 = 150 \, \text{N}
\]

### 2. When the bar is parallel to the magnetic field (\( \theta = 0^\circ \)):
\[
\sin(0^\circ) = 0
\]
\[
F = I \cdot L \cdot B \cdot \sin(0^\circ) = 200 \cdot 1.5 \cdot 0.5 \cdot 0 = 0 \, \text{N}
\]

### Answers:
1. **150 N** (when perpendicular)
2. **0 N** (when parallel)

NB: The force is maximum when the bar is perpendicular to the magnetic field, and null when it is parallel.

---

Motors are electrical machines convert electrical energies into mechanical energies and inversely: reversibility.

![Schemas](img/info1.png)

---
### Quick history

The DC machine is the first electric motor (around 1870 by Zenobe Gramme).
Used as a motor or generator.
Their use is in very clear decline, especially as a generator.
Although the DC motor is older, it remains competitive in some applications (robotics, light traction, etc.).


| Advantages                                      | Disadvantages                              |
|-------------------------------------------------|--------------------------------------------|
| DC supply                                       | High maintenance cost (brushes and commutator) |
| Traction systems for driving heavy loads        | Reliability                                |
| High starting torque (series connection)        |                                            |
| Wide range of speed control                     |                                            |
| DC motors are free from harmonics, reactive power consumption |                                            |
| Easy to control                                 |                                            |

# Nameplate of a DC machine
![Nameplate of a DC machine](img/info2.png)

---

# Constitution of a DC machine - overview
![Constitution of a DC machine - overview](img/info3.png)

---

# Constitution of a DC machine - Stator
![Constitution of a DC machine - Stator](img/info4.png)

---

# Constitution of a DC machine - Rotor
![Constitution of a DC machine - Rotor](img/info5.png)

---

# Constitution of a DC machine
![Constitution of a DC machine](img/info6.png)

---

# DC Motor Operation
![DC Motor Operation](img/info7.png)
![DC Motor Operation](img/info8.png)
![DC Motor Operation](img/info9.png)

---

# Creation of an electromotive force (EMF)
![Creation of an electromotive force (EMF)](img/info10.png)

---

# Equivalent circuit
![Equivalent circuit](img/info11.png)

---

# Equivalent circuit - steady state
![Equivalent circuit - steady state](img/info12.png)

---

# Electromagnetic power - Pem
![Electromagnetic power - Pem](img/info13.png)

---

# Power flow diagram in DC Machine
![Power flow diagram in DC Machine](img/info14.png)
![Power flow diagram in DC Machine](img/info15.png)
![Power flow diagram in DC Machine](img/info16.png)

---

# Control of the rotating speed
![Control of the rotating speed](img/info17.png)

---

# Electrical/Mechanical Evolution - Motor
![Electrical/Mechanical Evolution - Motor](img/info18.png)
![Electrical/Mechanical Evolution - Motor](img/info19.png)

---

# Control of the rotating speed
![Control of the rotating speed](img/info20.png)


#### **1) Calcul de la force électromotrice (fem) \( E \) du moteur :**

La relation tension-fem dans un moteur à courant continu est donnée par :  
\[
U_i = E + R_i \cdot I
\]  
où :  
- \( U_i = 220 \, \text{V} \) (tension d’alimentation),  
- \( R_i = 0,8 \, \Omega \) (résistance d’induit),  
- \( I = 15 \, \text{A} \) (courant d’induit).  

On isole \( E \) :  
\[
E = U_i - R_i \cdot I = 220 - (0,8 \times 15) = 220 - 12 = 208 \, \text{V}
\]  

**Réponse :**  
\[
\boxed{208 \, \text{V}}
\]  

---

#### **2) Calcul de la puissance électromagnétique \( P_{em} \) du moteur :**

La puissance électromagnétique est donnée par :  
\[
P_{em} = E \cdot I
\]  
où :  
- \( E = 208 \, \text{V} \),  
- \( I = 15 \, \text{A} \).  

Calcul :  
\[
P_{em} = 208 \times 15 = 3120 \, \text{W}
\]  

**Réponse :**  
\[
\boxed{3120 \, \text{W}}
\]  

---

### **Récapitulatif :**
1. **Fem \( E \)** : \( \boxed{208 \, \text{V}} \)  
2. **Puissance électromagnétique \( P_{em} \)** : \( \boxed{3120 \, \text{W}} \)


---

# Different types of loads ?
![Different types of loads ?](img/info21.png)

---

# Excitation coupling of DC motors
![Excitation coupling of DC motors](img/info22.png)
![Excitation coupling of DC motors](img/info23.png)
![Excitation coupling of DC motors](img/info24.png)
![Excitation coupling of DC motors](img/info25.png)
![Excitation coupling of DC motors](img/info26.png)
![Excitation coupling of DC motors](img/info27.png)


---
---
---

# AC motors - induction motors

Un peu d’histoire …
Moteur asynchrone ou « moteur d’induction »
inventé par Nikola Tesla vers 1890 aux USA
❖ Machine alternative tournante
❖ Robuste, économique, facile d’entretien
❖ ~70 % des moteurs utilisés (industrie)
❖ Plage de puissance : 100 W à 25 MW
❖ Variation de vitesse par variateur de fréquence
Principalement utilisé pour des applications d’entrainements à vitesse constante, il est
possible de l’utiliser pour de la variation de vitesse en utilisant des alimentations
électroniques de puissance à fréquence variable.

Ex d’applications : pompes, ventilateurs, compresseurs,…

![AC motors - induction motors](img/info28.png)
![AC motors - induction motors](img/info29.png)

---

# Composition d’un moteur asynchrone

![Composition d’un moteur asynchrone](img/info30.png)
![Composition d’un moteur asynchrone](img/info31.png)

---

# Champs tournants

![Champs tournants](img/info32.png)
![Champs tournants](img/info33.png)
![Champs tournants](img/info34.png)
![Champs tournants](img/info35.png)
![Champs tournants](img/info36.png)
![Champs tournants](img/info37.png)
![Champs tournants](img/info38.png)
![Champs tournants](img/info39.png)

---

# Composition du rotor

![Composition du rotor](img/info40.png)

---

# Interaction stator/rotor

![Interaction stator/rotor](img/info41.png)
![Interaction stator/rotor](img/info42.png)

---

# Notions de glissement

![Notions de glissement](img/info43.png)
![Notions de glissement](img/info44.png)

Au démarrage, glissement = 1
glissement évolue entre 0.02 et 0.05 de nS
autre truc que j'ai pas pu noter


---

# Nb poles Vs. Vitesse de synchronisme

![Nb poles Vs. Vitesse de synchronisme](img/info45.png)
3000 / 1500 / 750

---

# Schéma equivalent monophase MAS

![Schéma equivalent monophase MAS](img/info46.png)
![Schéma equivalent monophase MAS](img/info47.png)
![Schéma equivalent monophase MAS](img/info48.png)

---

# Bilan de puissance

![Bilan de puissance](img/info49.png)
![Bilan de puissance](img/info50.png)

---

# Fonctionnement à tension/fréquence cst

![Fonctionnement à tension/fréquence cst](img/info51.png)

---

# Caractéristique couple/vitesse

![Caractéristique couple/vitesse](img/info52.png)
![Caractéristique couple/vitesse](img/info53.png)

---

# Démarrage direct de la MAS

![Démarrage direct de la MAS](img/info54.png)
![Démarrage direct de la MAS](img/info55.png)
![Démarrage direct de la MAS](img/info56.png)

---

# Variation de vitesse de la MAS

![Variation de vitesse de la MAS](img/info57.png)
![Variation de vitesse de la MAS](img/info58.png)
![Variation de vitesse de la MAS](img/info59.png)
