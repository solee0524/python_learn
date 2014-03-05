#/usr/bin/python

#The below code is show webcam to gray

# import numpy as np
# import cv2
# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


#the below code is save the vedio from webcam
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

i = 0
# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mkv',fourcc, 20.0, (640,480))


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        # out.write(frame)

        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break

        if k == ord('c'):
            cv2.imwrite('out_' + str(i) + '.jpg', frame)
            i += 1
    else:
        break

# Release everything if job is finished
cap.release()
# out.release()
cv2.destroyAllWindows()