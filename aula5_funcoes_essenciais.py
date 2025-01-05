import cv2

# lendo a imagem - 3 canais
img = cv2.imread("assets/fots/cat_large.jpg")
img2 = cv2.imread("assets/fots/park.jpg")

# 1. COnvertendo para escala de cinza (grayscale)
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Cat", img)
cv2.imshow("Cat Cinza", cinza)

# 2. blur 
# cv2.GaussianBlur(image, tamanho do kernel, tamanho do kernel)
blurred = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow("Blur", blurred)

# 3. Edge Cascade - deteceção de bordas
# cv2.Canny(image, threshold1, threshold2)
canny = cv2.Canny(img, 250, 200)
cv2.imshow("Canny", canny)

# 3.1 melhora a detecção de bordas com a imagem borrada
canny_blurred = cv2.Canny(blurred, 250, 200)
cv2.imshow("Canny Blurred", canny_blurred)

# 4. Dilatando a imagem
dilated = cv2.dilate(canny_blurred, (9,9), iterations=3)
cv2.imshow("Dilated", dilated)

# 5. Eroding Image - Correndo a imagem
eroded = cv2.erode(dilated, (9,9), iterations=3)
cv2.imshow("Eroded", eroded)

# 6. Resize
resized = cv2.resize(img, (300,300), interpolation=cv2.INTER_AREA)

# 7. Cropping
cropped = img[50:200, 200:400]
cv2.imshow("Cropped", cropped)
