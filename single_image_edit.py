from PIL import Image

def compress_images(input_img, output_img, quality=90):
    img = Image.open(input_img)

    img.save(output_img, "JPEG", quality=quality, optimize=True)
    print(f"Compressed: {input_img} -> {output_img}")


input_img_path = "D:/Downloads/rohit_img.jpg"
output_img_path = "C:/Users/Desktop/final_resized_img/rohit.jpg"

compress_images(input_img=input_img_path, output_img=output_img_path, quality=80)
