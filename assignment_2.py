# simple program for house listing management
# yeah it's kinda like a house flipper CLI thing

class Listing:
    def __init__(self, address, price, bedrooms, bathrooms, sqft):
        # private-ish vars, dont mess with em directly
        self.__address = address
        self.__price = price
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__sqft = sqft

    def __str__(self):
        # printing the listing in a nice format
        return (f"Address: {self.__address}\n"
                f"Price: ${self.__price:,.2f}\n"
                f"Bedrooms: {self.__bedrooms}\n"
                f"Bathrooms: {self.__bathrooms}\n"
                f"Sq. Ft.: {self.__sqft}\n")

    # getter and setter for price cuz u might wanna change it later
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("uhh nope, price must be positive")

    # also added one for addrss just in case
    @property
    def address(self):
        return self.__address


def main():
    # some sample listings to start with
    listings = [
        Listing("1234 Main St, Anytown, USA", 350000.00, 3, 2, 1800),
        Listing("5678 Oak Ln, Suburbia, USA", 275000.00, 4, 3, 2200),
        Listing("9101 Pine Rd, Countryside, USA", 425000.00, 5, 4, 2800)
    ]

    while True:
        # basic menu every time
        print("\nWelcome to the House Flipper CLI thing.")
        print("1. See all listings")
        print("2. Check a specific listing's details")
        print("3. Buy a house")
        print("4. Add a new listing")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- Available Listings ---")
            if not listings:
                print("No listings right now, sorry.")
            else:
                for i, house in enumerate(listings, 1):
                    print(f"\n--- Listing #{i} ---")
                    print(house)

        elif choice == '2':
            try:
                num = int(input("Enter the number of the listing to view: "))
                if 1 <= num <= len(listings):
                    print("\n--- Listing Details ---")
                    print(listings[num - 1])
                else:
                    print("Hmm that listing number doesnt exist.")
            except ValueError:
                print("Enter a number dude...")

        elif choice == '3':
            try:
                num = int(input("Enter the number of the listing to purchase: "))
                if 1 <= num <= len(listings):
                    purchased = listings.pop(num - 1)
                    print(f"\nYou just bought the house at {purchased.address}.")
                    print("It's off the market now.")
                else:
                    print("That listing number aint valid.")
            except ValueError:
                print("Numbers only, thx.")

        elif choice == '4':
            print("\n--- Adding a New Listing ---")
            try:
                address = input("Enter the address: ")
                price = float(input("Enter the price: "))
                bedrooms = int(input("How many bedrooms? "))
                bathrooms = int(input("And the bathrooms? "))
                sqft = int(input("Enter the square footage (approx): "))

                new_listing = Listing(address, price, bedrooms, bathrooms, sqft)
                listings.append(new_listing)
                print(f"\nListing for {address} has been added. yay!")
            except ValueError:
                print("Something went wrong lol. enter nums where it ask for nums...")

        elif choice == '5':
            print("Ok bye ")
            break

        else:
            print("Not a valid choice, try again?")


if __name__ == "__main__":
    main()
