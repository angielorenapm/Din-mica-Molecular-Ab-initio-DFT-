from gpaw import GPAW
from gpaw.unfold import Unfold, plot_spectral_function
import pickle

with open('path_data.pckl', 'rb') as f:
    kpts, x, X, labels, M, Kpts = pickle.load(f)

unfold = Unfold(
    name='3x3_defect',
    calc='bands_3x3_defect.gpw',
    M=M,
    spinorbit=False
)

unfold.spectral_function(
    kpts=kpts,
    x=x,
    X=X,
    points_name=['M', 'K', 'G']
)

calc = GPAW('gs_3x3_defect.gpw', txt=None)
ef = calc.get_fermi_level()

plot_spectral_function(
    filename='sf_3x3_defect',
    color='blue',
    eref=ef,
    emin=-3,
    emax=3
)

print("Unfolding terminado.")
print("Busca archivos como sf_3x3_defect.png, sf_3x3_defect.pckl o weights_3x3_defect.pckl")
