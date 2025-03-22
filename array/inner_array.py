# Accessing inner array elements using multiple variables in the for loop

info_array = [("freeBSD", "demon"), ("linux", "penguin"), ("mac", "apple")]

# x Wrong
for info in info_array:
    name, logo = info
    print(f"{name} logo: {logo}")

# ✓ Better
for name, logo in info_array:
    print(f"{name} logo: {logo}")
