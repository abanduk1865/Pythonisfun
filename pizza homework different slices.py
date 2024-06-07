import math

pizzaslices = 8
family = 4

Pl = int(input("How many slices of pizza does brother eat: "))
P2 = int(input("How many slices of pizza does mom eat: "))
P3 = int(input("How many slices of pizza does dad eat: "))
P4 = int(input("How many slices of pizza do you eat: "))

totalslices = Pl + P2 + P3 + P4

print("Total slices eaten:", totalslices)

wholepizza = math.ceil(totalslices / pizzaslices)

leftbymodulo = totalslices % pizzaslices

if leftbymodulo == 0:
    print("No slices left")
else:
    leftover = 8 - leftbymodulo
    leftover2 = wholepizza * 8 - totalslices
    print("Total number of pizzas to buy:", wholepizza)
    print("Total slices left", leftover)
    print("Total slices left", leftover2)
