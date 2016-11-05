import cv2


cap = cv2.VideoCapture(0)

gesture_type = 'v'
counter = 0
path = 'photos/%s/%03d.png'
size = (36, 36)
skip = 5

def resize(frame):
    frames = [frame]
    frames.append(cv2.flip(frame, 0))
    frames.append(cv2.flip(frame, 1))
    frames.append(cv2.flip(cv2.flip(frame, 0), 1))
    return frames

while True:
    ret, frame = cap.read()
    cv2.imshow("webcam", frame)
    k = cv2.waitKey(30)
    if k == 27:
        break
    elif k == ord(' '):
        # frame = cv2.resize(frame, size)
        # frames = resize(frame)
        cv2.imwrite(path % (gesture_type, counter), frame)
        counter += 1
