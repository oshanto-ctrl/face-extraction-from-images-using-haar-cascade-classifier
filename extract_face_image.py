import cv2
import glob

# haarcascades face extraction model
face_cascade = cv2.CascadeClassifier("C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

# file path of image datasets
path = "E:\\#Research_Info\\video_dataset_folder_male\\image_dataset_folder\\*.*"

image_number = 1

image_list = glob.glob(path)

for file in image_list:
    print(f"Opening {file}")
    image = cv2.imread(file, 1)
    gray_images = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converting to grayscale
    face_images = face_cascade.detectMultiScale(gray_images, 1.3, 5)

    try:
        for (x, y, w, h) in face_images:
            region_of_interest = image[y:y+h, x:x+w]
        resized = cv2.resize(region_of_interest, (128, 128))
        cv2.imwrite("E:\\#Research_Info\\video_dataset_folder_male\\extracted_faces_dataset_folder/" + str(image_number) + ".png", resized)
    except:
        print("No Faces Detected.")
    
    image_number += 1

print("Done Interpreting the code.")











