import cv2

# Pretrained classes in the model

def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value


# Loading model
model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                      'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

cap = cv2.VideoCapture("van-floor.avi")

#image = cv2.imread("output.jpg")
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.rotate(frame,cv2.ROTATE_180)
        image_height, image_width, _ = frame.shape

        model.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True))
        output = model.forward()
        # print(output[0,0,:,:].shape)

        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > .5:
                class_id = detection[1]
                class_name=id_class_name(class_id,classNames)
                if class_name == "person":
                    print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
                    box_x = detection[3] * image_width
                    box_y = detection[4] * image_height
                    box_width = detection[5] * image_width
                    box_height = detection[6] * image_height
                    cv2.rectangle(frame, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=10)
                    cv2.putText(frame,class_name ,(int(box_x), int(box_y+.05*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(.005*image_width),(0, 0, 255))

                    # get pixel offset
                    x_pixel = int(box_x + (box_width - box_x) / 2.0)

                    print(x_pixel)
                    print(box_width)
                    print(image_width)
                    # get control offset 
                    feedback = (float(x_pixel) / float(image_width)) * 2 - 1
                    print(feedback)

                    resized = cv2.resize(frame, (114*5,64*5), interpolation = cv2.INTER_AREA)

                    cv2.imshow('image', resized)
                    # cv2.imwrite("image_box_text.jpg",image)

                    cv2.waitKey(0)

cv2.destroyAllWindows()
