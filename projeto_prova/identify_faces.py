import cv2

# Carrega o classificador Haarcascade para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Captura vídeo da webcam (ou de um arquivo de vídeo)
# Para capturar de um arquivo, substitua 0 pelo caminho do arquivo
cap = cv2.VideoCapture("la_cabra.mp4")

while True:
    # Lê o frame do vídeo
    ret, frame = cap.read()
    
    # Verifica se a captura do frame foi bem-sucedida
    if not ret:
        break
    
    # Converte o frame para escala de cinza (requisito para o classificador Haar)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detecta rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Desenha retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Exibe o frame com os rostos detectados
    cv2.imshow('Video - Face Detection', frame)
    
    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha as janelas
cap.release()
cv2.destroyAllWindows()
