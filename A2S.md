# 1364 moodle (Mehdi TURKI)

Philippe FOURNIER, un expert en FPGA (BARRANDON) et Mehdi TURKI

## Plan de cours (Partie 1)

### Mise en contexte

Qu'est-ce qu'un système automatisé ?
Vers un système automatisé intelligent
La théorie des Automates
Machine à états finis (FSM)

Différence entre automatisé et automatique :

Automatisé : qui fonctionne sans intervention humaine
Automatique : qui fonctionne sans intervention humaine, mais qui peut être contrôlé par un humain

### Problématique : système d'étude

Application : smart irrigation pv system
Objectifs :
- Identifier/Compléter la partie commande et opérative (capteurs, préactionneurs, actionneurs)....
- Comment rendre ce système automatisé et intelligent ?
- Proposer une méthode de contrôle et de supervision SMART

Capteur d'hydrométrie, lumière, niveau de l'eau dans le réservoir, capteur de taux de charge des batteries (tension et courants), pression
Actionneurs : électrovannes, pompe, moteur, 
Partie intelligente : microcontrôleur (par exemple, un esp32, un FPGA, un raspberry pi, un arduino, un PLC), BMS (Battery Management System), HMI (Human Machine Interface), SCADA (Supervisory Control And Data Acquisition), IoT (Internet of Things).

### Mise en contexte :

Les fabricants intègrent de nouvelles technologies, notamment l'IoT, le cloud, l'analytique, l'IA et l'apprentissage automatique dans leurs installations de production et dans l'ensemble de leurs opérations

Ces usines intelligentes sont équipées de capteurs avancés, de dispositifs de communication, de systèmes de contrôle et de logiciels d'analyse de données qui permettent aux fabricants de surveiller, de contrôler et d'optimiser les performances de leurs opérations de production

### Qu'est-ce qu'un système automatisé ?

Un système composé d'une partie opérative et d'une partie commande interagissant avec l'environnement physique et humain, organisé dans le but de générer une valeur ajoutée à partir de matières premières (matière, énergie, informations)

### Vers un système automatisé intelligent

Un système automatisé intelligent est une solution technologique intégrée qui combine des capacités d'automatisation avancées avec des fonctionnalités intelligentes basées sur des technologies telles que l'IA, le machine learning et d'autres approches permettant l'analyse et la prise de décision automatisée

L'intelligence dans un système automatisé peut être introduite à différents niveaux :

un instrument intelligent qui intègre des fonctionnalités avancées supplémentaires visant à améliorer ses performances initiales.

Capteur et/ou Actionneur

Un système de contrôle/gestion automatisé doté de capacités avancées permettant de prendre des décisions plus complexes


### La théorie des Automates

La théorie des automates a ses racines dans les travaux de mathématiciens tels que David Hilbert, Alonzo Church et Alan Turing au début du 20e siècle

Un automate est défini comme un dispositif abstrait capable de traiter des mots d'un langage donné
L'objectif est de représenter des problèmes informatiques sous forme de langage où chaque instance du problème est représentée par un mot


### Machine à états finis (FSM)

Un automate fini ou machine à état fini est un modèle mathématique de calcul utilisé dans de nombreux domaines : conception de programmes informatiques, circuits logiques, protocoles de communication, etc.

Un automate fini est susceptible d'être :
dans un nombre fini d'états
dans un seul état à la fois

La FSM sera définie par la liste de ses états et ses conditions de transition

L'état où il se trouve est appelé l'état courant. Le passage d'un état à un autre est dirigé par un événement (ou une condition) appelé une transition



### FSM --> diagramme a états (SysML)

La FSM est le concept ou le modèle théorique qui définit le comportement d'un système en termes d'états et de transitions.
Le diagramme d'états est la représentation visuelle de ce modèle, facilitant la compréhension et son analyse.

De nombreux éditeurs d'outils de modélisation prennent en charge SysML, que ce soit de manière complète ou partielle :
- Rational Rhapsody
- Papyrus
- MagicDraw
- Enterprise Architect

Il y a un outil en ligne pour cela : [draw.io](https://www.draw.io/)

Sur Matlab, on utilisera StateFlow.



FSM

Chaque état est représenté par un sommet (visualisé par un cercle)

Les arcs (flèches) montrent les transitions entre les états

une FSM est la donnée d'un quintuplet A: (Q, Σ, δ, q0, F) où : 
- Q est un ensemble fini d'états
- Σ est un ensemble fini de symboles d'entrée
- δ est une fonction de transition
- q0 est l'état initial
- F est un ensemble d'états finaux








### Technologie (API, µC, FPGA,...)

API : Application Programming Interface
µC : microcontrôleur
FPGA : Field Programmable Gate Array



Technologie microcontroleur: présentation

Système informatique entièrement réalisé sur un circuit intégré (circuit de silicium dans lequel on a intégré les éléments nécéssaires pour les rendre opérationnels)

Système informatique: composition ?

Mémoire vive + mémoire morte
Interface pour les entrées sorties
    Numérique: TOR, Comptage, fréquence, ...
    Analogique; CAN, CNA
Interface de communication
    Liaisons séries synchrone ou asynchrone
Base de temps, Timer, ...
Oscillateur, alimentation
Programmation, débug

Histoire: 

années 1980 environ, plus de transsitors: 
- plus de puissance de calculs
- plus de fonctionnalités, plus d'intégrations

Intégration d'un microprocesseur +:
- Mémoires (RAM, ROM, EEPROM)
- Horloge
- GPIO = E/S
- Communications (I2C, SPI, UART, USB, Ethernet, ...)
- Timer (compteurs, OC, IC, PWM, Watchdog, ...)
- Convertisseurs (ADC, DAC, Comparateur, ...)


Carte Arduino:

Carte électronique avec 2 microcontroleurs:
1x ATMega16U2-MU = interface USB
1x Atmel/Microchip ATMega328-PU

Taille: 8 bits
ISA: spécifique Atmel
Vitesse: 16 MHz
Mémoire: 32 Ko de flash, 2 Ko de SRAM, 1 Ko d'EEPROM
Timer: 2x8 bits, 1x16 bits, 6xPWM
Convertisseur: 1x10 bits, 6 canaux
Communication: 1xI2C, 1xSPI, 1xUART

Caractéristiques de la technologie de microcontroleurs:

Taille: 4-64 bits
Capacité mémoire: 
    - RAM: quelques octets à plusieurs kilo-octets
    - Flash: quelques kilo-octets à plusieurs méga-octets

Nombre de broches: nb entrées/sorties. de 6 à plusieurs centaines

Le marché est à moitié sur le 16 bits (info le plus important à retenir)

Les coûts:

Quelques centimes à plusieurs milliers d'euros

C = SBT (pour le fabricant)
Cout = Surface de silicium * nombre de broches * gamme température (tri ?)

C = SBT/Q (pour le client)
Q: facteur lié à la quantité (10 à 50 ou 100 ?)


STM32F411RE (en TP)

ARM Cortex-M4: microprocesseur 32 bits
Vitesse: 100 MHz
Mémoire: 512 Ko de flash, 128 Ko de SRAM
Timer: 3x16 bits, 2x32 bits, 12xPWM
Convertisseur: 2x12 bits, 16 canaux
Communication: 3xI2C, 3xSPI, 3xUART, 2xCAN, 2xUSB, 1xETH



Technologie FPGA: présentation

Schéma électronique numérique:
Des portes universelles (NAND/NOR)
Des bascules universelles (D/T)

Avantages:
Toutes les portes fonctionnent à la vitesse liée à la technologie (de l'ordre de la nanoseconde)
Toutes les bascules fonctionnent à la vitesse de l'horloge système (100MHz en TP)
Et surtout, tout fonctionne en parallèle


Imaginez: 

Ensemble de portes et de bascules (parfois plusieurs millions) (50 000 bascules en TP)
Cablées à la demande pour une fonction particulière (horloge du TP EN)
Cablé/configuré par transfert en mémoire RAM
(On a 2 catégorie de FPGA: ceux en RAM et ceux en Flash)

Circuit logique programmable (PLD)
CLB : Configurable Logic Block (LUT + Bascule FF)
Quelques milliers à quelques millions de CLB
Matrice d'interconnexion configurables
Basé sur des cellules SRAM (ultra rapide)

Exemple d'utilisation:
Missile Tomahawk (Raytheon)
Long Range Navy Cruise Missile (Lockheed Martin)

Moniteur ordinateur: Pivoting montor (landscape/portrait) (Dell)



Liens entre les domaines:

FPGA + microprocesseur + périphériques 
microprocesseur - soft core: NIOS, microBlaze, RISK-V
microprocesseurs intégrés:
    Power PC ou ARM: le Zynq

PSOC Cypress: Programmable System On Chip
microprocesseur + FPGA + Analogique (ampli, CAN, ...)

FPGA: domaines d'utilisation

Electronique numérique
Télécommunication; transport, traitement signaux
Réalisation de fonctions en vrai parallèle
Prototypage ASIC ou Circuit intégré (NVidia)
Test architecture processeur (graphique ?)
Reproduction ou émulation de circuits anciens
Rétro-gaming (Mister FPGA)
Réseau de neurones (IA)


Marché:

Xilinx (50%) (CA de environ 3 000 millions de dollars), racheté par AMD pour 50 milliards de dollars en 2022
Lattice SC (6;4%) (CA de 400 millions de dollars)
QuickLogic (1,5%) (CA de 100 millions de dollars)
Altera (33%) Racheté par INTEL pour 15 milliards de dollars en 2015
Achronix SC


Chaine de développement:

HDL -> Netlist -> Bitstream -> ADAPT => FPGA

Problème: Outils automatiques, Liées au fabriquants, Totalement obscurs


Langages:

Chaque fabriquant utilise son propre langage
==> Plusieurs dizaines de langages différents

Schéma graphiques

Puis ABEL-HDL, Verilog
Puis MOD ==> VHDL

VHDL (langage ADA)




Résumé:

Très forte puissance de calculs
Fonctionnement massivement parallèle
Très forte intégration
Très grande complexité
Copie ou modification très rapide

Mais:
Étude et développement complexe
Circuit intégrés couteux
Attention lors des manipulations !

Demain ? Intel/AMD