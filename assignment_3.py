
# Assignment 3 - Extended Listing CLI with subclasses

class Listing:
    def __init__(self, description, price):
        self.__description = description
        self.__price = price

    def __str__(self):
        return (f"Description: {self.__description}\n"
                f"Price: ${self.__price:,.2f}\n")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    @property
    def description(self):
        return self.__description


# Subclass for Houses
class HouseListing(Listing):
    def __init__(self, address, price, bedrooms, bathrooms, sqft):
        super().__init__(f"House at {address}", price)
        self.__address = address
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__sqft = sqft

    def __str__(self):
        return (super().__str__() +
                f"Address: {self.__address}\n"
                f"Bedrooms: {self.__bedrooms}\n"
                f"Bathrooms: {self.__bathrooms}\n"
                f"Square Feet: {self.__sqft}\n")


# Subclass for Furniture 
class FurnitureListing(Listing):
    def __init__(self, name, price, material, condition):
        super().__init__(f"Furniture: {name}", price)
        self.__name = name
        self.__material = material
        self.__condition = condition

    def __str__(self):
        return (super().__str__() +
                f"Name: {self.__name}\n"
                f"Material: {self.__material}\n"
                f"Condition: {self.__condition}\n")


# Subclass for Perishable Goods
class PerishableListing(Listing):
    def __init__(self, name, price, expiry_date, weight):
        super().__init__(f"Perishable: {name}", price)
        self.__name = name
        self.__expiry_date = expiry_date
        self.__weight = weight

    def __str__(self):
        return (super().__str__() +
                f"Name: {self.__name}\n"
                f"Expiry Date: {self.__expiry_date}\n"
                f"Weight: {self.__weight} kg\n")


def main():
    listings = [
        HouseListing("1234 Main St, Anytown, USA", 350000.00, 3, 2, 1800),
        FurnitureListing("Wooden Dining Table", 500.00, "Oak Wood", "Good"),
        PerishableListing("Milk", 2.50, "2025-09-20", 1.0)
    ]

    while True:
        print("\nWelcome to the Multi-Listing CLI.")
        print("1. See all listings")
        print("2. Add a new house listing")
        print("3. Add a new furniture listing")
        print("4. Add a new perishable listing")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- Current Listings ---")
            if not listings:
                print("No listings available.")
            else:
                for i, listing in enumerate(listings, 1):
                    print(f"\n--- Listing #{i} ---")
                    print(listing)

        elif choice == '2':
            try:
                addr = input("Enter address: ")
                price = float(input("Enter price: "))
                beds = int(input("Bedrooms: "))
                baths = int(input("Bathrooms: "))
                sqft = int(input("Square feet: "))
                listings.append(HouseListing(addr, price, beds, baths, sqft))
                print("House listing added!")
            except ValueError:
                print("Invalid input for house listing.")

        elif choice == '3':
            try:
                name = input("Furniture name: ")
                price = float(input("Price: "))
                material = input("Material: ")
                condition = input("Condition: ")
                listings.append(FurnitureListing(name, price, material, condition))
                print("Furniture listing added!")
            except ValueError:
                print("Invalid input for furniture listing.")

        elif choice == '4':
            try:
                name = input("Perishable item name: ")
                price = float(input("Price: "))
                expiry = input("Expiry date (YYYY-MM-DD): ")
                weight = float(input("Weight in kg: "))
                listings.append(PerishableListing(name, price, expiry, weight))
                print("Perishable listing added!")
            except ValueError:
                print("Invalid input for perishable listing.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Not a valid choice.")

if __name__ == "__main__":
    main()
