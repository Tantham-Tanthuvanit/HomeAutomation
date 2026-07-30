import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import Image, ImageFormat

import constants

from helper import cleaning

# loading the model
base_options = python.BaseOptions(model_asset_path = "./models/hand_landmarker.task")
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=6)

with vision.HandLandmarker.create_from_options(options) as detector:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        succes, frame = cap.read()
        if not succes:
            continue

        # clean image
        frame, rgb_frame = cleaning(frame)

        h, w, _ = frame.shape

        # run inference ( predict data )
        detection_res = detector.detect(rgb_frame)

        # check if hands were detected
        if detection_res.hand_landmarks:
            for hand_landmarks in detection_res.hand_landmarks:

                pixelPoints = []
                fingers = []

                for landmark in hand_landmarks:
                    # Scale the normalized float values into screen pixels
                    cx = int(landmark.x * w)
                    cy = int(landmark.y * h)

                    pixelPoints.append((cx,cy))

                    # Draw red dots at every joint coordinate
                    cv2.circle(frame, (cx,cy), 5, (0,0,255),-1)

                for connection in constants.hand_connections:
                    startIdx = connection[0]
                    endIdx = connection[1]

                    start_point = pixelPoints[startIdx]
                    end_point = pixelPoints[endIdx]

                    cv2.line(frame, start_point, end_point, (0,255,0), 2)

        cv2.imshow("Hand Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


