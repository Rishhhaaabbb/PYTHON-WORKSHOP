# Create storage to store items
storage = []
for i in range(4):
    item = str(input("Enter item to add to storage: "))  # Prompt user to enter items
    storage.append(item)  # Store items to storage

print("Initial storage:", storage)

print("Customer requests to see the list of items.")
print("Available items:", storage)

# Customer requests for an item from storage
item_to_buy = str(input("Enter item asked by the customer: "))

# If item is available in storage
if item_to_buy in storage:
    storage.remove(item_to_buy)
    print(f"Owner delivers {item_to_buy} to customer.")
# If item is not in storage
else:
    print(f"Item '{item_to_buy}' not found in storage.")

# Prints remaining items not purchased by customer
print("Updated storage:", storage)