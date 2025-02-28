import cv2
import mediapipe as mp
import numpy as np
import subprocess
import time
import pyautogui
import play_song

# Initialize MediaPipe Pose and Drawing utilities.
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Configure MediaPipe Pose.
pose = mp_pose.Pose(model_complexity=1, 
                    smooth_landmarks=True, 
                    enable_segmentation=False, 
                    min_detection_confidence=0.5, 
                    min_tracking_confidence=0.5)

# ตัวแปรป้องกันการส่งคำสั่งซ้ำ
has_triggered = False  # ควบคุมให้ยกแขนได้ครั้งเดียว
song_1_has_triggered = False
song_2_has_triggered = False
song_3_has_triggered = False
reset_time = None
cooldown_1 = 76  # 1 นาที 16 วินาที (76 วินาที)
cooldown_2 = 114  # 1 นาที 54 วินาที (114 วินาที)
cooldown_3 = 126  # 2 นาที 6 วินาที (126 วินาที)
hold_start_time = None  # เวลาที่เริ่มยกแขน
hold_time_required = 3  # ต้องยกแขนค้างไว้อย่างน้อย 3 วินาที

def classify_pose(landmarks, image_height):
    global has_triggered, reset_time, hold_start_time, song_1_has_triggered, song_2_has_triggered, song_3_has_triggered

    current_time = time.time()

    # Get required landmarks.
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]
    left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW]
    right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW]

    # Convert normalized x-coordinates to pixel values.
    lw_x = left_wrist.x * image_height
    rw_x = right_wrist.x * image_height
    ls_x = left_shoulder.x * image_height
    rs_x = right_shoulder.x * image_height

    # Convert normalized y-coordinates to pixel values.
    lw_y = left_wrist.y * image_height
    rw_y = right_wrist.y * image_height
    ls_y = left_shoulder.y * image_height
    rs_y = right_shoulder.y * image_height
    lh_y = left_hip.y * image_height
    rh_y = right_hip.y * image_height
    le_y = left_elbow.y * image_height
    re_y = right_elbow.y * image_height

    # ตรวจสอบว่าครบเวลาหรือยัง
    if has_triggered:
        if song_1_has_triggered == True:
            if reset_time is not None and (current_time - reset_time) >= cooldown_1:
                song_1_has_triggered = False
                has_triggered = False  # รีเซ็ตให้ยกมือได้อีกครั้ง
                reset_time = None  # เคลียร์เวลารีเซ็ต
                return "Ready Again"

            remaining_time = int(cooldown_1 - (current_time - reset_time)) if reset_time else 0
            return f"Wait {remaining_time}s"

        if song_2_has_triggered:
            if reset_time is not None and (current_time - reset_time) >= cooldown_2:
                song_2_has_triggered = False
                has_triggered = False  # รีเซ็ตให้ยกมือได้อีกครั้ง
                reset_time = None  # เคลียร์เวลารีเซ็ต
                return "Ready Again"

            remaining_time = int(cooldown_2 - (current_time - reset_time)) if reset_time else 0
            return f"Wait {remaining_time}s"

        if song_3_has_triggered:
            if reset_time is not None and (current_time - reset_time) >= cooldown_3:
                song_3_has_triggered = False
                has_triggered = False  # รีเซ็ตให้ยกมือได้อีกครั้ง
                reset_time = None  # เคลียร์เวลารีเซ็ต
                return "Ready Again"

            remaining_time = int(cooldown_3 - (current_time - reset_time)) if reset_time else 0
            return f"Wait {remaining_time}s"

    # Song 1
    if (lw_y > ls_y and lw_y < lh_y) and (rw_y > rs_y and rw_y < rh_y) and (abs(lw_x - rw_x) > 2.7 * abs(ls_x - rs_x)):
        if hold_start_time is None:
            hold_start_time = current_time  # เริ่มจับเวลายกแขน
            return "Hold... 3s"
        elif (current_time - hold_start_time) >= hold_time_required:
            has_triggered = True  # ป้องกันการกดซ้ำ
            song_1_has_triggered = True  # ป้องกันการกดซ้ำ
            reset_time = current_time  # ตั้งเวลาเริ่มหน่วง
            play_song.openPetrunko()
        else:
            remaining_hold_time = int(hold_time_required - (current_time - hold_start_time))
            return f"Hold... {remaining_hold_time}s"

    # Song 2
    elif (lw_y < ls_y and le_y > ls_y) and (rw_y < rs_y and re_y > rs_y):
        if hold_start_time is None:
            hold_start_time = current_time  # เริ่มจับเวลายกแขน
            return "Hold... 3s"
        elif (current_time - hold_start_time) >= hold_time_required:
            has_triggered = True  # ป้องกันการกดซ้ำ
            song_1_has_triggered = True  # ป้องกันการกดซ้ำ
            reset_time = current_time  # ตั้งเวลาเริ่มหน่วง
            play_song.openFunkonaut()
        else:
            remaining_hold_time = int(hold_time_required - (current_time - hold_start_time))
            return f"Hold... {remaining_hold_time}s"

    # Song 3
    elif (lw_y < le_y and le_y < ls_y) and (rw_y < re_y and re_y < rs_y):
        if hold_start_time is None:
            hold_start_time = current_time  # เริ่มจับเวลายกแขน
            return "Hold... 3s"
        elif (current_time - hold_start_time) >= hold_time_required:
            has_triggered = True  # ป้องกันการกดซ้ำ
            song_1_has_triggered = True  # ป้องกันการกดซ้ำ
            reset_time = current_time  # ตั้งเวลาเริ่มหน่วง
            play_song.openAstroFunk()
        else:
            remaining_hold_time = int(hold_time_required - (current_time - hold_start_time))
            return f"Hold... {remaining_hold_time}s"

    else:
        hold_start_time = None  # รีเซ็ตเวลาเมื่อแขนลดลง
        return "Other"

# Start video capture.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB.
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_rgb.flags.writeable = False

    # Process the image and detect pose landmarks.
    results = pose.process(image_rgb)

    # Convert the image back to BGR.
    image_rgb.flags.writeable = True
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    pose_label = "No Pose Detected"

    if results.pose_landmarks:
        # Draw pose landmarks on the image.
        mp_drawing.draw_landmarks(
            image_bgr,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(205,227,252), thickness=3, circle_radius=10),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255), thickness=3)
        )

        # Classify the pose.
        pose_label = classify_pose(results.pose_landmarks.landmark, image_bgr.shape[0])

    # # Display the classification label on the frame.
    # cv2.putText(image_bgr, f"Pose: {pose_label}", (10, 30), 
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Define text parameters
    text = f"Pose: {pose_label}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (255, 255, 255)  # White
    bg_color = (0, 0, 0)  # Black
    position = (10, 50)

    # Get text size
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)

    # Draw black rectangle as background
    cv2.rectangle(image_bgr, (position[0] - 5, position[1] - text_height - 5), 
                (position[0] + text_width + 5, position[1] + baseline + 5), bg_color, -1)

    # Put white text on top of black background
    cv2.putText(image_bgr, text, position, font, font_scale, text_color, font_thickness, cv2.LINE_AA)

    # Show the frame.
    cv2.imshow('MediaPipe Pose Landmark Detection with Classification', image_bgr)

    # Exit on pressing 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup.
cap.release()
cv2.destroyAllWindows()
pose.close()