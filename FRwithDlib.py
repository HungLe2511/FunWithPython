import dlib
import cv2

img = cv2.imread("Muller.jpg")

gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)
#cv2.imshow(winname= "MyIdol", mat = gray)

# gan face_detector vao model FR
face_detector = dlib.get_frontal_face_detector()

faces = face_detector(img)
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    
# draw rectangle into img
cv2.rectangle(img = img, pt1 = (x1, y1), pt2 = (x2, y2), color = (0, 255, 0), thickness = 4)
cv2.imshow(winname= "MyIdol", mat = img)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()