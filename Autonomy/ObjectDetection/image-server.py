import cv2

# Loading model
model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                      'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

# establish socket 
import socket
import random            
import pickle 
import numpy as np

# next create a socket object 
s = socket.socket()          

port = 6961#int(input("Enter your port: "))
ip = "169.231.137.9"#input("Enter your ip: ")
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind((ip, port))         
print("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening") 
  
# a forever loop until we interrupt it or  
# an error occurs 
  
# Establish connection with client. 

# receive frames and classify them 
while True:
    c, addr = s.accept()      
    print('Got connection from', addr) 

    frame = []
    for i in range(0,300):
        row = []
        for j in range(0,300):
            data = c.recv(3).decode('ascii')
#            print(data + "=") 
            if (data[:2] == "00"):
                row.append([int(data[2]), int(data[2]), int(data[2])])
            elif(data[0] == "0"):
                row.append([int(data[1:]), int(data[1:]), int(data[1:])])
            else:
                row.append([int(data),int(data),int(data)])
            print(row[j])

        frame.append(row)

#    print(frame)

#    data = pickle.loads(recv_data)
#    print(recv_data)

#    print(c.send(float(3.14)))
#    c.close()

#    frame = []
#    for i in range(0,300):
#        row = []
#        for j in range(0,300):
#            row.append(data[300*i+j])
#        frame.append(row)
    ret = True

    if ret == True:
        frame = cv2.rotate(np.float32(frame),cv2.ROTATE_90_CLOCKWISE)
        image_height, image_width, _ = frame.shape

        model.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True))
        output = model.forward()
        # print(output[0,0,:,:].shape)
        feedback = 6969

        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > .5:
                class_id = detection[1]
                if class_id == 1:
#                    print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
                    box_x = detection[3] * image_width
                    box_y = detection[4] * image_height
                    box_width = detection[5] * image_width
                    box_height = detection[6] * image_height
#                    cv2.rectangle(frame, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=10)
#                    cv2.putText(frame,class_name ,(int(box_x), int(box_y+.05*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(.005*image_width),(0, 0, 255))

                    # get pixel offset
                    y_pixel = int(box_y + (box_height - box_y) / 2.0)

#                    print(x_pixel)
#                    print(box_width)
#                    print(image_width)
                    # get control offset 
                    feedback = (float(y_pixel) / float(image_height)) * 2 - 1
                    print(feedback)

                    resized = cv2.resize(frame, (114*5,64*5), interpolation = cv2.INTER_AREA)

        cv2.imshow('image', frame)
                    # cv2.imwrite("image_box_text.jpg",image)

        cv2.waitKey(0)

        c.send(str(feedback).encode())

cv2.destroyAllWindows()
