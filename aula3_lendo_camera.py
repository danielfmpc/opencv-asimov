import cv2

cap = cv2.VideoCapture(0)
while True:
  _, frame = cap.read()
  
  # Inverter imagem
  frame = cv2.flip(frame, 1)

  # Mostrar imagem
  cv2.imshow('frame', frame)
  
  # Aguardar tecla para fechar
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

# import os 
# os.system('cls' if os.name == 'nt' else 'clear') 
# # Importante: escolha o número correspondente à câmera que pretende utilizar
# cap = cv2.VideoCapture(1) 
# while True: 
#   ret, frame = cap.read() 
#   if ret == True: 
#     # Exibir o frame do vídeo 
#     windowname = 'Imagem da Cammera' 
#     cv2.imshow(windowname, frame) 
#     # Definindo uma Tecla ("q") para encerramento de programa pelo usuário 
#   if cv2.waitKey(20) & 0xFF==ord('q'): 
#     print('nINFO | Programa finalizado pelo usuário') 
#     break 
  
#   # Permitindo que o programa seja encerrado pelo botão de fechar a janela 
#   if cv2.getWindowProperty(windowname, cv2.WND_PROP_VISIBLE) < 1: 
#     print('nINFO | Programa finalizado pelo usuário') 
#     break 
#     # Criando informando que a Câmera não está disponível 
#   else: 
#     print("nINFO | A câmera escolhida não está disponível") 
#     print("(Tente alterar o número da câmera utilizado)") 
#     break 
# cap.release() 
# cv2.destroyAllWindows() 