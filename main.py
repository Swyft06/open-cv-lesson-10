import cv2

webcam = cv2.VideoCapture("cars.mp4")

carcascade = cv2.CascadeClassifier("cars.xml")


while True:
    ret, img = webcam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars = carcascade.detectMultiScale(gray,1.1,1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("output",img)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()