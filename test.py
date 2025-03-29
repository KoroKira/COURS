import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Fichiers
input_file = "liens.txt"
output_alive = "liens_valides.txt"
output_dead = "liens_morts.txt"

# HTTP Headers pour éviter d'être bloqué par certains sites
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Bot/1.0; +https://example.com/bot)"
}

# Lire les liens
with open(input_file, "r") as f:
    liens = [line.strip() for line in f if line.strip()]

def check_link(lien):
    try:
        response = requests.get(lien, headers=headers, timeout=10, allow_redirects=True)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            titre = soup.title.string.strip() if soup.title and soup.title.string else "Sans titre"
            titre = titre.replace('\n', ' ').replace('\r', ' ').strip()
            return ("alive", lien, titre)
        else:
            return ("dead", lien, f"HTTP {response.status_code}")
    except Exception as e:
        return ("dead", lien, str(e))

# Multi-thread pour aller + vite
results = []

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(check_link, lien) for lien in liens]
    for future in tqdm(as_completed(futures), total=len(futures), desc="Scan des liens"):
        results.append(future.result())

# Écriture des résultats
with open(output_alive, "w", encoding="utf-8") as f_alive, open(output_dead, "w", encoding="utf-8") as f_dead:
    for status, lien, info in results:
        if status == "alive":
            f_alive.write(f"{info} - {lien}\n")
        else:
            f_dead.write(f"{lien} // {info}\n")

print("\n✅ Terminé ! Résultats dans :")
print(f" - {output_alive}")
print(f" - {output_dead}")