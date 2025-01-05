import cv2
import numpy as np

azul = (255, 0, 0)
verde = (0,255,0)
vermelho = (0,0,255)
roxo = (128, 0, 128)

# Ler as imagens
blank_img = np.zeros((500, 500, 3), dtype='uint8')

# 1. pintando blank por operação matricial
# blank_img[:] = vermelho
# blank_img[:] = azul
# blank_img[:] = verde

# blank_img[200:300, 300:400] = vermelho
# blank_img[:100, 50:150] = verde
# blank_img[400:, 200:300] = azul

# cv2.imshow('Blank', blank_img)

# 2. desenhar retangulo
# cv2.rectangle(blank_img, (10,10), (250,250), verde, 6)
# desenhando retangulo com metade da tela (x,y)
# cv2.rectangle(blank_img, (30,30), (blank_img.shape[1]//2, blank_img.shape[0]//2), verde, 3)
# cv2.imshow('Retangulo', blank_img)

# 3. desenhar circulo
# cv2.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2),200, vermelho, 5)
# cv2.imshow('Circulo', blank_img)

# 4. desenhar linha
# cv2.line(blank_img, (100,100), (blank_img.shape[1]//2, blank_img.shape[0]//2), verde, 2)
# cv2.imshow('Linha', blank_img)

# 5. escrever texto
cv2.putText(blank_img, 'Valentina', (0,250), cv2.FONT_HERSHEY_COMPLEX, 1.0, verde, 2)
cv2.putText(blank_img, 'Clara', (0,290), cv2.FONT_HERSHEY_COMPLEX, 1.0, vermelho, 2)
cv2.putText(blank_img, 'Ester', (0,330), cv2.FONT_HERSHEY_COMPLEX, 1.0, azul, 2)
cv2.putText(blank_img, 'Ana Luiza', (0,370), cv2.FONT_HERSHEY_COMPLEX, 1.0, roxo, 2)

def draw_teste(cv2, blank_img, center, np):    
  # Draw the left circle of the heart
  cv2.ellipse(
      blank_img,
      # center=(blank_img.shape[1] // 2 - 50, blank_img.shape[0] // 2 - 50),  # Adjusted center for left circle
      center=(center[1] - 50, center[0] -50),  # Adjusted center for left circle
      angle=0,
      axes=(70, 70),  # Circular shape
      startAngle=0,
      endAngle=-360,
      color=vermelho,
      thickness=-1  # Filled
  )

  # Draw the right circle of the heart
  cv2.ellipse(
      blank_img,
      # center=(blank_img.shape[1] // 2 + 50, blank_img.shape[0] // 2 - 50),  # Adjusted center for right circle
      center=(center[1] + 50, center[0] -50),  # Adjusted center for right circle
      angle=0,
      axes=(70, 70),  # Circular shape
      startAngle=0,
      endAngle=-360,
      color=vermelho,
      thickness=-1  # Filled
  )
  displacement_y = -51

  pts = np.array([
      (center[1]  - 100, center[0]  - 1),  # Left point of the triangle
      (center[1]  + 100, center[0]  - 1),  # Right point of the triangle
      (center[1] , center[0]  + 99)  # Bottom tip of the heart (adjusted for alignment)
  ], np.int32)

  pts = pts.reshape((-1, 1, 2))
  
  return cv2.fillPoly(blank_img, [pts], vermelho)


image = draw_teste(cv2, blank_img, (300,300), np)
# Show the image
cv2.imshow('As meninas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


