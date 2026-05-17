from gpaw import GPAW
import pickle

with open('path_data.pckl', 'rb') as f:
    kpts, x, X, labels, M, Kpts = pickle.load(f)

calc_bands = GPAW('gs_3x3_defect.gpw').fixed_density(
    kpts=Kpts,
    symmetry='off',
    nbands=160,
    convergence={'bands': 130}
)

calc_bands.write('bands_3x3_defect.gpw', 'all')

print("Archivo creado: bands_3x3_defect.gpw")
