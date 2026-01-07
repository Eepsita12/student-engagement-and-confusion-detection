import cv2
import mediapipe as mp
import threading

from ai_engine.confusion_logic import ConfusionLogic

latest_state = {
    "emotion": "focused",
    "alert" : False,
    "faces":1
}

mp_face_mesh=mp.solutions.face_mesh
mp_face_detection=mp.solutions.face_detection

face_mesh=mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

face_detector=mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6
)

logic= ConfusionLogic(window_seconds=5)

def webcam_loop():
    global latest_state

    cap=cv2.VideoCapture(0)

    while True:
        ret,frame=cap.read()
        if not ret:
            continue

        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        detection_result=face_detector.process(rgb)
        faces_count= (
            len(detection_result.detections)
            if detection_result.detections
            else 0
        )

        mesh_result=face_mesh.process(rgb)
    
        if mesh_result.multi_face_landmarks:

            face_landmarks=mesh_result.multi_face_landmarks[0]

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

        else:
            emotion="focused"
            alert=True

        if faces_count != 1:
            alert=True

        latest_state= {
            "emotion": emotion,
            "alert": alert,
            "faces":faces_count
            }
        
        cv2.imshow("Student Webcam",frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

threading.Thread(
    target=webcam_loop,
    daemon=True
).start()

def get_current_state():
    return latest_state