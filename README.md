# Image Compression Script

This Python script compresses images in a specified folder and saves the compressed versions in an output folder. It supports `.jpg`, `.jpeg`, and `.png` files. PNG images are converted to JPEG to save more space.


## Features

- Compress `.jpg`, `.jpeg`, and `.png` images.
- Convert PNG images to JPEG for better compression.
- Preserve original filenames in the output folder.
- Customizable image quality (default is 90%).
- Automatically creates the output folder if it doesn’t exist.
- Displays progress in the console with image numbers and paths.
- Handles exceptions gracefully for invalid or corrupted files.


## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) library

Install Pillow using pip if not already installed: `pip install Pillow`

## Usage

1. Clone or download the script.
2. Set the input and output folder paths:

```bash
input_folder_path = "D:/file path"
output_folder_path = "C:/final path"
```
3. Call the function with optional `quality` parameter (default is 90):

```bash
compress_images(input_folder=input_folder_path, output_folder=output_folder_path, quality=90)
```
4. Run the script:

```bash 
python compress_images.py
```

The compressed images will appear in the specified output folder.