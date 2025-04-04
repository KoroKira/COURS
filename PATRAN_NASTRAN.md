# Index:



# 0. Avant Patran/Nastran

1. Il faut analyser sur papier le problème

Formules mécaniques à connaitre:

PFS
Analyser l'emplacement des efforts/forces appliquées sur les poutres

EN SACHANT QU'ON EST TJR A L'EQUILIBRE, somme des forces = 0 et somme des moments = 0
La target c'est de trouver toute les forces et moments sur les poutres, et les appliquer en un point

Voici un condensé des bases de la mécanique des structures pour ton exam sur Patran.  

---

## 📌 **Formules Essentielles en Mécanique des Poutres & Portiques**

### **1. Équilibre Statique (Rappels de base)**
- **Somme des forces** : \( \sum F_x = 0 \), \( \sum F_y = 0 \)  
- **Somme des moments** : \( \sum M = 0 \)  
- Cas d’usage : Vérifier l’équilibre d’une structure isostatique (statique).

### **2. Efforts Internes (Diagrammes de sollicitation)**
- **Effort Normal (N)** : \( N = \sum F_x \)  
  - Contrainte normale : \( \sigma = \frac{N}{A} \)  
  - Utilisation : Vérifier la résistance d’une section en traction/compression.
- **Effort Tranchant (T ou V)** : \( V = \sum F_y \)  
  - Utilisation : Calcul des efforts coupants dans une poutre.
- **Moment Fléchissant (M)** :  
  - \( M = \sum (F \cdot d) \)  
  - Contrainte de flexion : \( \sigma = \frac{M \cdot y}{I} \)  
  - Utilisation : Calcul de la flexion d’une poutre.

### **3. Déformées (Flexion & Torsion)**
- **Flèche (Déformation verticale d’une poutre) :**  
  - **Poutre en appui simple** sous charge ponctuelle au centre :  
    \[
    \delta_{max} = \frac{F L^3}{48 E I}
    \]
  - **Poutre encastrée aux deux extrémités** sous charge uniforme :  
    \[
    \delta_{max} = \frac{5qL^4}{384EI}
    \]
- **Torsion (tige circulaire pleine) :**  
  - Angle de torsion : \( \theta = \frac{M_t L}{G J} \)  
  - Contraintes de torsion : \( \tau = \frac{M_t r}{J} \)  
  - Avec \( J = \frac{\pi d^4}{32} \) (moment d’inertie polaire)

### **4. Matériaux & Contraintes**
- **Module de Young \( E \)** : Rigidité du matériau en traction/compression.  
  Ex : \( E_{acier} \approx 210 \text{ GPa} \), \( E_{bois} \approx 10 \text{ GPa} \).
- **Module de cisaillement \( G \)** : Rigidité en cisaillement.  
  \( G = \frac{E}{2(1+\nu)} \) avec \( \nu \) le coefficient de Poisson.
- **Contrainte admissible** : \( \sigma_{adm} = \frac{\sigma_{rupture}}{\text{coefficient de sécurité}} \)

---

## 📌 **Unités & Conversions Importantes**
| Grandeur | Unité SI | Conversion |
|----------|---------|------------|
| Force \( F \) | Newton (N) | 1 kN = 1000 N |
| Longueur \( L \) | mètre (m) | 1 mm = 0.001 m |
| Contrainte \( \sigma \) | Pascal (Pa) | 1 MPa = \( 10^6 \) Pa |
| Moment \( M \) | Newton-mètre (N·m) | 1 kN·m = 1000 N·m |
| Module de Young \( E \) | Pascal (Pa) | 1 GPa = \( 10^9 \) Pa |

⚠ **Attention aux unités dans Patran !**  
- Travailler en **N, mm, MPa** pour éviter des erreurs.  
- Vérifier la **cohérence des unités** dans les entrées du logiciel.

---

Voici un **guide pratique** pour gérer les problèmes de **poutres, portiques et plaques avec trous** en mécanique **avant d'utiliser Patran**.  

---

# 📌 **GUIDE DE RÉFLEXION AVANT PATRAN**

## **1️⃣ Identifier le Type de Problème**
### ➤ **Poutre ou Portique ?**
- **Poutre** : Élément long et fin, sollicité en **flexion, traction/compression, cisaillement**.  
- **Portique** : Ensemble de poutres assemblées, souvent sollicité en **flexion et efforts normaux**.  
- **Plaque perforée** : Plaque mince avec un trou générant une concentration de contraintes.

---

## **2️⃣ Déterminer les Hypothèses et Modélisations**
**👉 Pour une Poutre :**  
- Hypothèse de **Bernoulli** : Pas de cisaillement transversal, plan de section reste plan.  
- Hypothèse de **Timoshenko** (si section courte et épaisse) : Cisaillement transversal pris en compte.  

**👉 Pour un Portique :**  
- Articulations ou encastrements aux jonctions ?  
- Structures hyperstatiques nécessitant une **analyse des réactions** avant tout.  

**👉 Pour une Plaque Perforée :**  
- Trou génère une **concentration de contrainte** :  
  \[
  \sigma_{max} = K_t \cdot \sigma_{nom}
  \]
  avec \( K_t \) facteur de concentration de contrainte.  

---

## **3️⃣ Équilibre Statique & Réactions**
**⚠ AVANT TOUT : Calculer les réactions d’appui !**  
### ➤ **Cas 1 : Poutre Isostatique**  
- **Appui simple** (1 réaction verticale)  
- **Appui glissant** (1 réaction perpendiculaire)  
- **Encastrement** (1 force + 1 moment)  

⚡ **Équations :**  
\[
\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M = 0
\]
✅ Résoudre ces équations pour obtenir **les réactions**.

### ➤ **Cas 2 : Poutre Hyperstatique**  
- Plus de trois équations → Nécessite des **équations supplémentaires** (flèche, compatibilité des déformations, etc.).

---

## **4️⃣ Efforts Internes : N, V, M**
**📌 Objectif : Tracer les diagrammes d'efforts internes.**  
- **Effort Normal \( N \)** : Traction/compression (utilisé pour résistance des matériaux).  
- **Effort Tranchant \( V \)** : Cisaillement.  
- **Moment Fléchissant \( M \)** : Flexion → Utilisation de \( \sigma = \frac{M y}{I} \).  

⚡ **Méthode :**  
1. **Découper la poutre** en segments entre les forces et appuis.  
2. Écrire les équations d’équilibre sur chaque segment.  
3. Tracer les **diagrammes de \( N, V, M \)**.  

---

## **5️⃣ Déformée & Flèche**
Si nécessaire, utiliser :  
- **Equation de la ligne élastique** (Poutre Bernoulli) :  
  \[
  EI \frac{d^2y}{dx^2} = M(x)
  \]
- Méthode des **intégrations successives** ou **principe de superposition**.  

---

## **6️⃣ Contraintes et Vérifications**
### ➤ **1. Contrainte Normale (traction/compression)**
\[
\sigma = \frac{N}{A}
\]
🔹 Vérifier \( \sigma < \sigma_{adm} \).

### ➤ **2. Contrainte de Flexion**
\[
\sigma = \frac{M y}{I}
\]
🔹 Vérifier \( \sigma_{max} \) dans la poutre.

### ➤ **3. Contrainte de Cisaillement**
\[
\tau = \frac{V S}{I b}
\]
Avec **\( S \)** le moment statique.

### ➤ **4. Torsion (si nécessaire)**
\[
\tau = \frac{M_t r}{J}
\]
🔹 Vérifier pour des sections circulaires.

---

## **7️⃣ Plaques avec Trous : Concentration des Contraintes**
⚠ **Trou = Zone critique → Vérifier \( K_t \)**  
- Pour un trou circulaire dans une plaque en traction simple :  
  \[
  K_t \approx 3
  \]
- Pour un trou dans une plaque en flexion :  
  \[
  K_t \approx 2.5
  \]

Si la contrainte max dépasse la limite admissible → **Renfort autour du trou**.

---

## **8️⃣ Vérification des Unités**
**Toujours vérifier** que tout est en N, mm, MPa avant d’entrer dans Patran.

---

### **🔥 En Résumé :**
1️⃣ **Identifier** le type de structure (poutre, portique, plaque).  
2️⃣ **Trouver les réactions d’appuis** avec l’équilibre statique.  
3️⃣ **Tracer les diagrammes d’efforts internes** (N, V, M).  
4️⃣ **Analyser la flèche et les contraintes**.  
5️⃣ **Vérifier les unités avant Patran**.  

### **🔥 GUIDE PAS À PAS POUR MODÉLISER UNE POUTRE DANS PATRAN (1D & 2D) 🔥**  
**(Pour les vrais débutants, on va détailler chaque clic)**  

---

## **📌 I. PRÉPARATION AVANT PATRAN**  
Avant de toucher à la souris :  
✅ Vérifie que tes unités sont **cohérentes** (ex : N, mm, MPa).  
✅ Dessine un **schéma rapide** avec les dimensions, appuis et chargements.  
✅ Note les **propriétés du matériau** (Module de Young \( E \), etc.).  
✅ Prépare une **table des charges** avec les forces appliquées.

---

## **🔴 II. CRÉER UNE POUTRE EN 1D (ÉLÉMENT FILAIRE)**
*(Utilisé pour les poutres simples, portiques, treillis…)*  

### **1️⃣ Ouvrir un Nouveau Modèle**
1. **Lancer Patran**  
2. **Fichier** → **Nouveau Modèle**  
3. Sélectionne l’unité : **mm, N**  
4. Clique sur **OK**.

---

### **2️⃣ Création de la Géométrie (Noeuds & Ligne)**
1. Dans le menu **Geometry**, clique sur **Points**.  
2. Dans **Create Point**, entre les coordonnées des points :  
   - Exemple : Poutre de 1000 mm de long, définis **deux points** :  
     - **Point 1** : (0,0,0)  
     - **Point 2** : (1000,0,0)  
3. Clique sur **Apply** après chaque point.  
4. Maintenant, crée une **ligne** entre ces points :  
   - **Geometry** → **Curve** → **Create**  
   - **Method** : **Two Points**  
   - Sélectionne **Point 1 & Point 2**  
   - Clique **Apply**.

---

### **3️⃣ Définir la Section de la Poutre**
1. **Properties** → **1D** → **Create**  
2. **Nom** : "Poutre1D"  
3. **Element Type** : **Beam** (Poutre)  
4. **Material** : Clique **Create Material** → entre :  
   - **Nom** : "Acier"  
   - **E (Module de Young)** : 210000 MPa  
   - **ν (Poisson)** : 0.3  
   - **Apply**  
5. **Section de la Poutre** → Clique sur **Create Section**  
   - Sélectionne **Rectangle / Tube / IPE** selon la poutre  
   - Exemple : Rectangle **b = 50 mm, h = 100 mm**  
   - **Apply**.  
6. Applique cette propriété à la **ligne créée** (sélectionne la ligne puis "Apply").

---

### **4️⃣ Définir les Appuis (Conditions aux Limites)**
1. **BCS (Boundary Conditions)** → **Create**  
2. Nom : "Appuis"  
3. **Sélectionne les Noeuds** où appliquer les appuis :  
   - Ex : Noeud **1** (x=0,0,0)  
   - **Tx, Ty, Tz, Rx, Ry, Rz = Fixé (encastrement)**  
4. **Apply**.  

---

### **5️⃣ Appliquer les Charges**
1. **BCS (Boundary Conditions)** → **Create**  
2. Nom : "Charge"  
3. **Sélectionne le Noeud** où s’applique la force  
4. **Type** : Force  
5. **Valeur** : Ex : **-5000 N en Y** (poussée vers le bas)  
6. **Apply**.  

---

### **6️⃣ Maillage de la Poutre**
1. **Meshing** → **1D**  
2. Sélectionne la ligne → **Number of Elements** : Ex : 10  
3. **Apply**.  

---

### **7️⃣ Lancer le Calcul**
1. **Analysis** → **Job** → **Create**  
2. Nom : "Test1"  
3. **Solution Type** : Linear Static  
4. **Submit Job** → **OK**.  

---

### **8️⃣ Affichage des Résultats**
1. **Results** → **Select Results Case** → **Apply**.  
2. **Deformed Shape** → **Apply** (pour voir la déformée).  
3. **Contour Plot** → **Apply** (pour voir contraintes).  

🔥 **1D Terminé ! Passons au 2D !** 🔥  

---

## **🔵 III. CRÉER UNE POUTRE EN 2D (ÉLÉMENT SHELL)**
*(Utilisé pour des plaques, poutres épaisses, coques…)*  

### **1️⃣ Ouvrir un Nouveau Modèle**
1. **Fichier** → **Nouveau**  
2. **Unité : mm, N**  
3. **OK**.  

---

### **2️⃣ Création de la Géométrie (Surface)**
1. **Geometry** → **Surfaces** → **Create**  
2. **Méthode** : Rectangle  
3. **Entrez les dimensions** :  
   - **Longueur** = 1000 mm  
   - **Hauteur** = 100 mm  
4. **Apply**.  

---

### **3️⃣ Définir les Propriétés de Matériau**
1. **Properties** → **2D** → **Create**  
2. **Nom** : "Plaque"  
3. **Element Type** : Shell  
4. **Material** :  
   - **Nom** : "Acier"  
   - **E = 210000 MPa, ν = 0.3**  
5. **Apply**.  

---

### **4️⃣ Appliquer les Appuis**
1. **BCS (Boundary Conditions)** → **Create**  
2. Sélectionne un **côté entier** de la plaque  
3. **Tx, Ty, Tz, Rx, Ry, Rz = Fixé** (encastrement)  
4. **Apply**.  

---

### **5️⃣ Appliquer la Charge**
1. **BCS (Boundary Conditions)** → **Create**  
2. Sélectionne la **face supérieure**  
3. **Type** : Pression  
4. **Valeur** : Ex : **5000 N/m²**  
5. **Apply**.  

---

### **6️⃣ Maillage de la Plaque**
1. **Meshing** → **2D**  
2. Sélectionne la surface  
3. **Nombre d’éléments** : Ex : 20x10  
4. **Apply**.  

---

### **7️⃣ Calculer et Afficher Résultats**
1. **Analysis** → **Create Job**  
2. **Submit Job** → **OK**  
3. **Results** → **Deformed Shape** → **Apply**  
4. **Contour Plot** → **Apply**  

---

🔥 **FÉLICITATIONS ! TU SAIS FAIRE DES POUTRES EN 1D ET 2D DANS PATRAN !** 🔥  