# Access to inner array elements using multiple variables in for loop

info_array = [("freeBSD", "demon"), ("linux", "penguin"), ("mac", "apple")]

for info in info_array:
    name, logo = info
    print(f"{name} logo: {logo}")

for name, logo in info_array:
    print(f"{name} logo: {logo}")
