<a name="readme-top"></a>

<div align="center">

  <h3 align="center">Student Engagement & Confusion Detection System</h3>

  <p align="center">
    A real-time computer vision system that detects student engagement,
    confusion, and basic proctoring violations during live online sessions.
  </p>

</div>

---

## About The Project

This project is a real-time student engagement and integrity monitoring system built for live online learning sessions.

The system analyzes a student’s webcam feed to determine engagement levels and raise proctor alerts using explainable computer vision logic, not black-box emotion models.

---

## What the System Does

- Detects student engagement states:
  - Focused
  - Happy
  - Confused
- Raises proctor alerts when:
  - No face is detected
  - Multiple faces are detected
  - Confusion persists over time
- Displays a live teacher dashboard with:
  - Current engagement status
  - Color-coded alerts
  - Session timeline

---

## Core Design Philosophy

- No black-box AI emotion models
- Explainable facial behavior logic
- Time-based decision making
- Conservative alerting to avoid false positives
- Clean separation between AI engine, backend, and frontend

---

## Tech Stack

### AI / Computer Vision
* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![OpenCV](https://img.shields.io/badge/OpenCV-27338E?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
* [![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)


### Backend
* [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
* [![WebSockets](https://img.shields.io/badge/WebSockets-010101?style=for-the-badge&logo=socket.io&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
* [![Uvicorn](https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)


### Frontend
* [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)


---

## Project Structure

```

student-engagement-and-confusion-detection/
│
├── ai_engine/
│   ├── confusion_logic.py
│   ├── state_provider.py
│   └── face_mesh_test.py
│
├── backend/
│   ├── main.py
│   └── ws_test.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
└── README.md

```

---

## System Architecture

```

Webcam Feed
|
v
Face Detection (Integrity Check)
|
v
Face Mesh (Facial Landmark Analysis)
|
v
Time-Based Confusion Logic
|
v
FastAPI Backend (WebSockets)
|
v
Teacher Dashboard (Live UI)

```

---

## System Working

### 1. Face Detection (Integrity Check)

MediaPipe Face Detection is used to count the number of faces in the frame:
- 0 faces → Student not present
- 1 face → Normal session
- 2+ faces → Possible impersonation

This information is used only for **proctor alerts**.

---

### 2. Facial Landmark Analysis (Engagement Detection)

MediaPipe Face Mesh is used to analyze the primary student’s face:
- Eyebrow distance → cognitive strain
- Smile intensity → engagement
- Head tilt → confusion support signal

---

### 3. Confusion Logic

Confusion is treated as a sustained cognitive state, not a momentary expression.

A rolling time window is used to:
- Avoid single-frame decisions
- Reduce false positives
- Trigger alerts only when confusion persists

---

### 4. Real-Time Streaming

The backend streams live engagement state and alerts to the frontend using **WebSockets**, enabling real-time updates without page refresh.

---

## Session Timeline

The teacher dashboard displays a session timeline using color-coded blocks:

🟢 Focused / Happy – Normal engagement

🟡 Confused – Student shows sustained confusion

🔴 Alert – Proctoring or integrity issue detected

This helps teachers understand engagement trends over time.

---

## Dashboard Preview

<p align="center">
  <img width="1535" height="776" alt="image" src="https://github.com/user-attachments/assets/d2558433-c18c-4602-ae54-32065a89c296" />
   <img width="1534" height="773" alt="image" src="https://github.com/user-attachments/assets/c9712c29-21eb-428a-958e-6abeae9039b7" />
  <img width="1544" height="779" alt="image" src="https://github.com/user-attachments/assets/5acc9b34-d45c-4d25-8734-1eeb3b41ac68" />
</p>


## Development Utilities

- `face_mesh_test.py`  
  Used during development to test facial landmarks and tune confusion logic.

- `ws_test.py`  
  Used to test WebSocket communication without the frontend.

These files are **not part of the production pipeline**.

---

## How to Run the Project

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start backend

```bash
uvicorn backend.main:app
```

> Webcam will open automatically.

### 4. Open frontend

Open `frontend/index.html` using Live Server or directly in the browser.

---

## Proctoring Rules Summary

| Condition               | Action   |
| ----------------------- | -------- |
| No face detected        | Alert    |
| Multiple faces detected | Alert    |
| Sustained confusion     | Alert    |
| Normal engagement       | No alert |

Alerts are intentionally **conservative** to ensure reliability.

---

## Future Scope

* Gaze direction detection
* Per-student baseline calibration
* Multi-student classroom support
* React-based frontend

---

## Project Status

| Feature              | Status     |
| -------------------- | ---------- |
| Confusion Detection  | ✅ Complete |
| Multi-Face Detection | ✅ Complete |
| Time-Based Logic     | ✅ Complete |
| WebSocket Backend    | ✅ Complete |
| Teacher Dashboard    | ✅ Complete |

---

## Thank You

