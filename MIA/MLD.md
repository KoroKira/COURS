# **MLD – MODÈLE LOGIQUE DE DONNÉES COMPLET**

---

### 🟦 **VOL**
- **id_vol** (PK)  
- date_vol  
- heure_depart  
- heure_arrivee  
- id_avion (FK → AVION.id_avion)  
- id_aeroport_depart (FK → AEROPORT.id_aeroport)  
- id_aeroport_arrivee (FK → AEROPORT.id_aeroport)  
- id_meteo (FK → METEO.id_meteo)

---

### 🟦 **AEROPORT**
- **id_aeroport** (PK)  
- code_OACI  
- code_IATA  
- nom_aeroport  
- ville  
- pays

---

### 🟦 **METEO**
- **id_meteo** (PK)  
- temperature  
- vent  
- pression  
- precipitation  
- visibilite

---

### 🟦 **COORDONNEE**
- **id_coord** (PK)  
- latitude  
- longitude  
- altitude  
- timestamp  
- id_vol (FK → VOL.id_vol)

---

### 🟦 **PARAMETRE_VOL**
- **id_parametre** (PK)  
- nom_parametre  
- id_type_donnee (FK → TYPE_DONNEE.id_type_donnee)  
- id_phase_vol (FK → PHASE_VOL.id_phase)  
- id_vol (FK → VOL.id_vol)

---

### 🟦 **TYPE_DONNEE**
- **id_type_donnee** (PK)  
- libelle  
- description

---

### 🟦 **PHASE_VOL**
- **id_phase** (PK)  
- nom_phase  
- ordre_phase

---

### 🟦 **PILOTE**
- **id_pilote** (PK)  
- nom  
- prenom  
- licence  
- experience_annees

---

### 🟦 **VOL_PILOTE** *(association N:N entre VOL et PILOTE)*
- **id_vol** (PK, FK → VOL.id_vol)  
- **id_pilote** (PK, FK → PILOTE.id_pilote)  
- role

---

### 🟦 **AVION**
- **id_avion** (PK)  
- immatriculation  
- modele  
- constructeur  
- capacite  
- annee_mise_service

---

### 🟦 **MAINTENANCE**
- **id_maintenance** (PK)  
- date_maintenance  
- type_maintenance  
- description  
- realisee_par  
- id_avion (FK → AVION.id_avion)

---

### 🟦 **INCIDENT**
- **id_incident** (PK)  
- description  
- gravite  
- date_incident  
- detecte_par  
- id_vol (FK → VOL.id_vol)

---

### 🟦 **EVENEMENT_SYSTEME**
- **id_event** (PK)  
- code_event  
- description  
- criticite  
- id_vol (FK → VOL.id_vol)

---

### 🟦 **UTILISATEUR**
- **id_utilisateur** (PK)  
- nom  
- prenom  
- email  
- role

---

### 🟦 **ANALYSE_VOL** *(association N:N entre UTILISATEUR et VOL)*
- **id_utilisateur** (PK, FK → UTILISATEUR.id_utilisateur)  
- **id_vol** (PK, FK → VOL.id_vol)  
- date_analyse  
- observations

---

### 🟦 **ANALYSE_INCIDENT** *(association N:N entre UTILISATEUR et INCIDENT)*
- **id_utilisateur** (PK, FK → UTILISATEUR.id_utilisateur)  
- **id_incident** (PK, FK → INCIDENT.id_incident)  
- date_analyse  
- recommandations

---