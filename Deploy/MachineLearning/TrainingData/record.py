import numpy as np
import cv, cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(2)

file_name = raw_input("Enter output file name: ")

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter("./Raw/" + file_name + ".avi",fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
#        frame = cv2.flip(frame,0)
#        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
