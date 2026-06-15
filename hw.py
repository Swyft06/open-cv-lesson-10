import cv2

webcam = cv2.VideoCapture("cars.mp4")

platecascade = cv2.CascadeClassifier("plate.xml")

while True:
    ret, img = webcam.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = platecascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



    cv2.imshow("Output", img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()