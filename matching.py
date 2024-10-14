import cv2
import numpy as np

base_image = cv2.imread("taj.png")
template = cv2.imread("template.png")

w, h = template.shape[1], template.shape[0]

base_img_gray = cv2.cvtColor(base_image, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(base_image, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where(res>threshold)

for pt in zip(*loc[::-1]):
    pt = (pt[0].item(), pt[1].item())
    cv2.rectangle(base_image, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

cv2.imshow("res", res)
cv2.imshow("base image", base_image)
cv2.imshow("template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()