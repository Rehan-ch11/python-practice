
menu = {
    1: ("Burger", 500),
    2: ("Pizza", 800),
    3: ("Fries", 250),
    4: ("Drink", 150)
}


def order():
    total = 0

    while True:
        print("\n1. Burger  2. Pizza  3. Fries  4. Drink  5. Exit")

        n = int(input("Choice: "))

        if n == 5:
            break

        elif n in menu:
            q = int(input("Quantity: "))
            total = total + menu[n][1] * q

        else:
            print("Invalid Choice")

    print("Final Bill:", total)

    with open("Orders.txt", "w") as f:
        f.write("Final Bill: " + str(total))


order()
