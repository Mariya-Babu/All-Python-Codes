import cv2

# Read frequencies from the text file (assuming one frequency per line)
with open('elements.txt', 'r') as file:
    frequencies = [int(line.strip()) for line in file]

# Load the video file
cap = cv2.VideoCapture('compressed_video.mp4')

# Iterate through each frame of the video
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('Frame', frame)
    cv2.waitKey(frequencies[frame_count]*10)  # Adjust the delay according to the frame's frequency

    frame_count += 1

# Release resources
cap.release()
cv2.destroyAllWindows()
