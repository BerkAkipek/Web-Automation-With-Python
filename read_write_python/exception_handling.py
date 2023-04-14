items_in_cart = 0

if items_in_cart != 0:
    raise Exception("Item exist in cart")

assert(items_in_cart == 0)
# Assert function raise an error i given condition met

try:
    with open("somefile.txt") as file:
        content = file.read()
except Exception as e:
    print(e)

