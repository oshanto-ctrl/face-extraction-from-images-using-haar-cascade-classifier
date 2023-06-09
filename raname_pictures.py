# this script renames images from a specific file
# import necessary modules
import os

# in file_path variable you set your own image dataset folder path
file_path = os.chdir("E:\\#Research_Info\\video_dataset_folder_male\\image_dataset_folder")

i = 1 # starting from image no. 1 (example: 1.png)

for image_file in os.listdir(file_path):
    renamed_file = f"{i}.png"
    os.rename(image_file, renamed_file)
    i += 1
    # print(f"Renamed {i}'th image: Ok")
  
# Completion
print("Renaming Complete.")

    
    
    
    
    
    
    
    
    
    
    
