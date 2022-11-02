from PIL import Image
import glob

file_path = "E:\\#Research_Info\\video_dataset_folder_male\\image_dataset_folder\\1.png" # starting from this path and item

image = Image.open(file_path)
# print(f"{image.size}")
# print(f"{image.mode}")

original_image_list = []
resized_image_list = [] 

# Append all image from file to original_image_list[]
for file_name in glob.glob("E:\\#Research_Info\\video_dataset_folder_male\\image_dataset_folder\\*.png"):
    image = Image.open(file_name)
    original_image_list.append(image)

# Resize all images and append on resized list
for img in original_image_list:
    img = img.resize((512, 512)) # specific image dimension to resize 512x512
    resized_image_list.append(img)

# save the resized image in new folder
for (i, new_img) in enumerate(resized_image_list):
    # new_img.save(f"{E:\\#Research_Info\\video_dataset_folder\\resized_dataset_one}{i+1}.png")
    new_img.save('{}{}{}'.format('E:\\#Research_Info\\video_dataset_folder_male\\resized_dataset_folder\\', i+1, '.png')) # storing the output in another folder
    
    
    
    
    
    
    
