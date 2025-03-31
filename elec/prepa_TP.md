# Préparation TP n°2 : Étude d’un convertisseur DC/DC 4 quadrants


### **1) Quel type de conversion effectue un hacheur DC/DC ?**

Un **hacheur DC/DC** est un convertisseur statique qui transforme une tension continue en une autre tension continue. Il existe plusieurs types de conversion en fonction du type :
- **Buck (abaisseur)** : Réduit la tension de sortie (Vs < Ve).
- **Boost (élévateur)** : Augmente la tension de sortie (Vs > Ve).
- **Buck-Boost** : Peut augmenter ou diminuer la tension.
- **Hacheur 4 quadrants** : Permet une inversion de polarité de la tension et du courant.

---

### **2) Différence entre un hacheur 1 quadrant et un hacheur 4 quadrants ?**
Un hacheur 1 quadrant permet uniquement un transfert d'énergie unidirectionnel, avec un courant et une tension de sortie de signes fixes (généralement positifs).
Un hacheur 4 quadrants permet un transfert d'énergie bidirectionnel, avec la possibilité d'avoir des courants et tensions de sortie positifs ou négatifs. Il peut donc fonctionner dans les quatre combinaisons possibles de signes de tension et courant.

| Type de hacheur | Tension (Vs) | Courant (Is) | Fonction |
|----------------|-------------|-------------|-----------|
| **1 Quadrant** | + | + | Un seul sens de fonctionnement (ex: moteur en marche avant) |
| **2 Quadrants** | + | ± | Fonctionnement dans un seul sens mais avec freinage |
| **4 Quadrants** | ± | ± | Propulsion et freinage dans les deux sens |

📌 **Schéma d’un hacheur 4 quadrants :**

```ascii
        Ve
         |
    T1--+--D1
     |      |
    T3--+--D3
     |      |
    T2--+--D2
     |      |
    T4--+--D4
         |
        Vs
```

---

### **3) Notion de quadrant et correspondance des grandeurs mécaniques**

- **Quadrants :**
  - **1er** : Propulsion avant
  - **2e** : Freinage avant
  - **3e** : Propulsion arrière
  - **4e** : Freinage arrière

- **Correspondance avec un moteur à courant continu :**
  - La **tension (Vs)** correspond à la **force électromotrice (FEM)**, donc proportionnelle à la vitesse de rotation.
  - Le **courant (Is)** est proportionnel au couple moteur.

# Formule fondamentale du moteur DC

## Équations de base

V = E + RₐI  
E = k · ω  
C = k · I

## Variables et constantes

| Symbole | Description                     | Unité |
|---------|---------------------------------|-----------------------|
| V       | Tension aux bornes du moteur    | Volt (V)              |
| E       | Force électromotrice (FEM)      | Volt (V)              |
| Rₐ      | Résistance de l'induit          | Ohm (Ω)               |
| I       | Courant d'induit                | Ampère (A)            |
| k       | Constante du moteur             | -                     |
| ω       | Vitesse angulaire               | rad/s                 |
| C       | Couple moteur                   | Newton-mètre (Nm)     |


La notion de quadrant correspond aux quatre combinaisons possibles des signes de la tension de sortie et du courant de sortie :

Quadrant 1 : tension positive, courant positif
Quadrant 2 : tension négative, courant positif
Quadrant 3 : tension négative, courant négatif
Quadrant 4 : tension positive, courant négatif

Dans un moteur à courant continu :

La tension induite correspond au couple électromagnétique (tension proportionnelle à la vitesse)
Le courant induit correspond au couple mécanique (courant proportionnel au couple)


---

### **4) Réversibilité d’une batterie d’accumulateurs**

- **Réversible en courant ?** OUI (peut se charger/décharger).
- **Réversible en tension ?** NON (la tension dépend de la charge, mais elle ne s’inverse pas spontanément).

Une batterie d'accumulateur est réversible en courant (elle peut se charger ou se décharger), mais pas en tension (la polarité reste fixe).

---

### **5) Réversibilité en courant dans un hacheur en pont**


La réversibilité en courant se fait par l'interrupteur K dans son ensemble.
Le transistor T permet la circulation du courant dans un sens lorsqu'il est commandé à l'état passant, tandis que la diode D permet la circulation du courant dans l'autre sens lorsque les conditions de polarisation le permettent.

---

### **6) Identification des éléments de la chaîne de conversion**

La chaîne de conversion comprend :

La source d'alimentation continue (point ①)
Le hacheur (convertisseur DC/DC) qui découpe la tension continue
Le filtre passe-bas qui lisse la tension découpée
La charge qui reçoit la tension filtrée

Formes d'onde aux différents points :

Point ② : Tension découpée (succession de créneaux entre 0 et Ve)
Point ③ : Tension filtrée mais avec une ondulation résiduelle
Point ④ : Tension de sortie lissée (quasi-continue)

---

### **7) Commande des interrupteurs K1 à K4 en charge résistive**

Pour obtenir la forme d'onde demandée avec une tension alternativement positive (E) et négative (-E), voici les configurations :
Pour Vs = +E (première partie du signal) :

K1 et K4 sont fermés (passants)
K2 et K3 sont ouverts (bloqués)
Le courant circule de la source vers la charge via K1 et K4

Pour Vs = -E (seconde partie du signal) :

K1 et K4 sont ouverts (bloqués)
K2 et K3 sont fermés (passants)
Le courant circule de la source vers la charge via K2 et K3, mais dans le sens opposé

Pour Vs = 0 (parties intermédiaires) :

Soit K1 et K3 sont fermés (court-circuitant la charge)
Soit K2 et K4 sont fermés (court-circuitant également la charge)

| Phase du signal | Tension de sortie | État des interrupteurs | Composants conducteurs | Chemin du courant |
|-----------------|-------------------|------------------------|-----------------------|-------------------|
| Phase 1 | Vs = +E | K1: ON, K2: OFF<br>K3: OFF, K4: ON | T1 et T4 (si courant positif)<br>D1 et D4 (si courant négatif) | Source → K1 → Charge → K4 → Source |
| Phase 2 | Vs = 0 | K1: ON, K2: OFF<br>K3: ON, K4: OFF | T1 et T3 (court-circuit) | Court-circuit du haut de la charge |
| Phase 3 | Vs = -E | K1: OFF, K2: ON<br>K3: ON, K4: OFF | T2 et T3 (si courant positif)<br>D2 et D3 (si courant négatif) | Source → K3 → Charge → K2 → Source |
| Phase 4 | Vs = 0 | K1: OFF, K2: ON<br>K3: OFF, K4: ON | T2 et T4 (court-circuit) | Court-circuit du bas de la charge |

**Note importante :** Pour éviter un court-circuit de la source, il ne faut jamais activer simultanément K1 et K2, ou K3 et K4. Un "temps mort" est généralement introduit entre les commutations pour éviter tout risque de court-circuit.


---

# Questions sur la simulation BUCK sous PSIM
1) Avec un rapport cyclique ALPHA = 0,5
Avec α = 0,5, la tension de sortie moyenne vaut théoriquement Vs = α × Ve = 0,5 × Ve.
Les tensions observées devraient montrer :

Ve : tension d'entrée constante
VD : tension inverse aux bornes de la diode (Ve quand T1 conduit, 0 quand D conduit)
Vs : tension de sortie découpée qui alterne entre Ve (quand T1 conduit) et 0 (quand D conduit)

2) Formes d'ondes des courants

I(Charge) : courant dans la charge, relativement constant avec une ondulation
I(L) : courant dans l'inductance, avec une ondulation triangulaire
I(T1) : courant dans le transistor, non nul uniquement pendant sa période de conduction (αT)
I(D1) : courant dans la diode, non nul uniquement pendant la période de conduction de la diode ((1-α)T)

3) Influence du rapport cyclique (α = 0,3 et α = 0,7)
Pour α = 0,3 : La tension moyenne de sortie sera Vs = 0,3 × Ve
Pour α = 0,7 : La tension moyenne de sortie sera Vs = 0,7 × Ve
Plus le rapport cyclique augmente, plus la tension moyenne de sortie est élevée. Dans un hacheur Buck, la relation est linéaire : Vs = α × Ve.
4) Rôle du condensateur C
Le condensateur C placé en parallèle avec la charge a pour rôle de :

Réduire l'ondulation de la tension de sortie (lissage)
Maintenir une tension plus stable aux bornes de la charge
Réduire l'ondulation du courant de sortie

Sans condensateur, la tension de sortie présente une ondulation plus importante. Avec le condensateur, la tension de sortie est beaucoup plus lisse et se rapproche davantage d'une tension continue pure.








---
---
---

## Explications supplémentaires pour la simulation BUCK

### 1) Rapport cyclique ALPHA = 0,5

**Explication des formes d'onde :**
- **Ve** : Tension continue d'entrée, constante tout au long de la simulation.
- **VD** : Tension aux bornes de la diode :
  * Vaut Ve quand T1 conduit (diode bloquée) car la tension aux bornes de la diode est égale à la tension d'entrée
  * Vaut approximativement 0V (en réalité -Vf avec Vf la tension de seuil) quand la diode conduit
- **Vs** : Tension de sortie avant filtrage :
  * Vaut Ve pendant αT (quand T1 conduit)
  * Vaut 0V pendant (1-α)T (quand D1 conduit)
  * Sa valeur moyenne théorique est Vs = α × Ve = 0,5 × Ve

### 2) Formes d'onde des courants

- **I(L)** : Courant dans l'inductance :
  * Forme d'onde triangulaire due à l'application d'une tension constante aux bornes de l'inductance (dI/dt = V/L)
  * Quand T1 conduit : pente positive car VL = Ve - Vs
  * Quand D1 conduit : pente négative car VL = -Vs
  * L'ondulation du courant ΔI = (Ve × α × (1-α))/(L × f) où f est la fréquence de découpage

- **I(T1)** : Courant dans le transistor :
  * Non nul uniquement pendant la période de conduction du transistor (αT)
  * Égal au courant dans l'inductance pendant cette période

- **I(D1)** : Courant dans la diode :
  * Non nul uniquement pendant la période de conduction de la diode ((1-α)T)
  * Égal au courant dans l'inductance pendant cette période

- **I(Charge)** : Courant dans la charge :
  * Forme d'onde avec ondulation triangulaire comme I(L)
  * Si la charge est purement résistive : I(Charge) = Vs/R

### 3) Influence du rapport cyclique

La relation entre le rapport cyclique α et la tension de sortie moyenne dans un hacheur Buck est :

Vs = α × Ve

**Pour α = 0,3 :**
- Vs = 0,3 × Ve
- Le transistor conduit pendant 30% de la période
- La diode conduit pendant 70% de la période
- L'ondulation de courant est proportionnelle à α × (1-α), soit 0,3 × 0,7 = 0,21

**Pour α = 0,7 :**
- Vs = 0,7 × Ve
- Le transistor conduit pendant 70% de la période
- La diode conduit pendant 30% de la période
- L'ondulation de courant est proportionnelle à α × (1-α), soit 0,7 × 0,3 = 0,21

**Remarque :** L'ondulation de courant est maximale pour α = 0,5 et diminue pour des valeurs s'éloignant de 0,5.

### 4) Rôle du condensateur C

Le condensateur joue plusieurs rôles essentiels :

1. **Réduction de l'ondulation de tension :**
   - L'ondulation de tension est donnée par : ΔV = ΔI/(8 × f × C)
   - Plus la capacité est grande, plus l'ondulation est faible

2. **Stockage d'énergie :**
   - Le condensateur stocke l'énergie pendant la phase de conduction du transistor
   - Il restitue cette énergie à la charge pendant la phase de conduction de la diode

3. **Filtrage des harmoniques :**
   - Avec l'inductance, il forme un filtre LC passe-bas qui atténue les harmoniques de découpage
   - La fréquence de coupure est fc = 1/(2π√(LC))

4. **Stabilisation de la tension :**
   - Il maintient une tension plus stable aux bornes de la charge, particulièrement lors des variations de charge

Sans condensateur, la tension de sortie présente une ondulation importante qui peut affecter le fonctionnement de la charge. Avec le condensateur, la tension devient quasi-continue, ce qui est généralement souhaitable pour alimenter des circuits électroniques sensibles.