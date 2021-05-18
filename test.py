import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros(shape=(500,500))

def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,color=(255,0,0), thickness=-1)

cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing",draw_circle)
while True:
    cv2.imshow("drawing",img)
    if cv2.waitKey(20) & 0xFF == ord("r"): 
        break
cv2.destroyAllWindows()