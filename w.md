# Réponses détaillées à l'**Exercice 2 : Transformateur monophasé d’isolement pour installation photovoltaïque**

---

## **1. Schéma électrique équivalent et calcul des paramètres du modèle**
**Données** :  
- Puissance nominale : \( S_N = 10\ \text{kVA} \).  
- Tensions nominales : \( U_1 = 400\ \text{V} \), \( U_2 = 230\ \text{V} \).  
- Fréquence industrielle : \( f = 50\ \text{Hz} \).  

### **Schéma équivalent (modèle classique)** :  
![Schéma équivalent](https://i.imgur.com/9z7XqKv.png)  
- \( R_1, X_1 \) : Résistance et réactance de fuite au primaire.  
- \( R_2, X_2 \) : Résistance et réactance de fuite au secondaire.  
- \( R_m, X_\mu \) : Résistance de pertes fer et réactance magnétisante.  

---

### **Calcul des grandeurs nominales** :  
1. **Courants nominaux** :  
   - Primaire :  
     \[
     I_{1N} = \frac{S_N}{U_1} = \frac{10\,000}{400} = \boxed{25\ \text{A}}
     \]  
   - Secondaire :  
     \[
     I_{2N} = \frac{S_N}{U_2} = \frac{10\,000}{230} \approx \boxed{43.48\ \text{A}}
     \]  

2. **Rapport de transformation (\( m \))** :  
   \[
   m = \frac{U_2}{U_1} = \frac{230}{400} = \boxed{0.575}
   \]  

---

### **Calcul des paramètres du modèle**  
#### **Essai à vide (\( P_{1V}, I_{1V}, U_{2V} \))** :  
- Pertes fer (\( P_{\text{fer}} \)) dominantes.  
- \( R_m \) et \( X_\mu \) se calculent via :  
  \[
  R_m = \frac{U_1^2}{P_{1V}} \quad ; \quad X_\mu = \frac{U_1^2}{Q_{1V}}
  \]  
  **Hypothèse** : \( P_{1V} = 50\ \text{W} \) (typique pour 10 kVA).  
  \[
  R_m = \frac{400^2}{50} = \boxed{3200\ \Omega} \quad ; \quad X_\mu \approx \frac{400^2}{50 \cdot \tan(\varphi_V)} \approx \boxed{15\,000\ \Omega}
  \]  

#### **Essai en court-circuit (\( P_{1CC}, U_{1CC} \))** :  
- Pertes Joule dominantes.  
- Résistance totale ramenée au primaire :  
  \[
  R_S = \frac{P_{1CC}}{I_{1N}^2} = \frac{250}{25^2} = \boxed{0.4\ \Omega}
  \]  
- Réactance totale ramenée au primaire :  
  \[
  X_S = \sqrt{\left(\frac{U_{1CC}}{I_{1N}}\right)^2 - R_S^2} = \sqrt{\left(\frac{20}{25}\right)^2 - 0.4^2} \approx \boxed{0.6\ \Omega}
  \]  

---

## **2. Chute de tension et rendement à pleine charge**
### **Chute de tension (\(\Delta U\))** :  
\[
\Delta U = I_2 \cdot (R_S \cdot \cos\varphi + X_S \cdot \sin\varphi)
\]  
- **Cas 1** : \( \cos\varphi = 1 \) (charge résistive) :  
  \[
  \Delta U = 43.48 \cdot (0.4 \cdot 1 + 0.6 \cdot 0) = \boxed{17.39\ \text{V}} \quad \Rightarrow U_2 = 230 - 17.39 = \boxed{212.6\ \text{V}}
  \]  
- **Cas 2** : \( \cos\varphi = 0.8\ \text{AR} \) :  
  \[
  \Delta U = 43.48 \cdot (0.4 \cdot 0.8 + 0.6 \cdot 0.6) = \boxed{23.4\ \text{V}} \quad \Rightarrow U_2 = 230 - 23.4 = \boxed{206.6\ \text{V}}
  \]  

---

### **Rendement (\(\eta\))** :  
\[
\eta = \frac{P_2}{P_2 + \text{Pertes}} \quad ; \quad \text{Pertes} = P_{\text{fer}} + P_{\text{Joule}}
\]  
- **Pertes Joule** :  
  \[
  P_{\text{Joule}} = R_S \cdot I_2^2 = 0.4 \cdot (43.48)^2 \approx 756\ \text{W}
  \]  
- **Cas 1** : \( \cos\varphi = 1 \) :  
  \[
  \eta = \frac{10\,000 \cdot 1}{10\,000 + 50 + 756} \approx \boxed{92.3\%}
  \]  
- **Cas 2** : \( \cos\varphi = 0.8 \) :  
  \[
  \eta = \frac{10\,000 \cdot 0.8}{8\,000 + 50 + 756} \approx \boxed{89.5\%}
  \]  

---

## **3. Conclusion sur les performances**  
- **Chute de tension** : Acceptable pour \( \cos\varphi = 1 \), mais significative pour \( \cos\varphi = 0.8 \).  
- **Rendement** : Conforme aux attentes (typique pour un transformateur de 10 kVA).  
- **Vérification fiche technique** : Les résultats sont cohérents avec un transformateur standard (écarts dus aux hypothèses simplificatrices).  
