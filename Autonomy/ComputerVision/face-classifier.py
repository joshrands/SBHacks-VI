import cv2

# Load the cascade
#face_cascade = cv2.CascadeClassifier("/usr/local/share/opencv4/haarcascade/haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

print(face_cascade)

# To capture video from webcam. 
cap = cv2.VideoCapture(2)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    print("test")
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    print(len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
