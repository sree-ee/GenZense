import json
from collections import Counter

# Load fashion items from JSON file
def load_fashion_items(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Count attributes and find dominant features
def find_dominant_attributes(fashion_items):
    attribute_counts = {
        "neckline_type": Counter(),
        "sleeve_type": Counter(),
        "waist_fit": Counter(),
        "print_type": Counter(),
        "lower_length": Counter(),
        "fit_type": Counter(),
        "color": Counter()
    }

    # Count occurrences of each attribute
    for item in fashion_items:
        attributes = item['attributes']
        for attribute, value in attributes.items():
            attribute_counts[attribute][value] += 1

    # Find dominant attributes for each category
    dominant_attributes = {}
    for attribute, counts in attribute_counts.items():
        dominant_value, dominant_count = counts.most_common(1)[0]
        dominant_attributes[attribute] = {
            "value": dominant_value,
            "count": dominant_count
        }

    return dominant_attributes

# Specify the path to your JSON file
file_path = 'fashion_items.json'

# Load items and find dominant attributes
fashion_items = load_fashion_items(file_path)
dominant_attributes = find_dominant_attributes(fashion_items)

# Output the results
print("Dominant Attributes:")
for attribute, info in dominant_attributes.items():
    print(f"{attribute}: {info['value']} (Count: {info['count']})")
