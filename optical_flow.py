import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()


max_points = 50                
min_keypoint_quality = 0.01    
keypoint_min_distance = 15     
trail_length = 25              

feature_params = dict(
    maxCorners=max_points,
    qualityLevel=min_keypoint_quality,
    minDistance=keypoint_min_distance,
    blockSize=7
)

lk_params = dict(
    winSize=(15, 15),          # Smaller window for facial motions
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

# Read first frame
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

mask = np.zeros_like(old_frame)
color = np.random.randint(0, 255, (max_points, 3))
frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate optical flow
    p1, st, _ = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Draw motion trails with fading effect
        mask = (0.9 * mask).astype(np.uint8)  # Fade trails gradually
        
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), 
                           color[i].tolist(), 2)
            frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)

        img = cv2.add(frame, mask)

        # Update previous frame and points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

        # Re-detect only when necessary
        frame_counter += 1
        if len(good_new) < max_points//2 or frame_counter % trail_length == 0:
            p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
            frame_counter = 0

    cv2.imshow('Facial Motion Tracking', img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()