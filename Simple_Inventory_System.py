# Define the Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name          # Product name
        self.price = price        # Product price
        self.quantity = quantity  # Product quantity in stock

    def display_info(self):
        """Displays the product's name, price, and quantity."""
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")
    
    def update_quantity(self, quantity_change):
        """Updates the quantity of the product. 
        A positive quantity_change adds stock, a negative quantity_change subtracts stock.
        """
        self.quantity += quantity_change
        if self.quantity < 0:
            self.quantity = 0  # Quantity can't be negative
        print(f"Updated quantity of {self.name}: {self.quantity}")

    def total_value(self):
        """Calculates and returns the total value of the product in stock (price * quantity)."""
        return self.price * self.quantity

# Define the Inventory class to manage the products
class Inventory:
    def __init__(self):
        self.products = []  # List to store all products in the inventory

    def add_product(self, product):
        """Adds a product to the inventory."""
        self.products.append(product)
        print(f"Product '{product.name}' has been added to the inventory.")

    def display_inventory(self):
        """Displays information about all products in the inventory."""
        if not self.products:
            print("No products available in the inventory.")
        else:
            print("\nInventory Details:")
            for product in self.products:
                product.display_info()
                print()  # Adding a space between products for readability

    def total_inventory_value(self):
        """Calculates and returns the total value of all products in the inventory."""
        total_value = sum(product.total_value() for product in self.products)
        return total_value

# Main function to demonstrate the inventory system
def main():
    # Create an instance of Inventory
    store_inventory = Inventory()

    # Create some Product objects
    product1 = Product("Laptop", 1200.00, 10)
    product2 = Product("Smartphone", 800.00, 15)
    product3 = Product("Headphones", 150.00, 30)

    # Add products to the inventory
    store_inventory.add_product(product1)
    store_inventory.add_product(product2)
    store_inventory.add_product(product3)

    # Display the inventory
    store_inventory.display_inventory()

    # Update quantities of some products
    print("\nUpdating product quantities:")
    product1.update_quantity(5)  # Adding 5 laptops to inventory
    product2.update_quantity(-3)  # Removing 3 smartphones from inventory

    # Display updated inventory
    store_inventory.display_inventory()

    # Calculate and display the total value of the inventory
    total_value = store_inventory.total_inventory_value()
    print(f"\nTotal value of inventory: ${total_value:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
