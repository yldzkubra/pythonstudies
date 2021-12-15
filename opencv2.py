import cv2 as cv

imge= cv.imread("red.jpeg")
imgeGray=cv.cvtColor(imge,cv.COLOR_BGR2GRAY)

ret,esiklenmis = cv.threshold(imgeGray,127,255,cv.THRESH_BINARY_INV)

n2,sinirlar,hiyerarsi = cv.findContours(esiklenmis,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(imge,sinirlar,-1,(0,255,0),5)

cnt = sinirlar[0]

M = cv.moments(cnt)             
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv.circle(imge,(cx,cy),5,(255,255,255),-1)

cv.imshow("sinirlar",imge)
cv.waitKey(0)

print(cx,cy)
