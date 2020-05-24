import cv2
import numpy as np


def change(x):
    print(x)


img = np.zeros((515, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('Blue', 'image', 0, 255, change)
cv2.createTrackbar('Green', 'image', 0, 255, change)
cv2.createTrackbar('Red', 'image', 0, 255, change)

switch = 'OFF/ON'
cv2.createTrackbar(switch, 'image', 0, 1, change)

while(True):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos('Blue', 'image')
    g = cv2.getTrackbarPos('Green', 'image')
    r = cv2.getTrackbarPos('Red', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = [0]
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
