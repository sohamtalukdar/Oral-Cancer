import json

# Load the JSON file
with open("/mnt/data/imp.json", "r") as file:
    data = json.load(file)

# Increment category IDs
for category in data["categories"]:
    category["id"] += 1

# Adjust annotations to use the updated category IDs
for annotation in data["annotations"]:
    annotation["category_id"] += 1

# Save the updated JSON
with open("/mnt/data/adjusted_imp.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON has been adjusted and saved as 'adjusted_imp.json'.")
