import os
import matplotlib.pyplot as plt
import cv2
import glob

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
user_input = input("Enter the path where the image is located: ")
user_input_ID = input("Student ID: ")
os.mkdir(user_input_ID)
user_input1 = input("Enter the path where you want to save the croped picture(please input the path with student ID): ")

#img_dir = "E:/COMPUTER/Module_1_Face_Recognition/face/"
data_path = os.path.join(user_input, '*jpg')
print(data_path)
temp = 0
image_list = []
for filename in glob.glob(data_path):
    print(filename)
    im = cv2.imread(filename)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)#color_to_gray
    face = face_cascade.detectMultiScale(gray,1.2,5)
    for (x,y,w,h) in face:
        cv2.rectangle(im,(x,y), (x+w, y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = im[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    Eyefile = "face_" + str(temp) + ".jpg"
    #cv2.imwrite(Eyefile, roi_color)
    cv2.imwrite(os.path.join(user_input1, Eyefile), roi_color)
    temp+=1

cv2.destroyAllWindows()
# for i in image_list:
#     cam = image_list[i]
#     _,frame = cam.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     face = face_cascade.detectMultiScale(gray,1.2,5)
#     for (x,y,w,h) in face:
#         cv2.rectangle(img,(x,y), (x+w, y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
#     cv2.imshow('img', frame)
#     cv2.waitKey(10000)
#
# cv2.destroyAllWindows()



#plt.imshow(img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import glob
# image_list = []
# for filename in glob.glob('E:/COMPUTER VISION A-Z™/Module_1_Face_Recognition/face/*.jpg'): #assuming gif
#     im=cv2.imread(filename)
#     image_list.append(im)
#
# img = image_list[0]
# print(img)

# import cv2
# import os, os.path
#
# print (cv2.__version__)
#
# imageDir = "E:/COMPUTER VISION A-Z™/Module_1_Face_Recognition/face/" #specify your path here
# image_path_list = []
# valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"] #specify your vald extensions here
# valid_image_extensions = [item.lower() for item in valid_image_extensions]
#
# for file in os.listdir(imageDir):
#     extension = os.path.splitext(file)[1]
#     if extension.lower() not in valid_image_extensions:
#         continue
#     image_path_list.append(os.path.join(imageDir, file))
#
# for imagePath in image_path_list:
#     img = cv2.imread(imagePath)
#     if img is None:
#         continue
#
#     cv2.imshow(imagePath, img)
#
#     key = cv2.waitKey(0)
#     if key == 27: # escape
#         break
# print(img)
# #cv2.destroyAllWindows()
