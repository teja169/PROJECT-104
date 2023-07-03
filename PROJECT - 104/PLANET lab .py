import cv2 

spc = cv2.imread("solar-system.jpg")

a = "MERCURY"
b = "VENUS"
c = "EARTH"
d = "MOON"
e = "MARS"
f = "JUPITER"
g = "SATURN"
h = "URANUS"
i = "NEPTUNE"

cv2.putText(spc , a , (125 , 182) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , b , (175 , 260) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , c , (280 , 265) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , d , (314 , 147) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , e , (380 , 250) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , f , (500 ,  32) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , g , (740 ,  93) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , h , (935 , 120) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )
cv2.putText(spc , i , (1095, 130) , color=(0 , 0 , 255) , fontFace=cv2.FONT_HERSHEY_COMPLEX , fontScale=0.35 )


cv2.imshow("space" , spc )
cv2.waitKey(0)