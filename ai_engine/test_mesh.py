import cv2
import mediapipe as mp
from confusion_logic import ConfusionLogic

mp_face_mesh=mp.solutions.face_mesh
face_mesh=mp_face_mesh.FaceMesh(static_image_mode=False)
logic= ConfusionLogic(window_seconds=5)

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=face_mesh.process(rgb)

    if result.multi_face_landmarks:
        face_landmarks= result.multi_face_landmarks[0]

        # Eyebrow Distance
        left_brow = face_landmarks.landmark[70]
        right_brow = face_landmarks.landmark[300]
        brow_dist= abs(left_brow.x-right_brow.x)

        # Smile Score
        left_mouth= face_landmarks.landmark[61]
        right_mouth=face_landmarks.landmark[291]
        smile_score=abs(left_mouth.x-right_mouth.x)

        # Head Tilt
        left_eye=face_landmarks.landmark[33]
        right_eye=face_landmarks.landmark[263]
        head_tilt=abs(left_eye.y-right_eye.y)

        emotion, alert=logic.update(brow_dist, smile_score, head_tilt)

        print(
        "Brow:", round(brow_dist, 4),
        "| Smile:", round(smile_score, 4),
        "| Tilt:", round(head_tilt, 4),
        "| Emotion:", emotion,
        "| Alert:", alert
    )

    
    
    cv2.imshow("Webcam",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
