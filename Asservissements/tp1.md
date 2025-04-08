# Réponses pour la partie 3.1 - Correcteur proportionnel

## 1. Fonction de transfert en boucle fermée \(F(s)\)

La fonction de transfert en boucle fermée est donnée par :

\[
F(s) = \frac{\Theta_b(s)}{\Theta_{ref}(s)} = \frac{C(s) \cdot H(s)}{1 + C(s) \cdot H(s)}
\]

Avec \(C(s) = k_c\) et \(H(s)\) étant la fonction de transfert du système en boucle ouverte (moteur + réducteur), on obtient :

\[
F(s) = \frac{k_c \cdot H(s)}{1 + k_c \cdot H(s)}
\]

**Explication :**  
Cette formule représente le rapport entre la sortie \(\Theta_b(s)\) et la consigne \(\Theta_{ref}(s)\) lorsque le système est bouclé avec un correcteur proportionnel. Le dénominateur \(1 + k_c \cdot H(s)\) montre l'effet de la rétroaction sur la stabilité et la réponse du système.

---

## 2. Stabilité du système en boucle fermée

Le système en boucle fermée est stable si tous les pôles de \(F(s)\) ont une partie réelle négative. Pour un correcteur proportionnel, la stabilité dépend des pôles de \(H(s)\) et de la valeur de \(k_c\).

**Explication :**  
Si \(H(s)\) est stable (ce qui est généralement le cas pour un moteur avec une constante de temps mécanique \(T_m > 0\)), alors le système en boucle fermée reste stable pour toute valeur positive de \(k_c\). Cependant, une valeur trop élevée de \(k_c\) peut entraîner des oscillations ou un comportement instable.

---

## 3. Paramètres caractéristiques de \(F(s)\)

Les paramètres caractéristiques sont :
- **Gain statique \(K\) :**  
  \[
  K = \lim_{s \to 0} F(s) = \frac{k_c \cdot K_m \cdot K_r}{1 + k_c \cdot K_m \cdot K_r}
  \]
  
- **Amortissement \(\zeta\) et pulsation naturelle \(w_n\) :**  
  Si \(H(s)\) est du premier ordre, \(F(s)\) reste du premier ordre avec un amortissement \(\zeta\) et une pulsation naturelle \(w_n\) dépendant de \(k_c\).

**Régime pseudo-périodique :**  
Le système présentera des oscillations si \(\zeta < 1\). Pour un système du second ordre, cela se produit lorsque :
\[
k_c > \frac{1}{4 \cdot T_m \cdot K_m \cdot K_r}
\]

**Explication :**  
Le gain statique \(K\) indique la réponse en régime permanent. L'amortissement \(\zeta\) et la pulsation naturelle \(w_n\) déterminent la dynamique de la réponse (rapidité, oscillations). Un amortissement faible (\(\zeta < 1\)) conduit à des oscillations.

---

## 4. Erreurs statiques et de traînage

- **Erreur statique :**  
  Pour une consigne en échelon, l'erreur statique est :
  \[
  e_{stat} = \frac{1}{1 + k_c \cdot K_m \cdot K_r}
  \]
  
- **Erreur de traînage :**  
  Pour une consigne en rampe, l'erreur de traînage est :
  \[
  e_{train} = \frac{1}{k_c \cdot K_m \cdot K_r}
  \]

**Explication :**  
L'erreur statique diminue avec l'augmentation de \(k_c\), mais l'erreur de traînage persiste car un correcteur proportionnel seul ne peut pas annuler complètement l'erreur pour une entrée en rampe.

---

## 5. Influence du gain \(k_c\)

- **Pour \(k_c\) faible (ex : 0.2) :**  
  Réponse lente, erreur statique importante, pas d'oscillations.
  
- **Pour \(k_c\) élevé (ex : 5) :**  
  Réponse rapide, erreur statique réduite, mais risque d'oscillations ou d'instabilité.

**Explication :**  
Un gain \(k_c\) élevé améliore la précision et la rapidité, mais peut compromettre la stabilité et introduire des oscillations. Il faut trouver un compromis.

---

## 6. Gain \(k_c\) pour une erreur de vitesse < 5%

Pour satisfaire \(e_{train} < 5\%\), on résout :
\[
\frac{1}{k_c \cdot K_m \cdot K_r} < 0.05 \implies k_c > \frac{20}{K_m \cdot K_r}
\]

**Explication :**  
Cette condition garantit que l'erreur de vitesse (pour une consigne en rampe) reste inférieure à 5%.

---

## 7. Pic du premier dépassement

Pour un système du second ordre, le dépassement \(D\%\) est donné par :
\[
D\% = 100 \cdot e^{-\frac{\zeta \pi}{\sqrt{1 - \zeta^2}}}
\]

Avec \(\zeta\) calculé à partir de \(k_c\), on peut estimer le dépassement.

**Explication :**  
Le dépassement dépend de l'amortissement \(\zeta\). Pour \(k_c\) élevé, \(\zeta\) diminue, ce qui augmente le dépassement.

---

## 8. Marges de gain et de phase

Utilisez MATLAB pour calculer :
- **Marge de gain (GM) :**  
  Mesure la robustesse face aux variations de gain.
  
- **Marge de phase (PM) :**  
  Doit être > 45° pour limiter le dépassement à 20-25%.

**Explication :**  
Une marge de phase suffisante garantit un bon compromis entre rapidité et stabilité. Si la marge est trop faible, le système peut devenir oscillant.

---

**Note :**  
Les réponses supposent que \(H(s)\) est du premier ordre. Si \(H(s)\) est plus complexe, les formules doivent être adaptées en conséquence. Les simulations sous MATLAB/Simulink sont nécessaires pour valider les calculs.