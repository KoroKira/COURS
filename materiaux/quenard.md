# Les Composites

Matériau issu de l'association judicieuse de AU MOINS 2 matériaux de nature différente, non miscibles, dont l'objectif est de:
# - Améliorer les propriétés mécaniques, thermiques, électriques, optiques, magnétiques, etc. d'un matériau
# - Augmenter les caractéristiques mécaniques à masse constante
# - A caractéristique mécanique donnée, réduire la masse
# - Augmenter les caractéristiques mécaniques et dinimuer la masse
# - Augmenter la rigidité spécifique (déf: rapport entre la rigidité et la masse volumique, module de Young/masse volumique) et/ou la résistance spécifique (déf: rapport entre la résistance et la masse volumique, contrainte de rupture/masse volumique) des pièces


Dans ces deux matériaux, on a: le renfort et la matrice.

## Le renfort

Matériau, en général, de haute résistance mécanique, de forte rigidité, de grande fragilité. 
Ce matériau supporte la très grande majorité des contraintes appliquées sur l'ensemble des composites.

Exemples:
- Verre
- Céramique

(Val est dégagé au rang 0)

c'est quoi un matériau fragile ?

Un matériau fragile est un matériau qui se casse ou se fissure facilement sous l'effet d'une contrainte mécanique, sans subir de déformation plastique significative. Contrairement aux matériaux ductiles, qui peuvent se déformer avant de rompre, les matériaux fragiles présentent une rupture brutale et soudaine. Ils ne peuvent pas absorber beaucoup d'énergie avant de se briser. Des exemples de matériaux fragiles incluent le verre, la céramique et certains types de plastiques.
A retenir: pas de déformation plastique, rupture brutale et soudaine, pas d'absorption d'énergie avant de se briser.


## La matrice

Matériau, en général, très léger, qui sera de faible résistance mécanique, très déformable, de faible rigidité.
Elle assure 3 rôles:
- Elle lie les renforts entre eux pour en faire un massif
- Elle TRANSFERE les contraintes et les efforts appliquées sur le composite VERS les renforts
- Protéger les renforts des aggressions extérieures (chocs, humidité, chaleur, etc.)

Exemples:
- Résine
- Polymère

Quelle est la différence entre résistance mécanique et rigidité ?

La résistance mécanique et la rigidité sont deux propriétés distinctes des matériaux, bien qu'elles soient souvent confondues.
- La résistance mécanique fait référence à la capacité d'un matériau à supporter des charges ou des contraintes sans se rompre. Elle est généralement mesurée par la contrainte maximale qu'un matériau peut supporter avant de céder, exprimée en unités de pression (par exemple, pascals ou mégapascals). La résistance mécanique est importante pour déterminer si un matériau peut supporter les forces appliquées sans se déformer ou se briser.
- La rigidité, en revanche, est une mesure de la résistance d'un matériau à la déformation lorsqu'une force est appliquée. Elle est souvent exprimée par le module d'élasticité (ou module de Young), qui quantifie la relation entre la contrainte (force par unité de surface) et la déformation (changement de longueur ou de forme) dans la région élastique du matériau. Un matériau rigide se déforme peu sous l'effet d'une contrainte, tandis qu'un matériau moins rigide se déformera davantage.


---

Pour avoir un composite de propriété mécanique proches des propriétés calculées, il faut ABSOLUMENT garantir une adhérence RENFORT-MATRICE optimale. (Phrase à retenir)

"Quand on fait un béton armé, si le béton colle pas à l'armature métallique, c'est juste du béton, c'est pas du béton armé."

---

Quelques exemples de composite:
- Cas particulier: matrice céramiques ==> les bétons (Matrice ciment avec un renfort granulaire). On peut avoir du béton armé (ciment + granulaire + fibre métallique) ou du béton fibré (ciment + granulaire + fibre de verre)
- Acier à outils => Fe - C + Cr - V (carbures de chrome vanadium). En gros au lieu d'un acier basique, on a de la carbure dispersée dans la masse.
- Alu série 2000 => Al - Cu + Mg + Si (alliage d'aluminium). C'est quoi l'Alu 2000 ? C'est un Alu avec dedans du Cuivre pour renforcer les propriétés mécaniques car l'alu c'est mou.


Notre cours se concentrera sur les composites fibreux à matrice polymère (ex: composites à matrice époxy, polyester, etc.)
On va étudier plusieurs paramètres:
- La proportion des matériaux dans le composite
- Le sens des fibres
- Longueur de fibres


# I. Influence d la teneur en fibres:

Imaginons un unidirectionnel constitué de fibres en proportion Volumique Vf noyées dans une résine polymère. 
Qu'est ce qu'un unidirectionnel ? Sa microstructure est constituée de fibres orientées dans une seule direction.
Sa fibre fait TOUTE la longueur de la pièce, sinon c'est du composite à fibres courtes.
Entre les fibres, on a de la matrice (schéma à faire, rectangle rayé, les bandes c'est les fibres, les jointures de bandes, c'est la matrice. Indiques forces dans le sens des fibres)

Autant les céramiques sont utilisées QUE en compression, autant les composites fibres sont utilisés QUE en traction.
Les composites fibreux flambent très facilement en compression, mais ils sont très résistants en traction.

Courbe résistance élastique - effort mes couilles, bref le module de young 

Le module de Young du composite est donné par la relation de mélange:
Somme pondéré des modules de tous les constituants


Loi des mélanges: Grandeur physique donnée d'un composite qui est égale à la somme pondérée des mêmes grandeurs physiques de chacun de ses constituants.

$$ E_c = E_f * V_f + E_m * (1-V_f) $$

Résistance mécanique composite: Somme pondéré des résistances mécaniques de la fibre + la proportion volumique de la fibre + la résistance de la matrice

$$ R_mc = R_mf * V_f + Sigma_m * (1-V_f) $$

La déformation d'un composite dépend de la déformation des fibres seules.