
#Construa um programa em OpenCV que faça o seguinte:
#1. Capture um quadro do vídeo de uma webcam;
#2. Exiba em janelas diferentes versões do quadro: a) em níveis de cinza; b) em vermelho; c) em verde; d) em azul;
#3. Salve o quadro original capturado e os quadros modificados como imagens em extensão PNG.
#* Lembre-se de sempre liberar os recursos ao final.



import numpy as np
import cv2
#Captura e salva imagem da webcam
cam = cv2.VideoCapture(0)
result, image = cam.read()
if result:
    cv2.imshow("Imagem",image)
    cv2.imwrite("Imagem.png",image)
    #The waitKey will pause your code run until you press any key with the image window opened.
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# destroyWindow("ImagemTeste")
else:
    print("Erro")
#cam.release()
#Escala Cinza
imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('EscalaCinza',imgGray)
cv2.imwrite("Escala-Cinza.png",imgGray)
cv2.waitKey(0)
#Separa a matriz da imagem em matrizes com valores de cada banda
b, g, r = cv2.split(image)
#Cria apenas uma matriz de zeros
zeros = np.zeros(image.shape[0:2], dtype="uint8")
#Escala Vermelho (0,0,255)
imgRed = cv2.merge([zeros, zeros, r])
cv2.imshow("Escala-Vermelho", imgRed)
cv2.imwrite("Escala-Vermelho.png",imgRed)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Escala Verde (0,255,0)
imgGreen = cv2.merge([zeros, g, zeros])
cv2.imshow("Escala-Verde", imgGreen)
cv2.imwrite("Escala-Verde.png",imgGreen)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Escala Azul (255,0,0)
imgBlue = cv2.merge([b, zeros, zeros])
cv2.imshow("Escala-azul", imgBlue)
cv2.imwrite("Escala-azul.png",imgBlue)
cv2.waitKey(0)
cv2.destroyAllWindows()
cam.release()