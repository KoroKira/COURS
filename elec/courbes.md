### **1️⃣ Tension de sortie (\( V_s(t) \)) en fonction du temps**  
- **Abscisse** : Temps \( t \) (en ms ou µs selon la fréquence de découpage)  
- **Ordonnée** : Tension \( V_s \) (en V)  
- **Forme** : Signal rectangulaire (tension découpée), alternant entre \( +E \) et \( -E \), avec des phases \( 0V \)  
- **Bornes** :  
  - \( V_s = +E \) lorsque \( K_1, K_4 \) sont actifs  
  - \( V_s = -E \) lorsque \( K_2, K_3 \) sont actifs  
  - \( V_s = 0 \) lors des périodes où la charge est court-circuitée  

---

### **2️⃣ Courant dans la charge (\( I_{charge}(t) \)) en fonction du temps**  
- **Abscisse** : Temps \( t \) (en ms ou µs)  
- **Ordonnée** : Courant \( I_{charge} \) (en A)  
- **Forme** :  
  - Si charge résistive : forme similaire à \( V_s(t) \) mais adoucie  
  - Si charge RL ou moteur : courbe triangulaire avec variations plus progressives  
- **Bornes** :  
  - En charge résistive : \( I = \frac{V_s}{R} \)  
  - En charge RL ou moteur : dépend de l’équation différentielle \( L \frac{dI}{dt} = V_s - R I \)  

---

### **3️⃣ Courant dans l’inductance (\( I_L(t) \))**  
- **Abscisse** : Temps \( t \)  
- **Ordonnée** : Courant dans l’inductance \( I_L \) (en A)  
- **Forme** :  
  - Signal triangulaire avec pente dépendant de \( V_s \)  
  - Montée du courant quand \( V_s \neq 0 \)  
  - Descente plus douce selon \( L \)  
- **Bornes** :  
  - Dépend de \( \Delta I = \frac{V_s \times T}{L} \) avec \( T \) la période de découpage  

---

### **4️⃣ Courant dans les interrupteurs (\( I_{T1}(t) \), \( I_{T2}(t) \), etc.)**  
- **Abscisse** : Temps \( t \)  
- **Ordonnée** : Courant dans chaque interrupteur (en A)  
- **Forme** : Signal en créneau (conduction ON/OFF)  
- **Bornes** :  
  - Conducteur seulement quand l’interrupteur est actif  
  - Courant \( I_{T1} \) suit \( I_{L} \) pendant la conduction de \( T1 \)  

---

### **5️⃣ Évolution du rapport cyclique (\( D \)) et impact sur \( V_s \)**  
- **Abscisse** : Rapport cyclique \( D \)  
- **Ordonnée** : Tension moyenne de sortie \( V_{s_{moy}} \)  
- **Forme** : Relation linéaire \( V_s = D \times V_e \)  
- **Bornes** :  
  - \( D = 0.3 \) → \( V_s = 0.3 \times V_e \)  
  - \( D = 0.7 \) → \( V_s = 0.7 \times V_e \)  

