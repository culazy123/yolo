import uuid
import os
import time
import cv2

# Define the path to save images
image_path = os.path.join('da', 'image')
os.makedirs(image_path, exist_ok=True)  # Create the directory if it doesn't exist

labels = ['awake', 'drowsy']
num_img = 20

# Initialize the video capture device
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

for label in labels:
    print("Collecting images for {}".format(label))
    time.sleep(5)  # Wait for 5 seconds before starting to capture images

    for img in range(num_img):
        print("Collecting image {} for {}".format(img, label))
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            continue
        
        # Create a unique file name
        img_name = os.path.join(image_path, "{}_{}.jpg".format(label, uuid.uuid1()))
        cv2.imwrite(img_name, frame)
        cv2.imshow('Image Collection', frame)
        time.sleep(2)  # Wait for 2 seconds before capturing the next image

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()  # Release the video capture device
cv2.destroyAllWindows()  # Close all OpenCV windows

