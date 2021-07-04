menu={
    "veg": {
                "starter":{"A":100,"B":200,"C":300},
                "main course":{"D":400,"E":500,"F":600}
           }
}
print(menu)
print(menu.get("veg").get("starter").get("A"))
print(menu.get("veg").get("main course").get("E"))