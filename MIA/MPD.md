# **MPD – MODÈLE PHYSIQUE DE DONNÉES (SQL)**

---

### 🟦 **AEROPORT**
```sql
CREATE TABLE AEROPORT (
    id_aeroport INT PRIMARY KEY,
    code_OACI CHAR(4),
    code_IATA CHAR(3),
    nom_aeroport VARCHAR(100),
    ville VARCHAR(100),
    pays VARCHAR(100)
);
```

---

### 🟦 **AVION**
```sql
CREATE TABLE AVION (
    id_avion INT PRIMARY KEY,
    immatriculation VARCHAR(20),
    modele VARCHAR(50),
    constructeur VARCHAR(50),
    capacite INT,
    annee_mise_service INT
);
```

---

### 🟦 **METEO**
```sql
CREATE TABLE METEO (
    id_meteo INT PRIMARY KEY,
    temperature FLOAT,
    vent VARCHAR(50),
    pression FLOAT,
    precipitation VARCHAR(50),
    visibilite VARCHAR(50)
);
```

---

### 🟦 **PHASE_VOL**
```sql
CREATE TABLE PHASE_VOL (
    id_phase INT PRIMARY KEY,
    nom_phase VARCHAR(50),
    ordre_phase INT
);
```

---

### 🟦 **TYPE_DONNEE**
```sql
CREATE TABLE TYPE_DONNEE (
    id_type_donnee INT PRIMARY KEY,
    libelle VARCHAR(50),
    description TEXT
);
```

---

### 🟦 **VOL**
```sql
CREATE TABLE VOL (
    id_vol INT PRIMARY KEY,
    date_vol DATE,
    heure_depart TIME,
    heure_arrivee TIME,
    id_avion INT,
    id_aeroport_depart INT,
    id_aeroport_arrivee INT,
    id_meteo INT,
    FOREIGN KEY (id_avion) REFERENCES AVION(id_avion),
    FOREIGN KEY (id_aeroport_depart) REFERENCES AEROPORT(id_aeroport),
    FOREIGN KEY (id_aeroport_arrivee) REFERENCES AEROPORT(id_aeroport),
    FOREIGN KEY (id_meteo) REFERENCES METEO(id_meteo)
);
```

---

### 🟦 **COORDONNEE**
```sql
CREATE TABLE COORDONNEE (
    id_coord INT PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    altitude FLOAT,
    timestamp DATETIME,
    id_vol INT,
    FOREIGN KEY (id_vol) REFERENCES VOL(id_vol)
);
```

---

### 🟦 **PARAMETRE_VOL**
```sql
CREATE TABLE PARAMETRE_VOL (
    id_parametre INT PRIMARY KEY,
    nom_parametre VARCHAR(100),
    id_type_donnee INT,
    id_phase_vol INT,
    id_vol INT,
    FOREIGN KEY (id_type_donnee) REFERENCES TYPE_DONNEE(id_type_donnee),
    FOREIGN KEY (id_phase_vol) REFERENCES PHASE_VOL(id_phase),
    FOREIGN KEY (id_vol) REFERENCES VOL(id_vol)
);
```

---

### 🟦 **PILOTE**
```sql
CREATE TABLE PILOTE (
    id_pilote INT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    licence VARCHAR(50),
    experience_annees INT
);
```

---

### 🟦 **VOL_PILOTE**
```sql
CREATE TABLE VOL_PILOTE (
    id_vol INT,
    id_pilote INT,
    role VARCHAR(50),
    PRIMARY KEY (id_vol, id_pilote),
    FOREIGN KEY (id_vol) REFERENCES VOL(id_vol),
    FOREIGN KEY (id_pilote) REFERENCES PILOTE(id_pilote)
);
```

---

### 🟦 **MAINTENANCE**
```sql
CREATE TABLE MAINTENANCE (
    id_maintenance INT PRIMARY KEY,
    date_maintenance DATE,
    type_maintenance VARCHAR(50),
    description TEXT,
    realisee_par VARCHAR(100),
    id_avion INT,
    FOREIGN KEY (id_avion) REFERENCES AVION(id_avion)
);
```

---

### 🟦 **INCIDENT**
```sql
CREATE TABLE INCIDENT (
    id_incident INT PRIMARY KEY,
    description TEXT,
    gravite VARCHAR(50),
    date_incident DATE,
    detecte_par VARCHAR(50),
    id_vol INT,
    FOREIGN KEY (id_vol) REFERENCES VOL(id_vol)
);
```

---

### 🟦 **EVENEMENT_SYSTEME**
```sql
CREATE TABLE EVENEMENT_SYSTEME (
    id_event INT PRIMARY KEY,
    code_event VARCHAR(50),
    description TEXT,
    criticite VARCHAR(50),
    id_vol INT,
    FOREIGN KEY (id_vol) REFERENCES VOL(id_vol)
);
```

---

### 🟦 **UTILISATEUR**
```sql
CREATE TABLE UTILISATEUR (
    id_utilisateur INT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50)
);
```

---

### 🟦 **ANALYSE_VOL**
```sql
CREATE TABLE ANALYSE_VOL (
    id_utilisateur INT,
    id_vol INT,
    date_analyse DATE,
    observations TEXT,
    PRIMARY KEY (id_utilisateur, id_vol),
    FOREIGN KEY (id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
    FOREIGN KEY (id_vol) REFERENCES VOL(id_vol)
);
```

---

### 🟦 **ANALYSE_INCIDENT**
```sql
CREATE TABLE ANALYSE_INCIDENT (
    id_utilisateur INT,
    id_incident INT,
    date_analyse DATE,
    recommandations TEXT,
    PRIMARY KEY (id_utilisateur, id_incident),
    FOREIGN KEY (id_utilisateur) REFERENCES UTILISATEUR(id_utilisateur),
    FOREIGN KEY (id_incident) REFERENCES INCIDENT(id_incident)
);
```