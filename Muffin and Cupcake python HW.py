buying = input('do you want a muffin or a cupcake?')

Muffins = 10
Cupcakes = 10

while buying != "0":
    if buying == "muffin" and Muffins > 0:
        Muffins -= 1
        if Muffins == 0:
            print("Muffins Out of stock")
    elif buying == "cupcake" and Cupcakes > 0:
        Cupcakes -= 1
        if Cupcakes == 0:
            print("Cupcakes Out of stock")
    buying = input('do you want a muffin or a cupcake?')

print("muffins:", Muffins, "cupcakes:", Cupcakes)



