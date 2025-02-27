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

