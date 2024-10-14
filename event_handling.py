import cv2

img = cv2.imread("template_matching/taj.png")

cv2.imshow("image", img)

l = []
def mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        l.append((x,y))
        if(len(l) == 2):
            x1, y1, x2, y2 = l[0][0], l[0][1], l[1][0], l[1][1]
            if(x2 > x1 and y2 > y1):
                cropped = img[y1:y2+1, x1:x2+1]
            else:
                cropped = img[y2:y1+1, x2:x1+1]
            cv2.imwrite("template_matching/template.png", cropped)
            cv2.imshow("cropped", cropped)
        cv2.imshow("image", img)

cv2.setMouseCallback("image", mouse_click)
cv2.waitKey(0)
print(l)
cv2.destroyAllWindows()