import cv2
path = r'C:\Users\ZAID\Videos\Captures\Assassin’s Creed® Odyssey 2022-08-18 01-04-30.mp4'
video = cv2.VideoCapture(path)

while True:
    status, img = video.read()
    if not status:
        break
    cv2.imshow('video', img)
    if cv2.waitKey(1) == 27:
        break
video.release()
cv2.destroyAllWindows()