import os
from PIL import Image


def compress_images(input_folder, output_folder, quality=90):

    os.makedirs(output_folder, exist_ok=True)   # Create output folder if it doesn't exist
    print(len(os.listdir(input_folder)))

    pic_num = 1
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)   # Creates the full path to the image file
            output_path = os.path.join(output_folder, filename) # ex: C:/Images/Raw(folder name)/DSC_001.JPG(file name)

            try:
                img = Image.open(input_path)

                # Convert PNG to JPEG (saves more space)
                if img.format == "PNG":
                    output_path = output_path.replace(".png", ".jpg")
                    img = img.convert("RGB")

                img.save(output_path, "JPEG", quality=quality, optimize=True)
                print(f"img{pic_num} Compressed: {filename} -> {output_path}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
        pic_num += 1

input_folder_path = "D:/file path"
output_folder_path = "C:/final path"

compress_images(input_folder=input_folder_path, output_folder=output_folder_path, quality=90)