import sys
import time

import cv2


def capture(refresh_interval, video_capture_index, temp_file):

    cap = cv2.VideoCapture(video_capture_index)

    if cap is None or not cap.isOpened():
        print('ERROR: VideoCapture with index {} does not exist'.format(video_capture_index))
        sys.exit(1)

    try:
        while True:
            ret, frame = cap.read()
            cv2.imwrite(temp_file, frame)

            time.sleep(refresh_interval)

    except:
        cap.release()
