# Réponses détaillées aux exercices sur les transformateurs

---

## **Exercice 1 : Transformateur ferroviaire monophasé**

### **1. Nombre de spires du primaire \(N_1\)**
**Formule utilisée** :  
\[
N_1 = \frac{U_1}{4.44 \cdot f \cdot B_m \cdot S_{\text{fer}}}
\]  
**Explication** :  
Cette formule découle de la relation fondamentale des transformateurs où la tension induite (\(U_1\)) est proportionnelle au flux magnétique (\(B_m \cdot S_{\text{fer}}\)) et à la fréquence (\(f\)).  
**Application** :  
- \(U_1 = 20\,000\ \text{V}\), \(f = 50\ \text{Hz}\), \(B_m = 1.1\ \text{T}\), \(S_{\text{fer}} = 5\ \text{dm}^2 = 0.05\ \text{m}^2\).  
- Calcul :  
\[
N_1 = \frac{20\,000}{4.44 \cdot 50 \cdot 1.1 \cdot 0.05} \approx \boxed{1637\ \text{spires}}
\]  
**Remarque** : Le coefficient \(4.44\) provient de la forme sinusoïdale du flux.

---

### **2. Nombre de spires du secondaire \(N_2\)**
**Formule utilisée** :  
\[
N_2 = N_1 \cdot \frac{U_2}{U_1}
\]  
**Explication** :  
Le rapport de transformation (\(m = \frac{U_2}{U_1}\)) est égal au rapport des spires (\(m = \frac{N_2}{N_1}\)).  
**Application** :  
- \(U_2 = 230\ \text{V}\), \(N_1 = 1637\).  
- Calcul :  
\[
N_2 = 1637 \cdot \frac{230}{20\,000} \approx \boxed{19\ \text{spires}}
\]  
**Remarque** : Un faible nombre de spires au secondaire est cohérent pour un transformateur dévolteur.

---

### **3. Puissances primaires et secondaires**
#### **Secondaire** :
- **Puissance apparente (\(S_2\))** :  
\[
S_2 = U_2 \cdot I_2 = 230 \cdot 150 = \boxed{34.5\ \text{kVA}}
\]  
- **Puissance active (\(P_2\))** :  
\[
P_2 = S_2 \cdot \cos(\alpha) = 34.5 \cdot 0.9 = \boxed{31.05\ \text{kW}}
\]  
- **Puissance réactive (\(Q_2\))** :  
\[
Q_2 = S_2 \cdot \sin(\alpha) = 34.5 \cdot \sqrt{1 - 0.9^2} \approx \boxed{15.03\ \text{kVAR}}
\]  

#### **Primaire** (transformateur idéal) :  
- \(S_1 = S_2 = \boxed{34.5\ \text{kVA}}\), \(P_1 = \boxed{31.05\ \text{kW}}\), \(Q_1 = \boxed{15.03\ \text{kVAR}}\).

---

### **4. Courant primaire \(I_1\)**
**Formule utilisée** :  
\[
I_1 = \frac{S_1}{U_1}
\]  
**Application** :  
\[
I_1 = \frac{34\,500}{20\,000} = \boxed{1.725\ \text{A}}
\]  
**Remarque** : Le courant primaire est faible car la tension est élevée.

---

## **Exercice 4 : Transformateur 230V/24V**

### **1. Résistance primaire \(R_1\)**
**Formule utilisée** :  
\[
R_1 = \frac{U_{\text{DC}}}{I_{\text{DC}}}
\]  
**Explication** :  
En courant continu, l'inductance n'intervient pas.  
**Application** :  
- \(U_{\text{DC}} = 2.40\ \text{V}\), \(I_{\text{DC}} = 0.95\ \text{A}\).  
\[
R_1 = \frac{2.40}{0.95} \approx \boxed{2.53\ \Omega}
\]  

---

### **2. Essai à vide**
#### **Rapport de transformation (\(m\))** :  
\[
m = \frac{U_{2V}}{U_1} = \frac{24.5}{230} \approx \boxed{0.106}
\]  

#### **Pertes Joule à vide (\(P_{JV}\))** :  
\[
P_{JV} = R_1 \cdot I_{1V}^2 = 2.53 \cdot (0.08)^2 \approx \boxed{0.016\ \text{W}}
\]  

#### **Pertes fer (\(P_{\text{fer}}\))** :  
\[
P_{\text{fer}} = P_{1V} - P_{JV} = 4 - 0.016 \approx \boxed{3.98\ \text{W}}
\]  
**Conclusion** : Les pertes fer dominent à vide (typique pour un transformateur).

---

### **3. Essai en court-circuit**
#### **Résistance totale ramenée au secondaire (\(R_S\))** :  
\[
R_S = \frac{P_{1CC}}{I_{2N}^2}
\]  
**Application** :  
- \(I_{2N} = \frac{I_{1CC}}{m} = \frac{0.91}{0.106} \approx 8.58\ \text{A}\).  
\[
R_S = \frac{5.1}{(8.58)^2} \approx \boxed{0.073\ \Omega}
\]  

#### **Réactance totale ramenée au secondaire (\(X_S\))** :  
\[
X_S = \sqrt{\left(\frac{U_{1CC}}{I_{1CC}} \cdot m^2\right)^2 - R_S^2}
\]  
**Application** :  
\[
X_S = \sqrt{\left(\frac{8.6}{0.91} \cdot (0.106)^2\right)^2 - (0.073)^2} \approx \boxed{0.078\ \Omega}
\]  

---

### **4. Tension secondaire en charge et rendement**
#### **Chute de tension (\(\Delta U\))** :  
\[
\Delta U = I_2 \cdot (R_S \cdot \cos\varphi + X_S \cdot \sin\varphi)
\]  
- \(I_2 = 8.3\ \text{A}\), \(\cos\varphi = 0.8\), \(\sin\varphi = 0.6\).  
\[
\Delta U = 8.3 \cdot (0.073 \cdot 0.8 + 0.078 \cdot 0.6) \approx 0.876\ \text{V}
\]  
- **Tension \(U_2\)** :  
\[
U_2 = U_{2V} - \Delta U = 24.5 - 0.876 \approx \boxed{23.6\ \text{V}}
\]  

#### **Rendement (\(\eta\))** :  
\[
\eta = \frac{P_2}{P_2 + \text{Pertes}} = \frac{23.6 \cdot 8.3 \cdot 0.8}{23.6 \cdot 8.3 \cdot 0.8 + 3.98 + 5.1} \approx \boxed{94.5\%}
\]  

---

## **Exercice 7 : Transformateur triphasé**

### **1. Courant nominal secondaire \(I_{2N}\)**
**Formule utilisée** :  
\[
I_{2N} = \frac{S_{2N}}{\sqrt{3} \cdot U_{2N}}
\]  
**Application** :  
\[
I_{2N} = \frac{250\,000}{\sqrt{3} \cdot 400} \approx \boxed{360.86\ \text{A}}
\]  

---

### **2. Rapport de transformation (\(m\))**
**Formule utilisée** :  
\[
m = \frac{U_{2\text{ph}}}{U_{1\text{ph}}} = \frac{400/\sqrt{3}}{20\,000/\sqrt{3}} = \frac{400}{20\,000} = \boxed{0.02}
\]  

---

### **3. Impédance \(Z_S\)**
#### **Résistance (\(R_S\))** :  
\[
R_S = \frac{P_{1CC}}{3 \cdot I_{2N}^2} = \frac{3\,250}{3 \cdot (360.86)^2} \approx \boxed{8.3\ \text{m}\Omega}
\]  

#### **Réactance (\(X_S\))** :  
\[
X_S = \sqrt{\left(\frac{U_{1CC}/\sqrt{3}}{I_{2N}}\right)^2 - R_S^2} \approx \boxed{25\ \text{m}\Omega}
\]  

---

### **4. Tension de charge et rendement**
#### **Tension ligne** :  
\[
\Delta U_{\text{phase}} = I_{2N} \cdot (R_S \cdot \cos\varphi + X_S \cdot \sin\varphi) \approx 8.4\ \text{V}
\]  
\[
U_{\text{ligne}} = 400 - \sqrt{3} \cdot \Delta U_{\text{phase}} \approx \boxed{396.7\ \text{V}}
\]  

#### **Rendement (\(\eta\))** :  
\[
\eta = \frac{P_2}{P_2 + \text{Pertes}} = \frac{200\,000}{200\,000 + 3\,900} \approx \boxed{98.1\%}
\]  

---

**Conclusion générale** :  
Les calculs respectent les principes électromagnétiques des transformateurs. Les approximations et hypothèses (comme le transformateur idéal pour l'exercice 1) sont justifiées par les données fournies. Les écarts mineurs proviennent des arrondis numériques.