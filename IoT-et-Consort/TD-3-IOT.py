#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import geocoder
from pyfiglet import Figlet 

# Configuration ASCII art (optionnel)
f = Figlet(font='slant')
print(f.renderText('GEOCODING PRO'))
print("🔍 Géocodeur d'adresses avec ArcGIS - @Desarcy\n")

def geocode_address(address):
    """Géocode une adresse avec ArcGIS et retourne les coordonnées"""
    try:
        g = geocoder.arcgis(address)
        if g.ok:
            return {
                'success': True,
                'address': g.address,
                'latitude': g.lat,
                'longitude': g.lng,
                'provider': 'ArcGIS'
            }
        else:
            return {'success': False, 'error': "Adresse introuvable"}
    except Exception as e:
        return {'success': False, 'error': f"Erreur réseau: {str(e)}"}

def main():
    while True:
        print("\n" + "="*50)
        address = input("Entrez une adresse (ou 'q' pour quitter) :\n> ")
        
        if address.lower() == 'q':
            print("\nÀ bientôt, globe-trotter ! 🌍✨")
            break

        result = geocode_address(address)
        
        if result['success']:
            print("\n✅ RÉSULTAT :")
            print(f"📍 Adresse : {result['address']}")
            print(f"🌐 Latitude : {result['latitude']}")
            print(f"🌐 Longitude : {result['longitude']}")
            print(f"⚙️ Source : {result['provider']}")
        else:
            print(f"\n❌ ERREUR : {result['error']}")

if __name__ == "__main__":
    # Installation automatique des dépendances manquantes
    try:
        import geocoder
    except ImportError:
        import os
        os.system('pip install geocoder')
    
    try:
        import pyfiglet
    except ImportError:
        import os
        os.system('pip install pyfiglet')
    
    main()

