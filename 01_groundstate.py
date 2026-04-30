from ase.build import mx2
from gpaw import GPAW, FermiDirac

# 1. Crear MoS2 monocapa 2H en supercelda 3x3
structure = mx2(
    formula='MoS2',
    kind='2H',
    a=3.184,
    thickness=3.127,
    size=(3, 3, 1),
    vacuum=7.5
)

structure.pbc = (1, 1, 1)

# 2. Crear una vacancia de azufre
# El tutorial borra el átomo con índice 2
del structure[2]

# 3. Cálculo DFT de estado base
calc = GPAW(
    mode='lcao',
    basis='dzp',
    xc='LDA',
    kpts=(4, 4, 1),
    occupations=FermiDirac(0.01),
    txt='gs_3x3_defect.txt'
)

structure.calc = calc
energy = structure.get_potential_energy()

print("Energía total =", energy, "eV")

# Guarda todo, incluyendo funciones de onda
calc.write('gs_3x3_defect.gpw', 'all')
