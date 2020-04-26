import cv2
import face_recognition

cap = cv2.VideoCapture(0)
cv2.namedWindow('v')


face_cascade = cv2.CascadeClassifier('')

while True:
    ret,frame = cap.read()
    if not ret:
        cv2.waitKey(30)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # faces = face_cascade
    face_locations = face_recognition.face_locations(grey)
    for (x,y,w,h) in face_locations:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)

    #显示
    cv2.imshow("face",frame)
    keyvacle = cv2.waitKey(20)

    if keyvacle & 0xfff == ord('q'):
        break