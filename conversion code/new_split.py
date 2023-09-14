import os
import shutil
import random

def split_dataset(base_dir, img_folder="images", label_folder="labels", img_ext=".jpg", label_ext=".txt"):
    # Source directories for images and labels
    img_source_dir = os.path.join(base_dir, img_folder)
    label_source_dir = os.path.join(base_dir, label_folder)
    
    # Create a main 'split' directory
    split_dir = os.path.join(base_dir, "split")
    
    # Directories for train, test, and valid inside 'split', each with subdirectories for images and labels
    train_img_dir = os.path.join(split_dir, "train", img_folder)
    train_label_dir = os.path.join(split_dir, "train", label_folder)
    
    test_img_dir = os.path.join(split_dir, "test", img_folder)
    test_label_dir = os.path.join(split_dir, "test", label_folder)
    
    valid_img_dir = os.path.join(split_dir, "valid", img_folder)
    valid_label_dir = os.path.join(split_dir, "valid", label_folder)

    for dir_path in [train_img_dir, train_label_dir, test_img_dir, test_label_dir, valid_img_dir, valid_label_dir]:
        os.makedirs(dir_path, exist_ok=True)
    
    # List all image files
    all_files = [f for f in os.listdir(img_source_dir) if f.endswith(img_ext)]
    random.shuffle(all_files)

    # Calculate the split sizes
    total_files = len(all_files)
    train_size = int(0.7 * total_files)
    valid_size = int(0.15 * total_files)
    # The rest go to test
    
    # Split the files
    train_files = all_files[:train_size]
    valid_files = all_files[train_size:train_size+valid_size]
    test_files = all_files[train_size+valid_size:]

    # Function to move files
    def move_files(files, img_dest_dir, label_dest_dir):
        for f in files:
            # Move image
            shutil.move(os.path.join(img_source_dir, f), img_dest_dir)
            
            # Move corresponding label
            label_name = f.replace(img_ext, label_ext)
            shutil.move(os.path.join(label_source_dir, label_name), label_dest_dir)

    # Move the files to respective directories
    move_files(train_files, train_img_dir, train_label_dir)
    move_files(valid_files, valid_img_dir, valid_label_dir)
    move_files(test_files, test_img_dir, test_label_dir)

# Usage
base_directory = "/home/soham/Oral-Cancer/RTMDET/combined_new"
split_dataset(base_directory)
