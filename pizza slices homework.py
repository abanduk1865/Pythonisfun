import math

pizzaslices = 8
family = 4
eat = int(input("How many slices does each member eat? "))

totalslices = eat * family
#print(totalslices)
wholepizza = math.ceil(totalslices / pizzaslices)
#print("Whole pizzas to order", wholepizza)
leftbymodulo = totalslices%pizzaslices
#print(leftbymodulo)

print(" Total number of pizzas to buy", wholepizza)
print("total slices left", leftbymodulo)
