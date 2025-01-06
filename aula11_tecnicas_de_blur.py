import cv2
import numpy as np

def show_image(titulo, img):
    cv2.imshow(titulo, img)


img = cv2.imread('assets/fotos/cat.jpg')
show_image('Original', img)

avarage = cv2.blur(img, (6,6))
show_image('Blur Avarage', avarage)

# Gaussian Blur
'''
A aplicação de uma função matemática a uma imagem para borrá-la
"It's like laying a translucent material like vellum on top of the image" ;
"É como colocar um material translúcido como pergaminho sobre a imagem"
- Kenton Waltz, fotógrafo
'''
gaussian = cv2.GaussianBlur(img, (7,7), 0)
show_image('Blur Gaussian', gaussian)

# Blur por mediana
'''
A média é a soma dos valores dividida pelo número de observações, 
enquanto a mediana é o valor central quando os dados são ordenados. 
A média é sensível a valores extremos, já a mediana não.
Segue os principios do conceitos de blur por média, quanto maior o ksize, maior o blur.
Tem uma pegada de desfoque diferente do blur por média, parece que desfoca em flocos, não como estamos acostumados
'''
median = cv2.medianBlur(img, 9)
show_image('Blur Median', median)

# Filtro Bilateral
# Edge preserving denoising filter
'''Um filtro bilateral é um filtro de suavização não linear, com preservação de bordas e redução de ruído para imagens. 
Ele substitui a intensidade de cada pixel por uma média ponderada dos valores de intensidade dos pixels próximos.
Visto que esse efeito reduz o ruído, testaremos com uma imagem com ruído

Primeiro temos que entender o que é Sigma no contexto de processamento de imagem:
Sigma define a quantidade de desfoque

cv2.bilateralFilter(imagem, d,  sigmaColor, sigmaSpace)
d -> kernel size ou ksize (que é o diametro de analise do modelo), quanto menor, mais custosa a análise
sigmaColor -> Filtra o Sigma no ColorSpace. 
    Um valor maior do parâmetro significa que as cores mais distantes dentro da vizinhança do pixel serão misturadas, resultando em áreas maiores de cor semi-igual
sigmaSpace -> Filtra o Sigma no espaço de coordenadas. 
    Um valor maior do parâmetro significa que os pixels mais distantes influenciarão uns aos outros (desde que suas cores sejam próximas o suficiente)
'''
img_noisy = cv2.imread('assets/fotos/noisy_image.jpg')
show_image('Noisy Image', img_noisy)

bilateral = cv2.bilateralFilter(img_noisy, 15, 75, 75)
show_image('Bilateral Filter', bilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()