import cv2
import numpy as np
import time
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
video_input = input("Enter video input: ")
cap = cv2.VideoCapture(2)

# target color
target_color_min = [0, 200, 0]
target_color_max = [50, 255, 50]

def rgbInTarget(rgb_value):
#  if (rgb_value[0] < target_color_max[0] and rgb_value[0] > target_color_min[0]) and (rgb_value[1] < target_color_max[1] and rgb_value[1] > target_color_min[1]) and (rgb_value[2] < target_color_max[2] and rgb_value[2] > target_color_min[2]):
  print(rgb_value)
  if (rgb_value[1] > rgb_value[0] and rgb_value[1] < rgb_value[2]):# and rgb_value[2] < 200):# and rgb_value[0] < 100):
    print("In range!")
    return True
  else:
    return False

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
#    resized = cv2.resize(frame, (57,32), interpolation = cv2.INTER_AREA)

    for i in range(0, len(frame), 10):
      for j in range(0, len(frame[i])):
        if (rgbInTarget(frame[i,j])):
          print(frame[i,j])

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

    time.sleep(1)
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
