import json

# Load the JSON file
with open('/home/soham/Oral-Cancer/RTMDET/combined_new/split/valid/output_coco_format_valid.json', 'r') as f:
    data = json.load(f)

# Increment the IDs for images and annotations
for image in data['images']:
    image['id'] += 1

for ann in data['annotations']:
    ann['id'] += 1
    ann['image_id'] += 1

# Save the updated JSON back
with open('/home/soham/Oral-Cancer/RTMDET/combined_new/split/valid/output_coco_format_valid_updated.json', 'w') as f:
    json.dump(data, f)
