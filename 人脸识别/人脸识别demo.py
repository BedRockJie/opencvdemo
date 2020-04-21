import cv2
import face_recognition


img = cv2.imread ("face\ziying.jpg",0)
resized_image = cv2.resize(img, (650,500))
cv2.imshow("Penguins", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = face_recognition.load_image_file("face\ziying.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)