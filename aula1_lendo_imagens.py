import cv2

# Ler imagem
imagem = cv2.imread('assets/fotos/cat_large.jpg')

# Mostrar imagem
cv2.imshow('Imagem CAT', imagem)

# Aguardar tecla para fechar
cv2.waitKey(0)