import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose and Drawing utilities.
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Configure MediaPipe Pose.
pose = mp_pose.Pose(model_complexity=1, 
                    smooth_landmarks=True, 
                    enable_segmentation=False, 
                    min_detection_confidence=0.5, 
                    min_tracking_confidence=0.5)

# Simple function for pose classification.
def classify_pose(landmarks, image_height):
    """
    A simple classification that checks if both wrists are above the respective shoulders.
    
    landmarks: list of pose landmarks from MediaPipe.
    image_height: used to convert normalized landmarks to pixel positions.
    
    Returns:
      A string with the classification result.
    """
    # Get required landmarks. Each landmark has x, y, z, visibility.
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    
    # Convert normalized y-coordinates to pixel values (higher pixel value = lower in the image).
    lw_y = left_wrist.y * image_height
    rw_y = right_wrist.y * image_height
    ls_y = left_shoulder.y * image_height
    rs_y = right_shoulder.y * image_height

    # Check if both wrists are above the shoulders.
    if lw_y < ls_y and rw_y < rs_y:
        return "Hands Up"
    else:
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
    
    # Display the classification label on the frame.
    cv2.putText(image_bgr, f"Pose: {pose_label}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Show the frame.
    cv2.imshow('MediaPipe Pose Landmark Detection with Classification', image_bgr)

    # Exit on pressing 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup.
cap.release()
cv2.destroyAllWindows()
pose.close()