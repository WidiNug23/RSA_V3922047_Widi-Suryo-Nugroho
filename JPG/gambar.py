import cv2
import numpy as np

demo = cv2.imread("C:/Users/User/Pictures/IMG_6678.JPG", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)
cv2.imwrite("C:/Users/User/Pictures/KEY-IMG_6678.JPG", key)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)
cv2.imwrite("C:/Users/User/Pictures/enc-IMG_6678.JPG", encryption)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imwrite("C:/Users/User/Pictures/dec-IMG_6678.JPG", decryption)

cv2.imshow("encryption", encryption)
cv2.imshow("decryption", decryption)

cv2.waitKey(-1)
cv2.destroyAllWindows()