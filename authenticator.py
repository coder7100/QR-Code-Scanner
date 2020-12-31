import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread("1.png")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open("data.text") as f:
    mydatalist = f.read().splitlines()
    print(mydatalist)

while cap.isOpened():
    _, img = cap.read()
    for barcodes in decode(img):
        mydata = barcodes.data.decode('utf-8')
        # print(barcodes.data)
        pts = np.array([barcodes.polygon], np.int32)
        print(mydata)
        if mydata in mydatalist:
            myoutput = "Authorized"
            color = (0, 255, 0)
        else:
            myoutput = "UnAuthorized"
            color = (0, 0, 255)
        pts = pts.reshape(-1, 1, 2)
        cv2.polylines(img, [pts], True, (0, 255, 0), 2)
        mydata = barcodes.data.decode('utf-8')
        pt2 = barcodes.rect
        cv2.putText(img, myoutput, (pt2[0], pt2[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Output", img)
    # cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
