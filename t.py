import pandas as pd
import openpyxl

# Feuille 1 : BEGES DETAILLE
data_be = [
    {
        "ID de la donnée": "C1",
        "Catégorie": "Immobilisation",
        "Sous-catégorie": "Bâtiments - Commercial",
        "Nom de la donnée d'activité": "Surface commerciale en béton",
        "Poste d'émission (selon norme ISO14001)": "Immobilisation-Bâtiments",
        "Valeur 2021": 1500,
        "Unité": "m²",
        "Incertitude de la donnée d'activité (%)": 5,
        "Information": "Donnée chantier",
        "Nom du facteur d’émission": "FE Béton",
        "Valeur du facteur d’émission": "580 kgCO2e/m² (lifetime)",
        "Incertitude du facteur d’émission (%)": 5,
        "Valeur Emissions (Kg CO2e)": round(1500*(580/30),0),
        "Incertitude globale (%)": 10
    },
    {
        "ID de la donnée": "C2",
        "Catégorie": "Immobilisation",
        "Sous-catégorie": "Bâtiments - Commercial",
        "Nom de la donnée d'activité": "Surface commerciale en structure métallique",
        "Poste d'émission (selon norme ISO14001)": "Immobilisation-Bâtiments",
        "Valeur 2021": 1000,
        "Unité": "m²",
        "Incertitude de la donnée d'activité (%)": 5,
        "Information": "Donnée chantier",
        "Nom du facteur d’émission": "FE Métallique",
        "Valeur du facteur d’émission": "580 kgCO2e/m² (lifetime)",
        "Incertitude du facteur d’émission (%)": 5,
        "Valeur Emissions (Kg CO2e)": round(1000*(580/30),0),
        "Incertitude globale (%)": 10
    },
    {
        "ID de la donnée": "B1",
        "Catégorie": "Immobilisation",
        "Sous-catégorie": "Bureaux",
        "Nom de la donnée d'activité": "Surface de bureaux en structure métallique",
        "Poste d'émission (selon norme ISO14001)": "Immobilisation-Bâtiments",
        "Valeur 2021": 800,
        "Unité": "m²",
        "Incertitude de la donnée d'activité (%)": 5,
        "Information": "Donnée chantier",
        "Nom du facteur d’émission": "FE Métallique Bureaux",
        "Valeur du facteur d’émission": "700 kgCO2e/m² (lifetime)",
        "Incertitude du facteur d’émission (%)": 5,
        "Valeur Emissions (Kg CO2e)": round(800*(700/30),0),
        "Incertitude globale (%)": 10
    },
    {
        "ID de la donnée": "COM1",
        "Catégorie": "Immobilisation",
        "Sous-catégorie": "Parkings/Communs",
        "Nom de la donnée d'activité": "Parking",
        "Poste d'émission (selon norme ISO14001)": "Immobilisation-Commun",
        "Valeur 2021": 10000,
        "Unité": "m²",
        "Incertitude de la donnée d'activité (%)": 5,
        "Information": "Donnée chantier",
        "Nom du facteur d’émission": "FE Parking",
        "Valeur du facteur d’émission": "300 kgCO2e/m² (lifetime)",
        "Incertitude du facteur d’émission (%)": 5,
        "Valeur Emissions (Kg CO2e)": round(10000*(300/30),0),
        "Incertitude globale (%)": 10
    },
    {
        "ID de la donnée": "COM2",
        "Catégorie": "Immobilisation",
        "Sous-catégorie": "Voirie/Communs",
        "Nom de la donnée d'activité": "Voirie de circulation",
        "Poste d'émission (selon norme ISO14001)": "Immobilisation-Commun",
        "Valeur 2021": 2000,
        "Unité": "m²",
        "Incertitude de la donnée d'activité (%)": 5,
        "Information": "Donnée chantier",
        "Nom du facteur d’émission": "FE Voirie",
        "Valeur du facteur d’émission": "400 kgCO2e/m² (lifetime)",
        "Incertitude du facteur d’émission (%)": 5,
        "Valeur Emissions (Kg CO2e)": round(2000*(400/30),0),
        "Incertitude globale (%)": 10
    }
]
df_be = pd.DataFrame(data_be)

# Feuille 2 : synthèse globale (données à remplacer)
data_syn = [
    {"Catégorie": "Achats", "Sous-catégorie": "Achats", "Somme de Valeur Emissions (Kg CO2e)": "0,03%"},
    {"Catégorie": "", "Sous-catégorie": "Achats de matières premières", "Somme de Valeur Emissions (Kg CO2e)": "12,06%"},
    {"Catégorie": "", "Sous-catégorie": "Achats de produits", "Somme de Valeur Emissions (Kg CO2e)": "10,60%"},
    {"Catégorie": "", "Sous-catégorie": "Achats de services", "Somme de Valeur Emissions (Kg CO2e)": "9,92%"},
    {"Catégorie": "Achats", "Sous-catégorie": "Total pour Achats", "Somme de Valeur Emissions (Kg CO2e)": "32,61%"},
    {"Catégorie": "Déchets", "Sous-catégorie": "Déchets", "Somme de Valeur Emissions (Kg CO2e)": "0,05%"},
    {"Catégorie": "", "Sous-catégorie": "Déchets non recyclés", "Somme de Valeur Emissions (Kg CO2e)": "1,20%"},
    {"Catégorie": "", "Sous-catégorie": "Déchets recyclés", "Somme de Valeur Emissions (Kg CO2e)": "0,31%"},
    {"Catégorie": "Déchets", "Sous-catégorie": "Total pour Déchets", "Somme de Valeur Emissions (Kg CO2e)": "1,57%"},
    {"Catégorie": "Déplacements", "Sous-catégorie": "Ecole de Production", "Somme de Valeur Emissions (Kg CO2e)": "0,00%"},
    {"Catégorie": "", "Sous-catégorie": "Formation Apprentissage", "Somme de Valeur Emissions (Kg CO2e)": "17,13%"},
    {"Catégorie": "", "Sous-catégorie": "Formation Continue", "Somme de Valeur Emissions (Kg CO2e)": "1,01%"},
    {"Catégorie": "", "Sous-catégorie": "Formation Intégré", "Somme de Valeur Emissions (Kg CO2e)": "12,71%"},
    {"Catégorie": "", "Sous-catégorie": "Formation Ouvert", "Somme de Valeur Emissions (Kg CO2e)": "3,55%"},
    {"Catégorie": "", "Sous-catégorie": "Journées d'Intégration", "Somme de Valeur Emissions (Kg CO2e)": "0,03%"},
    {"Catégorie": "", "Sous-catégorie": "Journées Portes Ouvertes", "Somme de Valeur Emissions (Kg CO2e)": "0,33%"},
    {"Catégorie": "", "Sous-catégorie": "Salariés", "Somme de Valeur Emissions (Kg CO2e)": "8,26%"},
    {"Catégorie": "Déplacements", "Sous-catégorie": "Total pour Déplacements", "Somme de Valeur Emissions (Kg CO2e)": "43,02%"},
    {"Catégorie": "Énergie", "Sous-catégorie": "Combustible fossile", "Somme de Valeur Emissions (Kg CO2e)": "6,46%"},
    {"Catégorie": "", "Sous-catégorie": "Électricité", "Somme de Valeur Emissions (Kg CO2e)": "1,75%"},
    {"Catégorie": "Énergie", "Sous-catégorie": "Total pour Énergie", "Somme de Valeur Emissions (Kg CO2e)": "8,21%"},
    {"Catégorie": "Hors énergie", "Sous-catégorie": "Climatisation", "Somme de Valeur Emissions (Kg CO2e)": "0,18%"},
    {"Catégorie": "Hors énergie", "Sous-catégorie": "Total pour Hors énergie", "Somme de Valeur Emissions (Kg CO2e)": "0,18%"},
    {"Catégorie": "Immobilisation", "Sous-catégorie": "Bâtiments", "Somme de Valeur Emissions (Kg CO2e)": "9,71%"},
    {"Catégorie": "", "Sous-catégorie": "Equipements", "Somme de Valeur Emissions (Kg CO2e)": "2,86%"},
    {"Catégorie": "", "Sous-catégorie": "Informatique", "Somme de Valeur Emissions (Kg CO2e)": "1,02%"},
    {"Catégorie": "", "Sous-catégorie": "Mobiliers", "Somme de Valeur Emissions (Kg CO2e)": "0,23%"},
    {"Catégorie": "", "Sous-catégorie": "Parkings", "Somme de Valeur Emissions (Kg CO2e)": "0,59%"},
    {"Catégorie": "Immobilisation", "Sous-catégorie": "Total pour Immobilisation", "Somme de Valeur Emissions (Kg CO2e)": "14,41%"},
    {"Catégorie": "", "Sous-catégorie": "Total général", "Somme de Valeur Emissions (Kg CO2e)": "100,00%"}
]
df_syn = pd.DataFrame(data_syn)

# Feuille 3 : Nomenclature des postes d'émissions
data_p = [
    {"N° Poste": "1.1", "Poste d'émissions": "Emissions directes des sources fixes de combustion"},
    {"N° Poste": "1.2", "Poste d'émissions": "Emissions directes des sources mobile à moteur thermique"},
    {"N° Poste": "1.3", "Poste d'émissions": "Emissions directes des procédés hors énergie"},
    {"N° Poste": "1.4", "Poste d'émissions": "Emissions directes fugitives"},
    {"N° Poste": "1.5", "Poste d'émissions": "Emissions issues de la biomasse (sols et forêts)"},
    {"N° Poste": "2.1", "Poste d'émissions": "Emissions indirectes liées à la consommation d'électricité"},
    {"N° Poste": "2.2", "Poste d'émissions": "Emissions indirectes liées à la consommation d'énergie autre que l'électricité"},
    {"N° Poste": "3.1", "Poste d'émissions": "Transport de marchandise amont"},
    {"N° Poste": "3.2", "Poste d'émissions": "Transport des marchandises aval"},
    {"N° Poste": "3.3", "Poste d'émissions": "Déplacements domicile-travail"},
    {"N° Poste": "3.4", "Poste d'émissions": "Déplacements des visiteurs et des clients"},
    {"N° Poste": "3.5", "Poste d'émissions": "Déplacements professionnels"},
    {"N° Poste": "4.1", "Poste d'émissions": "Achats de biens"},
    {"N° Poste": "4.2", "Poste d'émissions": "Immobilisations de biens"},
    {"N° Poste": "4.3", "Poste d'émissions": "Gestion des déchets"},
    {"N° Poste": "4.4", "Poste d'émissions": "Actifs en leasing amont"},
    {"N° Poste": "4.5", "Poste d'émissions": "Achats de services"},
    {"N° Poste": "5.1", "Poste d'émissions": "Utilisation des produits vendus"},
    {"N° Poste": "5.2", "Poste d'émissions": "actifs en leasing aval"},
    {"N° Poste": "5.3", "Poste d'émissions": "Fin de vie des produits vendus"},
    {"N° Poste": "5.4", "Poste d'émissions": "Investissements"},
    {"N° Poste": "6.1", "Poste d'émissions": "Autres émissions directes"}
]
df_postes = pd.DataFrame(data_p)

# Feuille 4 : Immobilisations et amortissements
data_imm = [
    {"Catégorie d'immobilisation": "Bâtiments neufs", "Nb d'années d'amortissement": 30},
    {"Catégorie d'immobilisation": "Rénovation de bâtiment (constructions)", "Nb d'années d'amortissement": 10},
    {"Catégorie d'immobilisation": "Machine Ecole de Prod", "Nb d'années d'amortissement": 8},
    {"Catégorie d'immobilisation": "Equipement laboratoires", "Nb d'années d'amortissement": 5},
    {"Catégorie d'immobilisation": "Mobilier", "Nb d'années d'amortissement": 5}
]
df_imm = pd.DataFrame(data_imm)

# Écriture dans un fichier Excel à plusieurs feuilles
with pd.ExcelWriter("BEGES_exercice.xlsx", engine="openpyxl") as writer:
    df_be.to_excel(writer, sheet_name="BEGES DETAILLE", index=False)
    df_syn.to_excel(writer, sheet_name="synthèse globale", index=False)
    df_postes.to_excel(writer, sheet_name="Feuille 3", index=False)
    df_imm.to_excel(writer, sheet_name="Feuille 4", index=False)

print("Le fichier Excel 'BEGES_exercice.xlsx' a été généré.")