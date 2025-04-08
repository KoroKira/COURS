# TP Sujet 2 - Asservissement en vitesse d’un moteur à courant continu

---

## **1. Modélisation du système**

### **1.1 Fonction de transfert \( G(p) = \frac{\omega(p)}{u(p)} \)**
**Équation donnée :**  
\[ T_m \cdot \dot{\omega}(t) + \omega(t) = k_m \cdot u(t) \]

En appliquant la transformée de Laplace (conditions initiales nulles) :  
\[ T_m \cdot p \cdot \omega(p) + \omega(p) = k_m \cdot u(p) \]  
Factorisation de \(\omega(p)\) :  
\[ \omega(p) (T_m p + 1) = k_m \cdot u(p) \]  
**Fonction de transfert :**  
\[ G(p) = \frac{\omega(p)}{u(p)} = \frac{k_m}{T_m p + 1} \]

---

### **1.2 Réponse à un échelon de tension \( u(t) = 6 \, \text{V} \)**
La réponse en régime permanent est une exponentielle :  
\[ \omega(t) = 6 k_m \left( 1 - e^{-t / T_m} \right) \]  
- **Valeur finale :** \( \omega_{\infty} = 6 k_m \, \text{rad/s} \)  
- **Constante de temps :** \( T_m \, \text{s} \).  

---

### **1.3 Identification expérimentale de \( k_m \) et \( T_m \)**  
**Méthode proposée :**  
1. Appliquer un échelon de tension \( u(t) = 6 \, \text{V} \).  
2. Mesurer la vitesse \( \omega(t) \) jusqu’à stabilisation.  
3. Déterminer \( T_m \) : temps pour atteindre \( 63\% \) de la valeur finale.  
4. Calculer \( k_m = \frac{\omega_{\infty}}{6} \).  

**Exemple :**  
Si \( \omega_{\infty} = 3 \, \text{rad/s} \), alors \( k_m = 0.5 \, \text{rad·s}^{-1}\text{·V}^{-1} \).  
Si \( T_m = 0.2 \, \text{s} \), le modèle Simulink doit correspondre à la réponse expérimentale.

---

## **2. Correction proportionnelle**

### **2.1 Fonction de transfert en boucle fermée \( F(p) \)**  
Schéma bloc :  
\[ F(p) = \frac{\omega(p)}{r(p)} = \frac{K G(p)}{1 + K G(p)} = \frac{K k_m}{T_m p + 1 + K k_m} \]  
Simplification :  
\[ F(p) = \frac{K k_m / (1 + K k_m)}{T_m / (1 + K k_m) \cdot p + 1} \]  
- **Nouvelle constante de temps :** \( \frac{T_m}{1 + K k_m} \).  
- **Gain statique :** \( \frac{K k_m}{1 + K k_m} \).  

---

### **2.2 Stabilité**  
Le système est **toujours stable** pour \( K > 0 \), car le pôle est :  
\[ p = -\frac{1 + K k_m}{T_m} < 0 \].  

---

### **2.3 Erreur statique**  
Pour une consigne \( r(t) = 5 \, \text{rad/s} \) :  
\[ \epsilon_{\text{stat}} = \frac{r}{1 + K k_m} \].  
- Si \( K \uparrow \), alors \( \epsilon_{\text{stat}} \downarrow \).  

**Simulation avec \( K = 0.5, 1, 2, 3 \) :**  
- Pour \( K = 3 \), réponse rapide (\( T_m / (1 + 3 k_m) \)), mais risque de saturation en tension (\( U_{\text{max}} = \pm 10 \, \text{V} \)).  

---

### **2.4 Respect du cahier des charges**  
- **Temps de réponse < 150 ms :**  
  Si \( T_m = 0.2 \, \text{s} \) et \( K = 3 \), la constante de temps devient \( 0.08 \, \text{s} \), ce qui est acceptable.  
- **Limitation :** Une valeur trop élevée de \( K \) entraîne une saturation du signal de commande \( u(t) \).  

---

## **3. Correction proportionnelle-intégrale (PI)**

### **3.1 Synthèse du correcteur \( C(p) \)**  
**Spécifications :**  
- Erreur statique nulle (intégrateur requis).  
- Temps de réponse \( \leq 150 \, \text{ms} \).  

**Correcteur PI :**  
\[ C(p) = K_p + \frac{K_i}{p} \]  
**Méthode du modèle imposé :**  
Choisir \( K_p \) et \( K_i \) pour imposer une dynamique souhaitée (ex : pôles dominants).  

---

### **3.2 Stabilité**  
La stabilité est vérifiée si les pôles de la boucle fermée sont à partie réelle négative.  
**Exemple :**  
Avec \( C(p) = 2 + \frac{1}{p} \), la fonction de transfert devient :  
\[ F(p) = \frac{C(p) G(p)}{1 + C(p) G(p)} \]  
Les pôles sont déterminés par l’équation caractéristique \( 1 + C(p) G(p) = 0 \).  

---

## **4. Prise en compte d’une perturbation**

### **4.1 Schéma bloc modifié**  
Ajouter la perturbation \( d(t) \) comme une entrée additive sur la sortie \( \omega(t) \).  

**Expression de l’erreur :**  
\[ \epsilon(p) = H_1(p) \cdot r(p) + H_2(p) \cdot d(p) \]  
Avec :  
- \( H_1(p) = \frac{1}{1 + C(p) G(p)} \)  
- \( H_2(p) = -\frac{G(p)}{1 + C(p) G(p)} \)  

---

### **4.2 Erreur statique avec perturbation**  
- **Correcteur proportionnel :** Erreur non nulle (\( \epsilon_{\text{stat}} = \frac{-d_0}{1 + K k_m} \)).  
- **Correcteur PI :** Erreur statique nulle (action intégrale compense la perturbation).  

---

### **4.3 Simulation avec \( d_0 = 0.8 \)**  
- **Correcteur P :** Déviation permanente de \( \omega(t) \).  
- **Correcteur PI :** Retour à la consigne après transitoire.  

---

## **5. Conclusion**  
- La correction proportionnelle améliore la rapidité mais laisse une erreur statique.  
- Le correcteur PI élimine l’erreur statique et rejette les perturbations.  
- Les simulations et tests expérimentaux confirment les calculs théoriques.