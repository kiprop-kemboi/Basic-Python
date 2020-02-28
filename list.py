shoe = ["nike", "adidas", "power", "tommy takkies", "safari"]
selection =  str(input("select the your brand\n"))

for n in shoe :
    print(n)
    if n == "nike":
        print("wow! great sport")

    elif n =="adidas":
        print("get you wardrope flourishing")

    elif n == "power":
        print("increase your day well fit energy")

    elif n == "tommy takkies":
        print("fell fresh with tommy")

    elif n == "safari":
        print("visit our savvannah to get pleasure of safari")

    else:
        print("still searching")
        break
