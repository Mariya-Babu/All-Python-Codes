import cv2
import numpy as np
L = list()
R = list()
count = 1
dim = list()

def process_video(input_path):
    # Open the video file
    cap = cv2.VideoCapture(input_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return
    
    ret, frame = cap.read()

    R.append(frame)
    i=0
    L.append(1)
    # Process the video frame by frame
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        global count
        
        count += 1
        
        # Check if the frame was read successfully
        if not ret:
            break

        # Process the frame (e.g., display it, perform operations on it)
        # Example: Display the frame
        # cv2.imshow('Frame', frame)
        gray_frame1 = cv2.cvtColor(R[i], cv2.COLOR_BGR2GRAY)
        gray_frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Compute the absolute difference between the two frames
        diff = cv2.absdiff(gray_frame1, gray_frame2)
        total_diff = np.mean(diff)
        #print(total_diff)
        # Get the dimensions of the frame
        height, width, _ = frame.shape
        dim.append(height)
        dim.append(width)
        # Calculate the number of pixels
        num_pixels = height * width
        if(total_diff< 1.0) :#num_pixels/100):
            L[i]= L[i]+1
        else:
            R.append(frame)
            i += 1
            L.append(1)
        # Wait for a key press; press 'q' to exit
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     break

    CompressionRatio = count/len(R)

    print(f'b = {count}')
    print(f'b` = {len(L)}')
    print(f'Compression Ration : {CompressionRatio}')


    # Define the file path
    file_path = 'elements.txt'

    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Iterate over the elements and write them to the file
        for element in L:
            file.write(str(element) + '\n')
        # Release resources
    cap.release()
    cv2.destroyAllWindows()


def generate_video(output_file):
    # Define the output video file name and codec
    # print(ouptut_file)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')


    # Define the video writer
    out = cv2.VideoWriter(output_file, fourcc, 25.0, (dim[1], dim[0]))

    # Write each frame to the video file
    for frame in R:
        out.write(frame)

    # Release the video writer
    out.release()

    print(f"Video saved as '{output_file}'")


# Example usage
input_path = 'input_video.mp4'
process_video(input_path)
generate_video('compressed_video.mp4')
print('video compression successfull')

