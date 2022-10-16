# 2022-10-12 MOCK TEST
import math

def pizzaEating():
    overallRadius = float(input("Enter the overall radius of the pizza (in cm): "))
    maxPizzaCalories = int(input("Enter the max number of pizza related calories you should eat in a month: "))

    radiusToppingRegion = overallRadius - 4
    print("The radius of the toppings region is " + str(radiusToppingRegion) + "cm.")
    
    toppingArea = math.pi * radiusToppingRegion ** 2
    print("The area of the topping region is "+ str(toppingArea)+ "cm2.")

    overallArea = math.pi * overallRadius ** 2
    baseCaloriesPerCM = 0.9
    toppingCaloriesPerCM = 2.7
    baseCalories = overallArea * baseCaloriesPerCM
    toppingCalories = toppingArea * toppingCaloriesPerCM
    overallCalories = baseCalories + toppingCalories
    print("The number of calories in this pizza is ", str(overallCalories)+ ".")

    maxPizzaPerMonth = maxPizzaCalories // overallCalories
    print(maxPizzaPerMonth)
    print("The maximum number of complete pizzas of this size we should eat in a month is " + str(maxPizzaPerMonth) + ".")



pizzaEating()