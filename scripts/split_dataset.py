# scripts/split_dataset.py

import os
import shutil
import random

# Paths to original images
original_cats = "archive/kagglecatsanddogs_3367a/PetImages/Cat"
original_dogs = "archive/kagglecatsanddogs_3367a/PetImages/Dog"

# Paths to new dataset folders
train_cats = "dataset/train/cats"
train_dogs = "dataset/train/dogs"
val_cats = "dataset/validation/cats"
val_dogs = "dataset/validation/dogs"

# Create directories if they don't exist
for path in [train_cats, train_dogs, val_cats, val_dogs]:
    os.makedirs(path, exist_ok=True)

# Function to split images
def split_data(source, train_path, val_path, split_ratio=0.8):
    files = [f for f in os.listdir(source) if f.endswith(".jpg")]
    random.shuffle(files)
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    val_files = files[split_index:]

    for f in train_files:
        shutil.copy(os.path.join(source, f), os.path.join(train_path, f))
    for f in val_files:
        shutil.copy(os.path.join(source, f), os.path.join(val_path, f))

# Split Cats and Dogs
split_data(original_cats, train_cats, val_cats)
split_data(original_dogs, train_dogs, val_dogs)

print("Dataset split complete!")
