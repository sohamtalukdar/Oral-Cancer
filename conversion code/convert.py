import os
import json
from PIL import Image

# Paths
yolo_annotation_dir = '/home/soham/Oral-Cancer/RTMDET/combined_new/split/valid/labels'
image_dir = '/home/soham/Oral-Cancer/RTMDET/combined_new/split/valid/images'
output_json_path = '/home/soham/Oral-Cancer/RTMDET/combined_new/split/valid/output_coco_format_valid.json'

# Load category names (you should define these based on your dataset)
categories = [{'id': 0, 'name': 'malignant'}, {'id': 1, 'name': 'non-malignant'}]

# Initialize COCO dataset format
coco_data = {
    "images": [],
    "annotations": [],
    "categories": categories
}

image_id = 0
annotation_id = 0

for filename in os.listdir(yolo_annotation_dir):
    if filename.endswith(".txt"):
        image_path = os.path.join(image_dir, filename.replace(".txt", ".jpg"))
        
        # Get the image width and height
        with Image.open(image_path) as img:
            image_width, image_height = img.size

        yolo_annotation_path = os.path.join(yolo_annotation_dir, filename)

        # Add image information
        coco_data["images"].append({
            "file_name": filename.replace(".txt", ".jpg"),
            "id": image_id
        })

        with open(yolo_annotation_path, "r") as file:
            for line in file:
                data = line.strip().split()
                try:
                    category_id, x_center, y_center, width, height = map(float, data)
                except ValueError:
                    print(f"Error in file: {filename}, line: {line}")
                    continue
                # Convert YOLO format to COCO format
                x_min = (x_center - width / 2) * image_width
                y_min = (y_center - height / 2) * image_height
                bbox_width = width * image_width
                bbox_height = height * image_height

                # Add annotation
                coco_data["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": int(category_id),
                    "bbox": [x_min, y_min, bbox_width, bbox_height],
                    "area": bbox_width * bbox_height,
                    "iscrowd": 0
                })

                annotation_id += 1

        image_id += 1

# Save to JSON
with open(output_json_path, "w") as json_file:
    json.dump(coco_data, json_file)
