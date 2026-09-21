shop_name = "Hitarth's Mall"

def shopping():
    discount = 10

    def calculate_bill():
        nonlocal discount

        price = float(input("Enter product price: "))
        discount_amount = price * discount/100;
        final_price= price - discount_amount;

        print("Shop Name:", shop_name)
        print("Price:", price)
        print("Discount is:",discount_amount);
        print("Final Price is:",final_price);

    calculate_bill()

shopping()
