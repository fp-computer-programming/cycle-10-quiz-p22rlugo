# Ryan Lugo: RJL 2/2/22

prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

# Question 1
def average_prices(table):
    total_cost = 0 # Created a new total cost for returning/adding the other numbers
    average = 0 # Created a average so we can return it
    if type(table) == list:
        for price in table:
            total_cost += price
        average = total_cost / len(table) # Divide it by the len for average (No strict dvision??)
    else:
        print("The prices list is not an list!")
    
    return average

print(average_prices(prices))

# Question 2
def reduce_prices(table):
    new_prices = [] # created a new table/list so we can just apppend it then return it
    if type(table) == list:
        for prices in table:
            new_prices.append(prices-5)
    else:
        print("The prices list is not an list!")

    return new_prices
print(reduce_prices(prices))

# Question 3
def money_made(prices,sales):
    total_cost = 0 # Same thing of creating a new number holder so we can return/use it/modify it
    counter = 0 # counter being used to go inside of the sales table/list to find it's value
    if type(prices) == list and type(sales) == list: # checking if they are both a list
        if len(prices) == len(sales): # checking if they are equal to each other to ensure they didn't try to be sly
            for price in prices:
                print(sales[counter],"item was sold for","$"+str(price)) # Printing out what each item was sold for (Had to force them into strings to ensure you get no errors)
                counter += 1 # Adding + 1 to the counter for the sales table to be read
                total_cost += price # Adding the the total price so it can be returned later
        else:
            print("The Prices list, and the sales list are not the same length!")
    else:
        print("One of the two lists is not an actual list!")
    return "Here's the total cost of them all "+"$"+str(total_cost)+"." # Return this
print(money_made(prices,sales))

# Quesiton 4
def cost_more(table):
    new_prices = [] # Created a new table/list to be returned
    if type(table) == list:
        for prices in table:
            if prices > 40: # Did a else and a if to check if it meets the requirements if not it will still append it to be returned
                new_prices.append(prices-10)
            else:
                new_prices.append(prices)
    else:
        print("The given prices is not an list!")
    return new_prices
cost_more(prices)

# Quesiton 5
def item_cost(prices,items):
    new_table = [] # create a new table to be returned
    table_counter = 0 # Made a table counter since the items list has another list inside of it (Supports any size of list)
    counter = 0 # counter being used to find the index in the list
    if type(prices) == list and type(items) == list:
        for price in prices:
            new_table.append(items[table_counter][counter]+" "+"$"+str(price)) # Since the default values of each is already set to 0 it will go for the first list inside of the items list
            counter += 1 # add the number for the counter to find the index inside

            if counter >= len(items[table_counter]): # If the counter reaches the end of taht specific table/list reset the counter for another talbe/list then add + 1 to the table counter to find the next table inside of the items table/list
                table_counter += 1
                counter = 0
    else:
        print("One of the lists given is not an list!")
    return new_table
print(item_cost(prices,items))