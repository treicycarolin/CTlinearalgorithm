def linear_search_marketplace(items, target_item):
   
    for item in items:
        name, details = item
        if name == target_item:
            return details
    return None

# item list
marketplace_items = [
    ("Laptop", {"brand": "Apple", "price": 1500}),
    ("Smartphone", {"brand": "Samsung", "price": 1000}),
    ("Tablet", {"brand": "Microsoft", "price": 600}),
    ("Headphones", {"brand": "Sony", "price": 200}),
    ("Smartwatch", {"brand": "Apple", "price": 400})
]

# item to search for
target = "Headphones"

# linear search
item_details = linear_search_marketplace(marketplace_items, target)

# Print result
if item_details:
    print(f"Item '{target}' found with details: {item_details}")
else:
    print(f"Item '{target}' not found in the marketplace.")
