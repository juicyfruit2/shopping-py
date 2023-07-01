# created a shopping list program 

# asking for the user to enter any 3 products 
product1 = input("Enter your 1st product:")
print(product1)
product2 = input("Enter your 2nd product:")
print(product2)
product3 = input("Enter your 3rd product:")
print(product3)

# the user to enter the price of the 3 products 
price1 = float(input("what is the price of product 1 ?:"))
print(price1)
price2 = float(input("what is the price of product 2 ?:"))
print(price2)
price3 = float(input("what is the price of product 3 ?:"))
print(price3)

# Adding up all the prices to get the total price / by 3 to get the average which is rounded off to 2 decimal plces 
total_price_of_3_products = price1 + price2 + price3
print(total_price_of_3_products)
average = total_price_of_3_products / 3
print(round(average,2))

# used the format function to print out the sentance 
print("The Total of {},{},{}, is R{} and the average price of items R{}".format(product1,product2,product3,total_price_of_3_products,average))