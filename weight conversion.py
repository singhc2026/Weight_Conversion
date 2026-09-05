weight = float(input("Enter your weight " ))
unit = input("kilogram or Pound?(K or L): ")

if unit == "K":
    weight = weight * 2.345
    unit = "pound."
    print(f"your weight is:{round(weight, 1)} {unit}")

elif unit == "L":
        weight = weight /2.345
        unit = "Kilo."
        print(f"your weight is:{round(weight, 1)} {unit}")

else:
    print(f"{unit} was not recognized")


