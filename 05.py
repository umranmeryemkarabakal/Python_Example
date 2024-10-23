import cv2
import numpy as np

img = cv2.imread("red_point.png")

# kırmızı renk sınırları
lower = np.array([160, 0, 0])
upper = np.array([179, 255, 255])

# rgb den hsv formatına çevir
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# aralıktaki kırmızı renk maskeler beyaza çevirir
img_mask = cv2.inRange(img_hsv,lower,upper)

#sadece maskelenen bölgeyi gösterir 
img_filter = cv2.bitwise_and(img,img, mask = img_mask )

# maskelenmiş resimlerin kenarlıkları 
contours, _ = cv2.findContours(img_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


if len(contours) > 0:
    # en büyük konturu bulur 
    max_contour = max(contours, key=cv2.contourArea)

    # konturu çevreleyen dikdörtgen oluştur
    x, y, w, h = cv2.boundingRect(max_contour)

    centerX = x + w // 2
    centerY = y + h // 2

    # resmin çıktı boyutu için boyutu yarıya indirir
    img = cv2.pyrDown(img)
    # kırmızı merkezin koordinatları için daire oluşturur
    cv2.circle(img, (int(centerX /2), int(centerY /2)), 5, (150, 255, 250), -1)  
 
    # Merkez koordinatlarını yazdır
    print(f"Kırmızı bölgenin merkezi: ({centerX}, {centerY})")


cv2.imshow("image",img)
#cv2.imshow("hsv image",img_hsv)
#cv2.imshow("red mask image",img_mask)
#cv2.imshow("red filter image",img_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()