# Cours A3.6 : Métallurgie Avancée  
*Par Guilhem, inspiré du cours original A36-Métallurgie (A2027)*  

---

## **1. Introduction à la Science des Matériaux Métalliques**  
### 1.1 Définition et Enjeux  
Les matériaux métalliques représentent **60% de la masse des objets manufacturés** (automobiles, avions, infrastructures). Leur étude combine :  
- **Physique des solides** (structure cristalline),  
- **Thermodynamique** (diagrammes de phases),  
- **Mécanique** (déformations, dislocations).  

**Exemple historique** : La transition Âge du Bronze → Âge du Fer (1200 av. J.-C.) a révolutionné les outils grâce à la maîtrise de la réduction du minerai.  

---

## **2. États de la Matière et Mécanismes de Solidification**  
### 2.1 Transition Liquide-Solide  
- **Liquide** :  
  - Mouvement brownien, **enthalpie élevée**.  
  - **Viscosité** : 1-10 mPa·s pour les métaux fondus (vs 1000 mPa·s pour l’huile).  
- **Solide** :  
  - **Réseaux cristallins** : CFC (Cu, Al), CC (Feα), HC (Zn).  
  - **Énergie de cohésion** : 100-800 kJ/mol (ex : 418 kJ/mol pour Fe).  

### 2.2 Courbes de Refroidissement  
![Courbe de refroidissement](https://via.placeholder.com/600x300?text=Palier+de+solidification+et+pente+de+surliquidus)  
- **Métal pur** : Palier isotherme (ex : Fe à 1538°C).  
- **Alliage** : Intervalle de solidification (ex : Al-Si entre 577°C et 660°C).  

**Équation de solidification** (simplifiée) :  
\[ Q = m \cdot L_f + m \cdot c_p \cdot \Delta T \]  
Où \( L_f \) = chaleur latente de fusion (ex : 272 kJ/kg pour Al).  

---

## **3. Alliages Binaires : Fondements des Diagrammes de Phases**  
### 3.1 Miscibilité Totale (Type I)  
**Conditions** :  
- Rayons atomiques ≤ 15% de différence,  
- Même structure cristalline.  

**Exemple** :  
- **Cu-Ni** : Solution solide continue.  
- **Diagramme** : Une seule phase solide α entre liquidus et solidus.  

### 3.2 Systèmes Eutectiques (Type II)  
**Caractéristiques** :  
- Point eutectique = **triple point** (L ↔ α + β).  
- **Microstructure** : Mélange lamellaire (ex : perlite dans l’acier).  

**Calcul des fractions** (règle du levier) :  
\[ f_\alpha = \frac{C_L - C_0}{C_L - C_\alpha} \]  

**Exemple concret** :  
- **Alliage Pb-Sn (61.9% Sn)** :  
  - Température eutectique = 183°C,  
  - Résistance mécanique optimale pour les soudures.  

### 3.3 Systèmes Péritectiques (Type III)  
**Réaction** : \( L + \alpha \leftrightarrow \beta \) à température constante.  
**Application** :  
- **Aciers inoxydables** : Formation de phase γ (austénite) à haute température.  

---

## **4. Solutions Solides : Des Atomes en Interaction**  
### 4.1 Solutions d’Insertion  
**Mécanisme** : Atomes petits (C, N, H) logés dans les **sites interstitiels** :  
- **CFC** : Sites octaédriques (ex : C dans Feγ avec rayon 0.414r).  
- **CC** : Sites tétraédriques (ex : C dans Feα, limité à 0.022% max).  

**Impact mécanique** :  
- Durcissement par **distorsion du réseau** (loi de Hall-Petch).  

### 4.2 Solutions de Substitution  
**Règles de Hume-Rothery** :  
1. **Rayon atomique** : Δr ≤ 15% (ex : Cu/Ag = 128pm/144pm → Δ=12.5%).  
2. **Valence** : Identique (ex : Cu⁺¹ et Au⁺¹).  
3. **Électronégativité** : Δχ ≤ 0.4 (ex : Al/Fe = 1.61/1.83 → Δ=0.22).  

**Échec des règles** :  
- **Zn/Cu** (Δr=4%) mais miscibilité limitée → structure CFC/HC incompatibles.  

---

## **5. Défauts Cristallins : Imperfections Structurantes**  
### 5.1 Défauts Ponctuels  
| Type          | Cause                          | Impact                           |  
|---------------|--------------------------------|----------------------------------|  
| Lacune         | Vibrations thermiques          | Augmente la diffusivité (eq. d’Arrhenius) |  
| Interstitiel   | Trempe rapide                  | Durcissement (ex : aciers au carbone) |  

**Équation de diffusion** (1ère loi de Fick) :  
\[ J = -D \frac{\partial C}{\partial x} \]  
Où \( D = D_0 e^{-Q/(RT)} \) (ex : \( D_C^{Feγ} = 2.0 \times 10^{-5} \, \text{cm}^2/\text{s} \) à 900°C).  

### 5.2 Dislocations et Mobilité  
**Dislocation coin** :  
- **Vecteur de Burgers (b)** ⊥ ligne de dislocation.  
- **Mouvement** : Glissement (slip) → déformation plastique.  

**Dislocation vis** :  
- **Vecteur de Burgers** // ligne.  
- **Mouvement** : Monte-Carlo (nécessite diffusion).  

![Dislocation](https://via.placeholder.com/500x300?text=Schéma+dislocation+coin+et+mécanisme+de+glissement)  

---

## **6. Diagramme Fer-Carbone : Clef des Aciers et Fontes**  
### 6.1 Phases Clés  
| Phase       | Structure | %C Max | Propriétés                  |  
|-------------|-----------|--------|-----------------------------|  
| Ferrite (α) | CC        | 0.022% | Douce, ductile (HV=80)      |  
| Austenite (γ)| CFC      | 2.14%  | Malléable à chaud           |  
| Cémentite   | Ortho.    | 6.67%  | Dure, fragile (HV=800)      |  

### 6.2 Transformations Critiques  
- **Eutectoïde** (727°C) : \( \gamma \leftrightarrow \alpha + \text{Cémentite} \) → **Perlite**.  
- **Eutectique** (1147°C) : \( L \leftrightarrow \gamma + \text{Cémentite} \) → **Ledeburite**.  

**TTT (Time-Temperature-Transformation)** :  
![Diagramme TTT](https://via.placeholder.com/600x400?text=Courbes+TTT+pour+un+acier+eutectoïde)  

---

## **7. Traitements Thermiques : Maîtrise des Microstructures**  
### 7.1 Recuit  
- **Objectif** : Éliminer les contraintes → structure équilibrée.  
- **Procédé** :  
  1. Chauffer à \( T > A_3 \) (ex : 950°C pour acier 0.8%C),  
  2. Maintien (1h/cm d’épaisseur),  
  3. Refroidissement lent (20°C/h).  

### 7.2 Trempe et Revenu  
- **Martensite** :  
  - Structure **CC tetragonale** (c/a > 1) → dureté HV=700.  
  - **Problème** : Fragilité → nécessite un revenu (200-600°C).  

**Courbe de revenu** :  
- **Étape 1** (200°C) : Précipitation de ε-carbure.  
- **Étape 2** (400°C) : Transformation de la martensite en troostite.  

---

## **8. Corrosion : Combat Électrochimique**  
### 8.1 Pile de Corrosion  
**Composants** :  
- **Anode** : \( \text{Fe} \rightarrow \text{Fe}^{2+} + 2e^- \) (\( E^\circ = -0.44 \, \text{V} \)),  
- **Cathode** : \( \text{O}_2 + 2\text{H}_2\text{O} + 4e^- \rightarrow 4\text{OH}^- \) (\( E^\circ = +0.40 \, \text{V} \)).  

**Potentiel de corrosion** :  
\[ E_{corr} = \frac{E_a + E_c}{2} \]  

### 8.2 Stratégies de Protection  
| Méthode               | Principe                          | Exemple                  |  
|-----------------------|-----------------------------------|--------------------------|  
| Revêtement (Zn)       | Anode sacrificielle               | Coques de navires        |  
| Passivation (Cr₂O₃)   | Couche oxyde protectrice          | Acier inox 316L          |  
| Inhibiteurs (NaNO₂)   | Blocage des sites réactifs        | Circuits de refroidissement |  

---

## **9. Études de Cas Industriels**  
### 9.1 Aéronautique : Alliages d’Aluminium  
- **7075-T6** (Al-Zn-Mg-Cu) :  
  - \( \sigma_y = 500 \, \text{MPa} \),  
  - Traitement : Solution heat treatment + aging artificiel.  

### 9.2 Biomédical : Titane Grade 5  
- **Ti-6Al-4V** :  
  - Compatibilité osseuse (module d’Young = 110 GPa vs os = 30 GPa),  
  - Usinage par électro-érosion.  

---

## **10. Annexes**  
### 10.1 Tableaux de Données  
| Métal    | \( T_f \) (°C) | \( \rho \) (g/cm³) | \( \sigma_y \) (MPa) |  
|----------|----------------|--------------------|----------------------|  
| Fer      | 1538           | 7.87               | 50-250               |  
| Aluminium| 660            | 2.70               | 20-500               |  
| Titane   | 1668           | 4.51               | 200-1400             |  

### 10.2 Références  
- Askeland, *The Science and Engineering of Materials*, 7e éd.  
- *ASM Handbook*, Volume 4 : Heat Treating.  



Solidus : température à laquelle le liquide commence à se solidifier. (L → L+α) dans le diagramme eutectique

A la fin, on est 100% solide. (L+α → α) dans le diagramme eutectique
La différence avant et après la transformation est la chaleur latente de solidification.
L'alliage alpha beta est plus dur que l'alliage alpha seul.
On forme du beta en refroidissant plus vite.
On forme du alpha en refroidissant plus lentement.
On peut aussi former du beta en chauffant plus vite.
On peut aussi former du alpha en chauffant plus lentement.


Le point E: tant qu'on est au dessus du poitn E, on a que du liquide. Des qu'on le franchis, tout est solide.
2 structures possibles: lamellaire ou globuleuse.


Le diagramme de phase est un diagramme de température en fonction de la composition.
On peut avoir des alliages qui sont des solutions solides. On peut avoir des alliages qui sont des mélanges de phases.

La composition en B de tout ce qui est liquide 

Règle des segments inverses: si on a un segment qui est plus long que l'autre, alors la phase qui est plus proche du segment le plus long est plus présente. 


Composé intermétallique : une barre verticale fixe pour toute température dans le diagramme. 