#CTI-110
#P2HW2-Tip,Tax,and Total
#Tiffany Kuhns
#2/23/2018

print ("Please enter the cost of the meal.")
foodcost= float(input(""))
tip= (foodcost * .18)
salestax= (foodcost * .07)
totalcost= (foodcost + tip + salestax)
print ("Food Cost: ", foodcost)
print ("Tip: ", tip)
print ("Sales Tax: ",salestax)
print ("Your total: ",totalcost)
