import os

combined_dir = '/home/soham/Oral-Cancer/RTMDET/combined'  # Path where your combined folder is located

image_dir = os.path.join(combined_dir, 'images')
label_dir = os.path.join(combined_dir, 'labels')

# List all image and label filenames
image_files = set(os.listdir(image_dir))
label_files = set(os.listdir(label_dir))

# Convert image filenames to the format of label filenames and vice versa
image_files_as_labels = {f.replace('.jpg', '.txt') for f in image_files}
label_files_as_images = {f.replace('.txt', '.jpg') for f in label_files}

# Find unmatched images and labels
unmatched_images = image_files - label_files_as_images
unmatched_labels = label_files - image_files_as_labels

# Remove unmatched images and labels
for img in unmatched_images:
    os.remove(os.path.join(image_dir, img))
    print(f"Removed unmatched image: {img}")

for lbl in unmatched_labels:
    os.remove(os.path.join(label_dir, lbl))
    print(f"Removed unmatched label: {lbl}")
