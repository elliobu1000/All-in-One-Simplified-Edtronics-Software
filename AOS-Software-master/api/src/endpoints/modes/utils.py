from threading import Thread
import numpy as np
import logging
import multiprocessing as mp
import cv2, time

def capture_frames():
    src = 'api/media/videos/video.mp4'
    capture = cv2.VideoCapture(src)
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

    # FPS = 1/X, X = desired FPS
    FPS = 1/120
    FPS_MS = int(FPS * 1000)

    while True:
        # Ensure camera is connected
        if capture.isOpened():
            print("THe camera is running")
            (status, frame) = capture.read()
            
            # Ensure valid frame
            if status:
                cv2.imshow('frame', frame)
            else:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(FPS)
        else:
            print("nada working")
    capture.release()
    cv2.destroyAllWindows()

MODES = {
    "LED_ON_MODE":1,
    "LED_OFF_MODE":2,
    
}