
def bill(products):
    total = 0

    for p in products:
        p["total"] = p["price"] * p["quantity"]
        total += p["total"]

    if total > 10000:
        discount = total * 0.10
    else:
        discount = 0

    final = total - discount

    expensive = max(products, key=lambda p: p["price"])

    print("Total Bill:", total)
    print("Discount:", discount)
    print("Final Bill:", final)
    print("Most Expensive:", expensive["name"])

    with open("bill.txt", "w") as f:
        f.write(str(products))
        f.write("\nFinal Bill: " + str(final))


products = []

for i in range(5):
    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

bill(products)
