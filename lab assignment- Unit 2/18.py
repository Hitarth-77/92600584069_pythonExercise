shop_name = "Hitarth's Mall"

def shopping():
    discount = 10

    def calculate_bill():
        nonlocal discount

        price = float(input("Enter product price: "))

        print("Shop Name:", shop_name)
        print("Price:", price)
        print("Discount:", discount, "%")

    calculate_bill()

shopping()
