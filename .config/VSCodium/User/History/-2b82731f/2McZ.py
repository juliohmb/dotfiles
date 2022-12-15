import os
from PIL import Image
from datetime import datetime

# Get the current date
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")

# Create the PDF file name
pdf_file_name = f"comprovantes_{date_str}.pdf"

# Open the PDF file
pdf_file = open(pdf_file_name, "wb")

# Sort the images alphabetically
image_file_names = sorted(os.listdir("."))

# Loop through all images in the current directory
for image_file_name in image_file_names:
  # Check if the file is an image
  if image_file_name.endswith(".png") or image_file_name.endswith(".jpg") or image_file_name.endswith(".jpeg"):
    # Open the image file
    image_file = Image.open(image_file_name)

    # Convert the image to RGB mode (if it's not already in that mode)
    image_file = image_file.convert("RGB")

    # Save the image to the PDF file
    image_file.save(pdf_file, "PDF", resolution=100.0)

# Close the PDF file
pdf_file.close()
