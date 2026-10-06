class Product:
    def __init__(self, weight, name, price, variety, brand, size, make):
        self.weight = float(weight)
        self.name = name
        self.price = float(price)
        self.variety = variety
        self.brand = brand
        self.size = size
        self.make = make

product_list = [
    Product(1.0, "Apple", 1.99, "Fruit", "Organic", "Medium", "Farm Fresh"),
    Product(2.0, "Bread", 2.49, "Bakery", "Whole Wheat", "Large", "Bake Best"),
    Product(1.5, "Milk", 3.49, "Dairy", "Low Fat", "Small", "Dairy Delight"),
    Product(0.5, "Eggs", 2.99, "Dairy", "Free Range", "Medium", "Farm Fresh"),
    Product(1.2, "Biscoff Spread", 4.99, "Spread", "Biscoff", "Small", "Lotus"),
    Product(0.8, "Cheese", 5.49, "Dairy", "Cheddar", "Medium", "Cheese Co."),
    Product(1.0, "Chicken", 7.99, "Meat", "Organic", "Large", "Farm Fresh"),
    Product(0.6, "Salmon", 9.99, "Seafood", "Wild Caught", "Small", "Ocean Fresh"),
    Product(1.5, "Pasta", 2.99, "Grains", "Whole Wheat", "Large", "Pasta Co."),
    Product(0.4, "Tomato Sauce", 1.49, "Condiment", "Organic", "Small", "Sauce Co."),
]

class Shopping_Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

print("#####Double Ds#####")
print("")
input("Would you like to a look at our offerings? ")

