import cv2

def camera(src=0):
    cam = cv2.VideoCapture(src)
    while True:
        status, img = cam.read()
        if not status:
            break
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # cv2.imshow('video', img)
        # cv2.imshow('grey', grey)
        # cv2.imshow('rgb', rgb)
        # stiching into one window
        cv2.imshow('video', cv2.hconcat([img, rgb]))
        if cv2.waitKey(1) == 27:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera()