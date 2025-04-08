# **MCD COMPLET – GESTION DES VOLS**

---

## 🔷 **ENTITÉS PRINCIPALES**

---

### ✈️ VOL
- id_vol (PK)  
- date_vol  
- heure_depart  
- heure_arrivee  
- id_avion (FK)  
- id_aeroport_depart (FK)  
- id_aeroport_arrivee (FK)  
- id_meteo (FK)

---

### 🛬 AEROPORT
- id_aeroport (PK)  
- code_OACI  
- code_IATA  
- nom_aeroport  
- ville  
- pays  

---

### 🌦️ METEO
- id_meteo (PK)  
- temperature  
- vent  
- pression  
- precipitation  
- visibilite  

---

### 📡 COORDONNEE (Trajectoire)
- id_coord (PK)  
- latitude  
- longitude  
- altitude  
- timestamp  
- id_vol (FK)

---

### 📊 PARAMETRE_VOL
- id_parametre (PK)  
- nom_parametre  
- id_type_donnee (FK)  
- id_phase_vol (FK)  
- id_vol (FK)

---

### ⚙️ TYPE_DONNEE
- id_type_donnee (PK)  
- libelle (DFDR, CVR, Compute)  
- description  

---

### 🌀 PHASE_VOL
- id_phase (PK)  
- nom_phase (Taxi, Take-off…)  
- ordre_phase  

---

### 🧑‍✈️ PILOTE
- id_pilote (PK)  
- nom  
- prenom  
- licence  
- experience_annees  

---

### 👥 VOL_PILOTE *(Association N:N entre Vol et Pilote)*
- id_vol (FK)  
- id_pilote (FK)  
- role (commandant, copilote…)

---

### 🛠️ MAINTENANCE
- id_maintenance (PK)  
- date_maintenance  
- type_maintenance  
- description  
- realisee_par  
- id_avion (FK)

---

### 🛩️ AVION
- id_avion (PK)  
- immatriculation  
- modele  
- constructeur  
- capacite  
- annee_mise_service  

---

### 🚨 INCIDENT
- id_incident (PK)  
- description  
- gravite  
- date_incident  
- detecte_par (manuel, automatique)  
- id_vol (FK)

---

### 🔧 EVENEMENT_SYSTEME
- id_event (PK)  
- code_event  
- description  
- criticite  
- id_vol (FK)

---

### 🧑‍💻 UTILISATEUR
- id_utilisateur (PK)  
- nom  
- prenom  
- email  
- role (analyste, superviseur, admin)

---

### 📈 ANALYSE_VOL *(Association N:N entre Utilisateur et Vol)*
- id_utilisateur (FK)  
- id_vol (FK)  
- date_analyse  
- observations  

---

### ⚠️ ANALYSE_INCIDENT *(Association N:N entre Utilisateur et Incident)*
- id_utilisateur (FK)  
- id_incident (FK)  
- date_analyse  
- recommandations  

---

## 🔁 **RELATIONS (résumé)**

- VOL → AEROPORT (départ & arrivée) : N - 1  
- VOL → AVION : N - 1  
- VOL → METEO : 1 - 1  
- VOL → COORDONNEE : 1 - N  
- VOL → PARAMETRE_VOL : 1 - N  
- PARAMETRE_VOL → TYPE_DONNEE : N - 1  
- PARAMETRE_VOL → PHASE_VOL : N - 1  
- VOL → PILOTE : N - N (via VOL_PILOTE)  
- VOL → INCIDENT : 1 - N  
- VOL → EVENEMENT_SYSTEME : 1 - N  
- AVION → MAINTENANCE : 1 - N  
- UTILISATEUR → VOL : N - N (via ANALYSE_VOL)  
- UTILISATEUR → INCIDENT : N - N (via ANALYSE_INCIDENT)

