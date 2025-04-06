import matplotlib.pyplot as plt

# Données
actions = ["Raccordement au RCU", "Panneaux photovoltaïques", "Réduction des déplacements étudiants", "Recyclage plastique avancé"]
gain_carbone = [25, 12.5, 6.5, 75]  # Moyenne des intervalles de gain
effort = [1, 2, 3, 2]  # Faible=1, Moyen=2, Élevé=3

# Création du graphique
plt.figure(figsize=(12, 8))
scatter = plt.scatter(effort, gain_carbone, color="skyblue", s=200, edgecolor="black", alpha=0.8)

# Ajout des étiquettes pour chaque point
for i, action in enumerate(actions):
    plt.text(effort[i] + 0.15, gain_carbone[i], action, fontsize=10, ha='left', va='center')

# Paramètres du graphique
plt.title("Graphique Gain/Effort des Actions d'Amélioration", fontsize=16, fontweight='bold')
plt.xlabel("Effort (Faible=1, Moyen=2, Élevé=3)", fontsize=14)
plt.ylabel("Gain carbone (tCO₂e/an)", fontsize=14)
plt.xticks([1, 2, 3], labels=["Faible", "Moyen", "Élevé"], fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Ajout d'une légende
plt.legend(["Actions"], loc="upper left", fontsize=12, frameon=True, edgecolor="black")

# Affichage
plt.show()