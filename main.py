import cv2
import mediapipe as mp
import numpy as np
from body_detection import detect_bodies

# initialize mediapipe pose solution
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()


def process_pose_detection(frame):
    # do Pose detection
    results = pose.process(frame)
    mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                           mp_draw.DrawingSpec((255, 0, 255), 2, 2)
                           )
    # Extract and draw pose on plain white image
    h, w, c = frame.shape
    opImg = np.zeros([h, w, c])
    opImg.fill(0)

    # draw extracted pose on black white image
    mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                           mp_draw.DrawingSpec((255, 0, 255), 2, 2)
                           )
    # print all landmarks
    print(results.pose_landmarks)

    return opImg,frame;


    return
def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        opImg, frame = process_pose_detection(frame)

        # display extracted pose on blank images
        cv2.imshow("Extracted Pose", opImg)
        frame = detect_bodies(frame)
        cv2.imshow('Body Detection', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    