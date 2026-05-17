# Simulación de MoS₂ con GPAW

Esta carpeta contiene los códigos, archivos de cálculo, resultados y referencias asociados a una simulación DFT de MoS₂ usando GPAW y ASE.

## Estructura de la carpeta

- `codigos/`: scripts de Python usados para ejecutar la simulación.
- `datos_gpaw/`: archivos generados por GPAW, incluyendo archivos `.gpw`, `.txt` y `.pckl`.
- `resultados/`: imágenes, gráficas y salidas visuales del cálculo.
- `articulos/`: artículos y documentos teóricos relacionados con DFT, teoría de bandas, zonas de Brillouin y MoS₂.
- `presentacion/`: material de presentación o documentos del semillero.

## Flujo general de la simulación

1. `01_groundstate.py`: calcula el estado fundamental del sistema.
2. `02_k_points.py`: define o analiza los puntos k.
3. `03_bands.py`: calcula la estructura de bandas.
4. `04_unfold_plot.py`: genera o visualiza el unfolding de bandas.

## Archivos principales

- `gs_3x3_defect.gpw`: archivo de reinicio o estado guardado de GPAW.
- `gs_3x3_defect.txt`: salida textual del cálculo.
- `path_data.pckl`: datos de la trayectoria en el espacio recíproco.
- `sf_3x3_defect.pckl`: datos asociados al spectral function.
- `weights_3x3_defect.pckl`: pesos usados en el análisis de unfolding.
- `sf_3x3_defect_spec.png`: imagen del resultado de la estructura de bandas/unfolding. 
