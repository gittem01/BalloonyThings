from Storage import *
from Marble import *

img = np.zeros((900, 900, 3), np.uint8)
winName = "ellipses"

cv2.namedWindow(winName)

ss = []
for i in range(4):
    for j in range(4):
        ss.append(Storage([300*(i), 300*(j)], baseSize=75))

m = Marble([70, 70], [4, 2])

while 1:
    img2 = img.copy()
    for s in ss:
        s.draw(img2)
    m.draw(img2)
    for s in ss:
        s.update(m)
    m.move(img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

    cv2.imshow(winName, img2)
