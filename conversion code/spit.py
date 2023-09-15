import os
import shutil

base_dir = '/home/soham/Oral-Cancer/RTMDET/6200_data'  # Path to your directory containing the train and valid folders
combined_dir = '/home/soham/Oral-Cancer/RTMDET/combined_new'  # Path where you want the combined folder to be

# Create combined directory and its sub-directories if they don't exist
os.makedirs(os.path.join(combined_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(combined_dir, 'labels'), exist_ok=True)

# Function to copy files from source to destination directory
def copy_files(src_dir, dst_dir, extension):
    for filename in os.listdir(src_dir):
        if filename.endswith(extension):
            shutil.copy(os.path.join(src_dir, filename), os.path.join(dst_dir, filename))

# Copy images and labels from train to combined
copy_files(os.path.join(base_dir, 'train', 'images'), os.path.join(combined_dir, 'images'), ".jpg")
copy_files(os.path.join(base_dir, 'train', 'labels'), os.path.join(combined_dir, 'labels'), ".txt")

# Copy images and labels from valid to combined
copy_files(os.path.join(base_dir, 'valid', 'images'), os.path.join(combined_dir, 'images'), ".jpg")
copy_files(os.path.join(base_dir, 'valid', 'labels'), os.path.join(combined_dir, 'labels'), ".txt")
