name = 4808

for groups in [1,2,3,4]:
    for group in ["voltage", "current", "soc" , "balance", "status"]:
        for param in range(1,5):
            print(f"name: {name}, Group_{param} Group_{group}")
            name += 2


# name = 8
# for group in [1, 2, 3, 4]:
#     for param in ["voltage", "temperature", "internal resistance", "soc", "soh"]:
#         for cell in range(1, 121):
#             print(f"name: {name} Group {group}, Cell {cell}, {param}")
#             name += 2

