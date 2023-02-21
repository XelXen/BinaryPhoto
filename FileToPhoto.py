from PIL import Image
import os
from tqdm import tqdm

# Prompt the user for a file path
file_path = input("Enter the file path: ")

# Check if the file exists
if not os.path.exists(file_path):
    print("The file does not exist.")
    exit()

# Extract the file name and extension from the file path
file_name, file_ext = os.path.splitext(file_path)

# Open the file and read the contents
with open(file_path, "rb") as f:
    content = f.read()

# Convert the content to bits
num_bytes = len(content)
with tqdm(total=num_bytes, desc="Converting to bits") as pbar:
    bits = []
    for byte in content:
        bits.extend(format(byte, '08b'))
        pbar.update(1)

# Calculate the width and height of the image based on the number of bits
num_bits = len(bits)
width = int(num_bits**0.5) + 1
height = int(num_bits/width) + 1

# Create a new image
img = Image.new('1', (width, height), 1)

# Set the pixels based on the bits
with tqdm(total=num_bits, desc="Setting pixels") as pbar:
    for i, bit in enumerate(bits):
        x = i % width
        y = int(i/width)
        color = 0 if bit == '1' else 1
        img.putpixel((x, y), color)
        pbar.update(1)

# Save the image with the file name and extension
image_path = f"{file_name}{file_ext}.png"
img.save(image_path)
print(f"The image has been saved as {image_path}.")
