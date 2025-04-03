Durant les phases expérimentales, le circuit de charge (connecté entre les points B et
C) sera successivement composé de :
o Cas 1: Une résistance réglée à 75Ω [R],
o Cas 2: Une résistance réglée à 75Ω associée à une inductance, à sa valeur minimale
[Lmin],
o Cas 3: Une résistance réglée à 75Ω associée à une inductance, à sa valeur maximale
[Lmax],

1) Observer à l’oscilloscope et sur le voltmètre analogique placés au niveau de la
charge, l’évolution de la tension quand on fait varier les potentiomètres
"Fréquence" et Tension moyenne. Expliquer l’impact de ces variables sur la
tension de sortie.
2) Enregistrer les courbes de tension et courant dans la charge pour une tension
moyenne de sortie de 15V et une fréquence de découpage de 500Hz. Faites
attention à la lecture de la fréquence sur l’oscilloscope qui peut être erronée.
Assurez vous de mesurer la période sur l’oscilloscope.
3) En vous appuyant sur les formes d’ondes de la tension de sortie Vs, déterminer
la relation liant la valeur moyenne de Vs et la tension d’entrée Ve ainsi que le
rapport cyclique α, tel que < Vs >= f(Ve, α).

---

---

## **📌 Partie 1 : Étude du hacheur 4 quadrants**  

### **Cas 1 : Charge purement résistive**  

1️⃣ **Observation de l’impact de la fréquence et du rapport cyclique sur la tension de sortie**  
- **Effet du rapport cyclique \( \alpha \) :**  
  - Si \( \alpha \) augmente, la tension moyenne \( \langle V_s \rangle \) augmente.  
  - Si \( \alpha \) diminue, \( \langle V_s \rangle \) diminue.  
  - Relation attendue :  
    \[
    \langle V_s \rangle = \alpha \times V_e
    \]
- **Effet de la fréquence de découpage \( f \) :**  
  - Plus \( f \) est grande, plus l’ondulation sur \( V_s \) et \( I_s \) diminue.  
  - Plus \( f \) est basse, plus l’ondulation devient importante.  

📌 **Comment on l'a vu** :  
- On a fait varier \( \alpha \) et on a vu comment \( V_s \) évolue à l’oscilloscope.  
- On a fait varier \( f \) et on a vu l’ondulation.  

2️⃣ **Enregistrement des courbes de \( V_s \) et \( I_s \)**  
📌 **À faire** :  
- Régler \( \langle V_s \rangle = 15V \) et \( f = 500Hz \).  
- Capturer la courbe de \( V_s(t) \) et \( I_s(t) \) avec l’oscilloscope.  
- Vérifier la période du signal pour valider la fréquence.  

3️⃣ **Détermination de la relation entre \( \langle V_s \rangle \), \( V_e \) et \( \alpha \)**  
📌 **À faire** :  
- Déterminer \( \langle V_s \rangle \) expérimentalement.  
- Vérifier si \( \langle V_s \rangle = \alpha \times V_e \) est respecté.  

4️⃣ **Tracer \( \langle V_s \rangle = f(\alpha) \)**  
📌 **À faire** :  
- Tracer \( \langle V_s \rangle \) en fonction de \( \alpha \) (de 0.2 à 0.8).  
- Comparer avec la courbe théorique \( \langle V_s \rangle = \alpha V_e \).  

---

### **Cas 2 : Charge résistive + inductance variable**  

1️⃣ **Enregistrement de \( V_s \) et \( I_s \) pour \( L_{min} \), \( f = 200Hz \)**  
📌 **À faire** :  
- Capturer les courbes \( V_s(t) \) et \( I_s(t) \) à l’oscilloscope.  

2️⃣ **Impact de l’inductance sur \( V_s \) et \( I_s \)**  
- Plus \( L \) est grand, plus \( I_s \) est lissé.  
- Relation avec la constante de temps \( \tau = \frac{L}{R} \).  

📌 **À faire** :  
- Faire varier \( L \) de \( L_{min} \) à \( L_{max} \) et observer les effets sur \( \Delta i_L \).  

3️⃣ **Impact de la fréquence sur l’ondulation du courant**  
📌 **À faire** :  
- Faire varier \( f \) jusqu’à \( f_{max} \) et observer l’effet sur \( \Delta i_L \).  

4️⃣ **Relation de l’ondulation du courant**  
La formule est :  
\[
\Delta i_L = \frac{V_e \times \alpha}{L \times f}
\]  
📌 **À faire** :  
- Vérifier expérimentalement cette relation.  
- Proposer une solution pour réduire \( \Delta i_L \) (ex : augmenter \( L \) ou \( f \)).  

5️⃣ **Retrouver \( L \) expérimentalement**  
📌 **À faire** :  
- Régler \( \alpha = 0.5 \), \( R = 100 \Omega \), \( V_e = 30V \), \( L = 0.5H \).  
- Mesurer \( \Delta i_L \) et vérifier si \( L \) correspond à la formule.  

6️⃣ **Étudier les séquences de conduction**  
📌 **À faire** :  
- Dessiner les schémas équivalents pour \( \alpha = 0.8 \) et \( \alpha = 0.5 \).  

---

## **📌 Partie 2 : Étude d’un onduleur**  

### **Cas 1 : Charge résistive**  
1️⃣ **Différences des formes d’ondes par rapport au hacheur 4Q**  
📌 **À faire** :  
- Comparer \( V_s(t) \) et \( I_s(t) \) entre les deux cas.  

2️⃣ **Observer la tension de réglage du rapport cyclique**  
📌 **À faire** :  
- Observer la tension entre \( E \) et \( F \).  
- Identifier le signal et son rôle (probablement un signal PWM).  

---

### **Cas 2 : Charge résistive + inductive**  
3️⃣ **Impact de l’inductance sur \( V_s \) et \( I_s \)**  
📌 **À faire** :  
- Observer comment l’inductance affecte la forme d’onde de \( I_s \).  

4️⃣ **Amélioration de la tension de sortie**  
📌 **À faire** :  
- Proposer un composant pour améliorer la tension (ex : condensateur en parallèle).  

---

Si tu veux des courbes et calculs détaillés, dis-moi ce que tu veux en priorité ! 🚀📊