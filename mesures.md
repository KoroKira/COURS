Voici le tableau final complété pour **l'expansion**, **la contraction**, et les **coudes**, basé sur les données et formules fournies. Les valeurs de \( K_{L_{emp}} \) sont tirées des annexes (Figure 4 et Figure 5).

---

### **Explications des calculs :**
1. **Vitesse (\( V \)) :**
   - Calculée avec \( V = \frac{Q_v}{A} \), où \( A = \frac{\pi D^2}{4} \).
   - **Expansion/Contraction :** \( D = 14 \, \text{mm} \) (entrée/sortie respectivement).
   - **Coudes :** \( D = 15 \, \text{mm} \).

2. **Pertes de pression (\( J_{L_{exp}} \)) :**
   - \( J_{L_{exp}} = \rho g \Delta h \) avec \( \Delta h \) mesuré entre les points indiqués.

3. **Coefficients \( K_{L_{emp}} \) :**
   - **Expansion :** \( K_L = 0.6 \) (Figure 4, \( A_1/A_2 = 0.17 \)).
   - **Contraction :** \( K_L = 0.44 \) (Figure 4, \( A_1/A_2 = 0.17 \)).
   - **Coudes :** Valeurs de la Figure 5 (ex. \( 90^\circ \) petit rayon = 1.5, \( 135^\circ = 3 \)).

4. **Pertes empiriques (\( J_{L_{emp}} \)) :**
   - \( J_{L_{emp}} = K_{L_{emp}} \cdot \frac{1}{2} \rho V^2 \).

---


- Les **écarts entre \( J_{L_{exp}} \) et \( J_{L_{emp}} \)** peuvent s'expliquer par des approximations des \( K_L \) ou des pertes non idéales.
- Pour les **coudes**, \( K_L \) dépend du rayon et de l'angle (Figure 5).



Pour compléter le tableau, voici les calculs que vous devez effectuer pour chaque composant (expansion, contraction, et les différents coudes) et pour chaque débit (400, 450, 500, 550 L/h). Les étapes sont les suivantes :

---

### **1. Calcul de la vitesse \( V \) (m/s)**
La vitesse est calculée à l'entrée ou à la sortie selon le composant, comme indiqué dans les consignes. Utilisez la formule :
\[
V = \frac{Q_v}{A}
\]
où :
- \( Q_v \) est le débit volumique en \( m^3/s \) (convertir \( L/h \) en \( m^3/s \) : \( Q_v (m^3/s) = Q_v (L/h) \times \frac{1}{3600} \times 10^{-3} \)).
- \( A \) est la section transversale du tuyau en \( m^2 \) :
  - Pour les diamètres \( D_1 = 14 \, \text{mm} \) et \( D_2 = 34 \, \text{mm} \), calculez \( A = \pi \left(\frac{D}{2}\right)^2 \).

**Exemple pour l'expansion (diamètre \( D_1 = 14 \, \text{mm} \)) :**
\[
A_1 = \pi \left(\frac{14 \times 10^{-3}}{2}\right)^2 \approx 1.54 \times 10^{-4} \, m^2
\]
\[
V = \frac{400 \times \frac{1}{3600} \times 10^{-3}}{1.54 \times 10^{-4}} \approx 0.72 \, m/s
\]

---

### **2. Calcul de la perte de pression expérimentale \( J_{L_{exp}} \) (Pa)**
Utilisez la formule :
\[
J_{L_{exp}} = \rho g \Delta h
\]
où :
- \( \rho = 1000 \, kg/m^3 \) (masse volumique de l'eau),
- \( g = 9.81 \, m/s^2 \),
- \( \Delta h \) est la différence de hauteur en mètres (convertir cm en m).

**Exemple pour l'expansion (9-10) à 400 L/h :**
\[
\Delta h = h_{10} - h_9 = 45 - 44.5 = 0.5 \, cm = 0.005 \, m
\]
\[
J_{L_{exp}} = 1000 \times 9.81 \times 0.005 = 49.05 \, Pa
\]

---

### **3. Calcul du coefficient de perte expérimental \( K_{L_{exp}} \) (-)**
Utilisez la formule :
\[
K_{L_{exp}} = \frac{2 J_{L_{exp}}}{\rho V^2}
\]
**Exemple pour l'expansion à 400 L/h :**
\[
K_{L_{exp}} = \frac{2 \times 49.05}{1000 \times (0.72)^2} \approx 0.19
\]

---

### **4. Détermination du coefficient de perte empirique \( K_{L_{emp}} \) (-)**
- **Expansion/Contraction** : Utilisez les figures 4 ou les formules données (par exemple, pour l'expansion, \( K_L \) dépend du rapport des sections \( A_1/A_2 \)).
  - Pour \( D_1 = 14 \, \text{mm} \) et \( D_2 = 34 \, \text{mm} \), \( A_1/A_2 = (14/34)^2 \approx 0.17 \). Selon la figure 4 (bas), \( K_L \approx 0.6 \).
- **Coudes** : Utilisez les valeurs de la figure 5 (par exemple, coude \( 90^\circ \) petit rayon : \( K_L = 1.5 \)).

---

### **5. Calcul de la perte de pression empirique \( J_{L_{emp}} \) (Pa)**
Utilisez la formule :
\[
J_{L_{emp}} = K_{L_{emp}} \times \frac{1}{2} \rho V^2
\]
**Exemple pour l'expansion à 400 L/h :**
\[
J_{L_{emp}} = 0.6 \times \frac{1}{2} \times 1000 \times (0.72)^2 \approx 155.52 \, Pa
\]

---

### **Résumé des étapes pour chaque composant et débit :**
1. Convertir \( Q_v \) en \( m^3/s \).
2. Calculer \( V \) avec \( V = Q_v / A \).
3. Calculer \( \Delta h \) (différence de hauteur entre les points du composant).
4. Calculer \( J_{L_{exp}} = \rho g \Delta h \).
5. Calculer \( K_{L_{exp}} = \frac{2 J_{L_{exp}}}{\rho V^2} \).
6. Trouver \( K_{L_{emp}} \) via les figures/tableaux.
7. Calculer \( J_{L_{emp}} = K_{L_{emp}} \times \frac{1}{2} \rho V^2 \).

---

### **Exemple complet pour l'expansion à 400 L/h :**
| Composant | \( Q_v \) (L/h) | \( V \) (m/s) | \( \Delta h \) (cm) | \( J_{L_{exp}} \) (Pa) | \( K_{L_{exp}} \) (-) | \( K_{L_{emp}} \) (-) | \( J_{L_{emp}} \) (Pa) |
|-----------|-----------------|---------------|---------------------|------------------------|-----------------------|-----------------------|------------------------|
| Expansion | 400             | 0.72          | 0.5                 | 49.05                  | 0.19                  | 0.6                   | 155.52                 |

Répétez ces calculs pour tous les composants et débits.