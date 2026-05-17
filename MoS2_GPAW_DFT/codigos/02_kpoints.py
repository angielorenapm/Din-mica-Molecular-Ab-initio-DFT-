from ase.build import mx2
from gpaw.unfold import find_K_from_k
import pickle

a = 3.184

# Celda primitiva de MoS2
PC = mx2(
    formula='MoS2',
    kind='2H',
    a=a,
    thickness=3.127,
    vacuum=7.5
).get_cell(complete=True)

# Camino de alta simetría: M -> K -> Gamma
bp = PC.get_bravais_lattice().bandpath('MKG', npoints=24)

x, X, labels = bp.get_linear_kpoint_axis()

# Matriz de transformación: celda primitiva -> supercelda 3x3
M = [[3, 0, 0],
     [0, 3, 0],
     [0, 0, 1]]

Kpts = []

for k in bp.kpts:
    K = find_K_from_k(k, M)[0]
    Kpts.append(K)

with open('path_data.pckl', 'wb') as f:
    pickle.dump((bp.kpts, x, X, labels, M, Kpts), f)

print("Número de puntos k:", len(bp.kpts))
print("Número de puntos K:", len(Kpts))
print("Archivo creado: path_data.pckl")
