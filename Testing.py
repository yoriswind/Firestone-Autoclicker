import os

print("Current working directory:", os.getcwd())

image_path = 'Expedition Guild.png'
if os.path.exists(image_path):
    print("Image file exists.")
else:
    print("Image file not found.")