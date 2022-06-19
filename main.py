import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)


while True:
    success , img = cap.read()
    img, faces = detector.findFaceMesh(img,draw = False)
    if (faces):
        face = faces[0]
        pointLeftEye = face[374] ## You can find details on mediapipe's website about landmarks.
        pointRightEye = face[145]
        ## For eyes point
            ##cv2.circle(img, pointLeftEye, 5 , (255,0,0), cv2.FILLED)
            ##cv2.circle(img, pointRightEye, 5, (255, 0, 0), cv2.FILLED)
        ##
        w, _ = detector.findDistance(pointLeftEye,pointRightEye)
        W = 6.3 ## Average human eye distance.

        f = 650 ## This is focal length for my camera (You should probably change this.)
        d = (W*f)/w
        text = "Distance: " + str(int(d)) + "cm"
        cv2.putText(img,text,(face[10][0] - 100, face[10][1]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Image",img)
    cv2.waitKey(1)

