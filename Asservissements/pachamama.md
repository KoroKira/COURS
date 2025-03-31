**Étapes détaillées pour MATLAB/Simulink :**

### **Partie 2 : Modélisation du système**
1. **Création de la fonction de transfert \( H(s) \) :**
   - Ouvrez MATLAB et lancez Simulink.
   - Créez un nouveau modèle Simulink.
   - Ajoutez les blocs suivants :
     - **Step** (Source) : Configuration par défaut (échelon unitaire à \( t = 1 \)).
     - **Transfer Fcn** (Continuous) : 
       - Numérateur : \( K_r \cdot K_m \) (remplacer par les valeurs numériques).
       - Dénominateur : \( [T_m \quad 1 \quad 0] \) (correspond à \( s(T_m s + 1) \)).
     - **Scope** (Sinks) : Pour visualiser \( \Theta_b(t) \).
   - Connectez les blocs : Step → Transfer Fcn → Scope.
   - Simulez (Configuration : durée de simulation suffisante, ex. 10s). La réponse doit montrer une rampe après un transitoire.

2. **Explication de la réponse :**
   - Mathématique : \( H(s) = \frac{K_r K_m}{s(T_m s + 1)} \). En réponse à un échelon (\( \frac{1}{s} \)), \( \Theta_b(t) \) diverge (rampe linéaire).
   - Physique : Le moteur atteint une vitesse constante (\( w = K_m u \)), donc \( \Theta_b(t) \) croît linéairement.

3. **Solution au problème :**
   - Ajouter un **asservissement en position** (boucle fermée) pour stabiliser \( \Theta_b(t) \).

---

### **Partie 3 : Correcteur Proportionnel**
1. **Fonction de transfert en boucle fermée \( F(s) \) :**
   - \( F(s) = \frac{k_c K_r K_m}{T_m s^2 + s + k_c K_r K_m} \).

2. **Stabilité :**
   - Tous les coefficients du dénominateur sont positifs → système stable.

3. **Paramètres caractéristiques :**
   - Gain statique \( K = 1 \).
   - Amortissement \( \zeta = \frac{1}{2 \sqrt{k_c K_r K_m T_m}} \).
   - Pulsation naturelle \( \omega_n = \sqrt{\frac{k_c K_r K_m}{T_m}} \).
   - Oscillations si \( k_c > \frac{1}{4 K_r K_m T_m} \).

4. **Calcul des erreurs :**
   - Erreur statique (échelon) : \( 0 \).
   - Erreur de traînage (rampe) : \( \frac{1}{k_c K_r K_m} \).

5. **Simulation dans Simulink :**
   - Ajoutez un **Sum** (comparaison \( \Theta_{ref} - \Theta_b \)).
   - Ajoutez un **Gain** \( k_c \) entre le Sum et \( H(s) \).
   - Bouclez \( \Theta_b \) vers le Sum (négatif).
   - Testez pour \( k_c \in [0.2, 5] \) :
     - **Échelon** (\( \pi/2 \)) : Vérifiez l’absence d’erreur statique.
     - **Rampe** : Mesurez l’erreur de traînage (doit diminuer avec \( k_c \)).

6. **Calcul de \( k_c \) pour erreur de vitesse < 5% :**
   - \( k_c = \frac{20}{K_r K_m} \) (si \( \frac{1}{k_c K_r K_m} < 0.05 \)).

7. **Pic de dépassement :**
   - Utilisez \( D\% = e^{\frac{-\pi \zeta}{\sqrt{1 - \zeta^2}}} \times 100\% \) avec \( \zeta \) calculé pour \( k_c \) trouvé.

8. **Marge de phase avec MATLAB :**
   - Code :
     ```matlab
     sys_open = kc * tf([Kr*Km], [Tm 1 0]); % Boucle ouverte
     margin(sys_open); % Vérifiez Marges > 45°
     ```

---

### **Partie 4 : Correcteur à Avance de Phase**
1. **Vérification de l’erreur de vitesse :**
   - \( K_v = k_c K_r K_m \) reste inchangé → erreur maintenue.

2. **Réglage de \( \tau \) et \( a \) :**
   - Utilisez la **boîte à outils "Control System Designer"** dans MATLAB :
     - Fixez \( k_c \) précédent.
     - Ajustez \( \tau \) et \( a \) pour obtenir une marge de phase \( \geq 45° \).
   - Code de synthèse :
     ```matlab
     C_phase = kc * tf([a*Tau 1], [Tau 1]); % Correcteur avance de phase
     sys_open_new = C_phase * H(s);
     margin(sys_open_new);
     ```
   - Testez dans Simulink et validez les spécifications.

---

**Fichiers Simulink à créer :**
- `Modele_OpenLoop.slx` : Partie 2 (boucle ouverte).
- `Modele_Proportional.slx` : Partie 3 (correcteur proportionnel).
- `Modele_PhaseLead.slx` : Partie 4 (correcteur avance de phase).

📝 **Remarque :** Les valeurs numériques de \( T_m, K_m, K_r \) doivent être remplacées par celles de votre étude préparatoire.