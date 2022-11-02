# this script renames images from a specific file
import os

file_path = os.chdir("E:\\#Research_Info\\video_dataset_folder_male\\image_dataset_folder")

i = 1

for image_file in os.listdir(file_path):
    renamed_file = f"{i}.png"
    os.rename(image_file, renamed_file)
    i += 1
    # print(f"Renamed {i}'th image: Ok")

    
    
    
    
    
    
    
    
    
    
    
