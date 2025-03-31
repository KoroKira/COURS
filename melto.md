# Triangle de Pascal

Le triangle de Pascal est une construction mathématique qui donne des coefficients binomiaux. Voici un exemple de code Python pour générer un triangle de Pascal.

```python
def pascal_triangle(n):
    """Génère un triangle de Pascal avec n lignes."""
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    """Affiche le triangle de Pascal."""
    for row in triangle:
        print(" ".join(map(str, row)))

# Exemple d'utilisation
n = 5
triangle = pascal_triangle(n)
print_triangle(triangle)