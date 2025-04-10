# TP Sujet 2 - Asservissement en vitesse d’un moteur à courant continu

---

## Modélisation du système

### Fonction de transfert \( G(p) = \frac{\omega(p)}{u(p)} \)
**Équation donnée :**  
\[ T_m \cdot \dot{\omega}(t) + \omega(t) = k_m \cdot u(t) \]

En appliquant la transformée de Laplace (conditions initiales nulles) :  
\[ T_m \cdot p \cdot \omega(p) + \omega(p) = k_m \cdot u(p) \]  
Factorisation de \(\omega(p)\) :  
\[ \omega(p) (T_m p + 1) = k_m \cdot u(p) \]  
**Fonction de transfert :**  
\[ G(p) = \frac{\omega(p)}{u(p)} = \frac{k_m}{T_m p + 1} \]

---

### Réponse à un échelon de tension \( u(t) = 6 \, \text{V} \)
La réponse en régime permanent est une exponentielle :  
\[ \omega(t) = 6 k_m \left( 1 - e^{-t / T_m} \right) \]  
- **Valeur finale :** \( \omega_{\infty} = 6 k_m \, \text{rad/s} \)  
- **Constante de temps :** \( T_m \, \text{s} \).  

---

### Identification expérimentale de \( k_m \) et \( T_m \)  
**Méthode proposée :**  
1. Appliquer un échelon de tension \( u(t) = 6 \, \text{V} \).  
2. Mesurer la vitesse \( \omega(t) \) jusqu’à stabilisation.  
3. Déterminer \( T_m \) : temps pour atteindre \( 63\% \) de la valeur finale.  
4. Calculer \( k_m = \frac{\omega_{\infty}}{6} \).  
