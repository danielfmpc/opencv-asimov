import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_img(titulo, img):
  cv2.imshow(titulo, img)

img = cv2.imread('assets/fotos/cats.jpg')
show_img('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# show_img('Cinza', cinza)

# cinza_hist = cv2.calcHist([cinza], [0], None, [256], [0, 256])
# plt.figure()
# plt.title('Histograma Cinza')
# plt.xlabel('Intervalos/Setores')
# plt.ylabel('# de Pixels')
# plt.plot(cinza_hist)
# plt.xlim([0, 256])
# plt.show()

mask = cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
show_img('Mascara', mask)

masked = cv2.bitwise_and(img, img, mask=mask)
show_img('Mascara na imagem', masked)

plt.figure()
plt.title('Histograma de cores, sem máscara')
plt.xlabel('Intervalos/Setores')
plt.ylabel('Número de Pixels')
colors = ['b', 'g', 'r']
print(masked.shape)
print(img.shape)
for channel, color in enumerate(colors):
  hist = cv2.calcHist([img], [channel], mask, [256], [0,256])
  plt.plot(hist, color=color)
  plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()