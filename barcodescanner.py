import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread("1.png")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():
    _, img = cap.read()
    for barcodes in decode(img):
        mydata = barcodes.data.decode('utf-8')
        # print(barcodes.data)
        pts = np.array([barcodes.polygon], np.int32)
        # print(mydata)
        pts = pts.reshape(-1, 1, 2)
        cv2.polylines(img, [pts], True, (0, 255, 0), 2)
        mydata = barcodes.data.decode('utf-8')
        pt2 = barcodes.rect
        cv2.putText(img, mydata, (pt2[0], pt2[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("images", img)
    # cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
