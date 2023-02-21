from PIL import Image
import os
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = None

# Prompt the user for an image file path
image_path = input("Enter the image file path: ")

# Check if the file exists
if not os.path.exists(image_path):
    print("The image file does not exist.")
    exit()

# Open the image and get its dimensions
img = Image.open(image_path)
width, height = img.size

# Convert the pixels to bits
bits = ""
for y in tqdm(range(height), desc="Converting to bits"):
    for x in range(width):
        pixel = img.getpixel((x, y))
        bit = "0" if pixel == 255 else "1"
        bits += bit

# Convert the bits to the original file and save it
if os.path.exists(os.path.splitext(image_path)[0]):
    print("The output file already exists.")
    output_path = input("Enter an output path: ")
else:
    output_path = os.path.splitext(image_path)[0]
    
with open(output_path, "wb") as f:
    byte = ""
    for i, bit in tqdm(enumerate(bits), desc="Converting to file", total=len(bits)):
        byte += bit
        if len(byte) == 8:
            f.write(bytes([int(byte, 2)]))
            byte = ""
    if byte:
        f.write(bytes([int(byte.ljust(8, "0"), 2)]))

print(f"The output file has been saved to '{output_path}'")
