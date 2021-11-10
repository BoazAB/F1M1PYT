GroceryList = "milk" + "cheese" + "cookies" + "tangerenes" + "manderines"
def shopping():
    print("what do you put in your cart?")
    P = input()
    ShoppingCart = (GroceryList - P)
    GroceryList = ShoppingCart
    if ShoppingCart == GroceryList:
        print("You're done shopping.")
        shopping()
    else:
        print("je hebt nog " + ShoppingCart + " nodig")
shopping()