pizza={
    "crust":"peproni",
    "topping":["chesse","sosis","olive"]
}
print(f"your order a{pizza["crust"]}-crust pizza"
      "with the folling toppings")

for topping in pizza["topping"]:
    print(f"\t{topping}")