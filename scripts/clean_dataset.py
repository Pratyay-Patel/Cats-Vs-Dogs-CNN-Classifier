# scripts/clean_dataset.py

import os
from PIL import Image

# Paths to original images
folders = [
    "archive/kagglecatsanddogs_3367a/PetImages/Cat",
    "archive/kagglecatsanddogs_3367a/PetImages/Dog"
]

print("Checking for corrupted images...")

for folder in folders:
    count_removed = 0
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        try:
            img = Image.open(path)
            img.verify()  # Verify the image is valid
        except (IOError, SyntaxError) as e:
            print(f"Corrupted image found and removed: {path}")
            os.remove(path)
            count_removed += 1
    print(f"Removed {count_removed} corrupted images from {folder}")

print("Dataset cleaning complete!")
