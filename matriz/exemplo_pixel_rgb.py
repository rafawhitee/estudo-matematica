import numpy as np
import matplotlib.pyplot as plt

# Definindo a matriz de pixels RGB
pixels_rgb = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 255]]
])

# Plotando a imagem RGB
plt.imshow(pixels_rgb)
plt.title("Imagem RGB de 2x2 Pixels")
plt.show()