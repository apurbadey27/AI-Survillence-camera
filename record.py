import numpy as np
import cv2
from datetime import datetime

def record():
    video_capture_0 = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_0 = cv2.VideoWriter(f'recording/recording_0/{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.avi', fourcc,20.0,(640,480))

    video_capture_1 = cv2.VideoCapture(1)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_1 = cv2.VideoWriter(f'recording/recording_1/{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.avi', fourcc,20.0,(640,480))

    video_capture_2 = cv2.VideoCapture(2)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_2 = cv2.VideoWriter(f'recording/recording_2/{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.avi', fourcc,20.0,(640,480))

    while True:
        # Capture frame-by-frame
        ret0, frame0 = video_capture_0.read()
        cv2.putText(frame0, f'{datetime.now().strftime("%D - %H : %M : %S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255,255,255), 2)
        out_0.write(frame0)

        ret1, frame1 = video_capture_1.read()
        cv2.putText(frame1, f'{datetime.now().strftime("%D - %H : %M : %S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255,255,255), 2)
        out_1.write(frame1)

        ret2, frame2 = video_capture_2.read()
        cv2.putText(frame2, f'{datetime.now().strftime("%D - %H : %M : %S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255,255,255), 2)
        out_2.write(frame2)
        

        if (ret0):
            # Display the resulting frame
            cv2.imshow('Cam 0', frame0)

        if (ret1):
            # Display the resulting frame
            cv2.imshow('Cam 1', frame1)

        if (ret2):
            # Display the resulting frame
            cv2.imshow('Cam 2', frame2)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture_0.release()
    video_capture_1.release()
    video_capture_2.release()
    cv2.destroyAllWindows()
