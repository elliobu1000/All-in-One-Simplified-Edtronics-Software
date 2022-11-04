from flask import Blueprint, jsonify, request
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




test_mode = Blueprint(name="test_mode", import_name=__name__)

@test_mode.route('/run', methods=['GET'])
def run():
    """
    ---
    get:
      description: test mode
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - testing
    """
    output = {
      "msg": "The Test mode was succesfully started"
    }

    # this should start the video 
    capture_process = mp.Process(target=capture_frames, args=())
    capture_process.start()

    return jsonify(output)