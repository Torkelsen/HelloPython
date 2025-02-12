import cv2
import time

video = cv2.VideoCapture(1) #0 for integrated laptop cam, 1 for usb
time.sleep(1)

first_frame = None

while True:
    check, frame = video.read()
    if not check:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    #cv2.imshow("My video", gray_frame_gau)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # preview only the changes
    #cv2.imshow("My video", delta_frame)

    # test cam for what thresh value that works best, obj white and background black
    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    # remove noise
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # preview only the changes, but nw with black and white
    #cv2.imshow("My video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # eliminating small fake objects (10k pixels)
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0))

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()