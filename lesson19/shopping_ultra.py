import json

shoplist = list(input("Write your shoping list"))
filename = 'shoplist.json'

with open("shoplist.json", "w") as f:
    json.dump(shoplist, f)
    print("Add to list" + shoplist)

with open(filename) as fi:
    user = json.load(fi)
    print("Your shopping list" + user)
