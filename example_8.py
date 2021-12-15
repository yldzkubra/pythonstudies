import cv2  as cv
import numpy as np

imge= cv.imread("red.jpeg")
imgeGray=cv.cvtColor(imge,cv.COLOR_BGR2GRAY)

matris=np.array(imgeGray)

x=[]
y=[]

for satir in range(1216):
    for sütun in range(1600):
       if matris[satir][sütun]!=255:
           x.append(sütun)
           y.append(satir)

m_x=sum(x)/len(x)
m_y=sum(y)/len(y)

print(round(m_x),round(m_y))