import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

camera = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while camera.isOpened():
        success, image = camera.read()
        if not success: continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # left wrist coordinates
        if results.pose_landmarks is not None:
            left_wrist = results.pose_landmarks.landmark[
                mp_pose.PoseLandmark.LEFT_WRIST]
            print(left_wrist)
        mp_drawing.draw_landmarks(image,
            results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        cv2.imshow('MediaPipe Pose Demo', image)
        if cv2.waitKey(5) == 27: break
cv2.destroyAllWindows()
camera.release()