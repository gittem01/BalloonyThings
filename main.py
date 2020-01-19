from Storage import *
from Marble import *

img = np.zeros((900, 900, 3), np.uint8)
winName = "ellipses"

cv2.namedWindow(winName)

ss = []
for i in range(2):
    for j in range(2):
        ss.append(Storage([300*(i+1), 300*(j+1)]))

m = Marble([70, 70], [2, 1])

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

