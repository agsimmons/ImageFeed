import time

import cv2


def capture(refresh_interval, video_capture_index, temp_file):
    try:

        cap = cv2.VideoCapture(video_capture_index)

        while True:
            ret, frame = cap.read()
            cv2.imwrite(temp_file, frame)

            time.sleep(refresh_interval)

    except:
        cap.release()
