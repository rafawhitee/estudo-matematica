import numpy as np
import matplotlib.pyplot as plt

# Definindo a matriz de pixels
pixels = np.array([
    [0, 128, 255],
    [64, 192, 128],
    [255, 64, 0]
])

# Plotando a imagem
plt.imshow(pixels, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.title("Imagem em Escala de Cinza de 3x3 Pixels")
plt.show()