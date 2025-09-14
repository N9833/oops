class Listing:
    def __init__(self, address, price, bedrooms, bathrooms, sqft):
        self.__address = address
        self.__price = price
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__sqft = sqft

    def __str__(self):
        return (f"Address: {self.__address}\n"
                f"Price: ${self.__price:,.2f}\n"
                f"Bedrooms: {self.__bedrooms}\n"
                f"Bathrooms: {self.__bathrooms}\n"
                f"Sq. Ft.: {self.__sqft}\n")

    # Getter and setter for price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be a positive value.")

    # I have added property to get address 
    @property
    def address(self):
        return self.__address


def main():
    listings = [
        Listing("1234 Main St, Anytown, USA", 350000.00, 3, 2, 1800),
        Listing("5678 Oak Ln, Suburbia, USA", 275000.00, 4, 3, 2200),
        Listing("9101 Pine Rd, Countryside, USA", 425000.00, 5, 4, 2800)
    ]

    while True:
        print("\nWelcome to the House Flipper CLI.")
        print("1. See all listings")
        print("2. Check a specific listing's details")
        print("3. Buy a house")
        print("4. Add a new listing")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- Available Listings ---")
            if not listings:
                print("No listings right now.")
            else:
                for i, house in enumerate(listings, 1):
                    print(f"--- Listing #{i} ---")
                    print(house)

        elif choice == '2':
            try:
                num = int(input("Enter the number of the listing to view: "))
                if 1 <= num <= len(listings):
                    print("\n--- Listing Details ---")
                    print(listings[num - 1])
                else:
                    print("That listing number doesn't exist.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            try:
                num = int(input("Enter the number of the listing to purchase: "))
                if 1 <= num <= len(listings):
                    purchased = listings.pop(num - 1)
                    print(f"\nYou just bought the house at {purchased.address}.")
                    print("It's no longer listed.")
                else:
                    print("That listing number doesn't exist.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("\n--- Adding a New Listing ---")
            try:
                address = input("Enter the address: ")
                price = float(input("Enter the price: "))
                bedrooms = int(input("Enter the number of bedrooms: "))
                bathrooms = int(input("Enter the number of bathrooms: "))
                sqft = int(input("Enter the square foot: "))

                new_listing = Listing(address, price, bedrooms, bathrooms, sqft)
                listings.append(new_listing)
                print(f"\nListing for {address} has been added.")
            except ValueError:
                print("Something went wrong. fix that  you're entering numbers where needed.")

        elif choice == '5':
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()



