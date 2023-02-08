
#========Define classes=======

class Shoe:
    #define attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    #define methods with the class

    
    def get_cost(self):
        'returns cost'
        return (self.cost)

    def get_quantity(self):
        'returns quantity'
        return (self.quantity)

    def __str__(shoe):
        'returns a string in the correct format to be written to inventory.txt'
        shoe_str = (f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
        return (shoe_str)
        

#==========Functions outside the class==============


def read_shoes_data():

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    
    try:
        shoe_list = []
        with open ("inventory.txt", "r+") as f:
            count = 0
            for line in f:
                #generate a list of Shoe objects with attributes taken from the string lines in inventory.txt, skipping the first line
                if count != 0:
                    line = line.strip("\n")
                    country = line.split(",")[0]
                    code = line.split(",")[1]
                    product = line.split(",")[2]
                    cost = line.split(",")[3]
                    quantity = line.split(",")[4]
                    #generate a Shoe object based on these values and append this to shoe_list
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
                
                count +=1
            
            return (shoe_list)

    except:
        print ("I am sorry the file is of the wrong format")

def capture_shoes(shoe_list):

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    
    print("You have selected to add a shoe")

    #get country
    country = input("Please enter the name of the country: ")
    print("")

    #get code
    code = input ("Please enter the shoe code: ")
    print ("")

    #get name
    product = input ("Please enter the name of the product: ")
    print ("")

    #get cost and round to 2dp with error handling
    while True:
        cost = input("Please enter the cost of the product: ")
        print("")
        try:
            cost = float(cost)
            cost = cost * 100
            cost = int(cost)
            cost = cost/100
            cost = str(cost)
            break
        except:
            print("please enter an number")
            continue

        
    #get quantity with error handling
    while True:
        quantity = input("Please enter the quantity of the product: ")
        print("")
        try:
            quantity = int (quantity)
            break
        
        except:
            print("please enter an integer\n")
            continue

    
#generate shoe object and update both shoe_list and inventory.txt
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    with open ("inventory.txt","w+") as g:

            g.write(f"country,code,product,cost,quantity\n")
            for element in shoe_list:  
                shoe_string = element.__str__()
                g.write(f"{shoe_string}\n")
            
    return
        
def view_all(shoe_list):
    
    '''
    This function generates a table of all the shoes and prints to terminal
    '''
    from tabulate import tabulate

    #initialise list called table
    table = []
    # for each shoe in shoe_list, add a new list to table. table will then be in the correct format for tabulate
    for shoe in shoe_list:
        table.append([f"Country: {shoe.country}",f"Code: {shoe.code}" ,f"Product: {shoe.product}" ,f"Cost: R{shoe.cost}", f"Quantity: {shoe.quantity} units in stock"])
    #print the table
    print (tabulate(table))
    return

def re_stock(shoe_list):

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    #initialise the lowest number and the lowest shoe as the first shoe in the list
    lowest_num = int(shoe_list[0].quantity)
    lowest_shoe = shoe_list[0]
    #loop through list to find the shoe with the lowest stock
    for shoe in shoe_list:
        if int(shoe.quantity) < lowest_num:
            lowest_shoe = shoe

    while True:
        #give user the opportunity to add stock with error handling
        restock_num = input(f"""
The shoe lowest in stock is: {lowest_shoe.product}, code {lowest_shoe.code}. Current stock: {lowest_shoe.quantity}. 
Please enter the number of stock you would like to add:
""")
        print("")
        try:
            new_stock = int(lowest_shoe.quantity) + int(restock_num)

            #update inventory.txt
            lowest_shoe.quantity = new_stock
            with open ("inventory.txt","w+") as g:
                g.write(f"country,code,product,cost,quantity\n")
                for shoe in shoe_list:
                    g.write(f"{shoe.__str__()}\n")
            #message confirming update
            print (f"The new stock of shoe {lowest_shoe.product} is {new_stock}. This has been updated.\n\n")
            break
        #if entry is not an integer, display error and return to top of loop
        except:
            print ("Error: Please enter an integer") 
            continue  

def search_shoe(shoe_list):
    
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    while True:
        #initialise found_shoe for case shoe not found
        found_shoe = "1******1"
        #request input from user
        code= input("Please enter the code of the shoe you would like to view or type 'e' to exit:\n")
        #exit if e selected
        if code == 'e':
            return
        #else loop through shoe_list and if code found, assign found_shoe and break loop
        else:
            for shoe in shoe_list:
                if shoe.code == code:
                    found_shoe = shoe
                    break
        #if shoe not found print error message and return to top of while loop
        if found_shoe =="1******1":

            print ("\nShoe not found.\n")
            continue
        
        #if shoe found, print message and give shoe details
        else:
            print("\nShoe found!!\n")
            print (f"Country: {found_shoe.country}",f"Code: {found_shoe.code}" ,f"Product: {found_shoe.product}" ,f"Cost: R{found_shoe.cost}", f"Quantity: {found_shoe.quantity} units in stock\n\n")

def value_per_item(shoe_list):
    

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print ("")
    #for each shoe, calculate total value and print this information to the terminal
    for shoe in shoe_list:
        total_value = float(shoe.cost)*int(shoe.quantity)
        print(f"{shoe.product}, total value = {total_value}")
    print("")
    return

def highest_qty(shoe_list):
    
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    #initialise shoe with highest number as first shoe in list
    highest_num = int(shoe_list[0].quantity)
    highest_shoe = shoe_list[0]
    #loop through to find the highest quantity
    for shoe in shoe_list:
        if int(shoe.quantity) > highest_num:
            highest_shoe = shoe

    #display the result
    print(f"\nThe shoe: {highest_shoe.product} has the highest stock: {highest_shoe.quantity}\n")
    

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

def main():

    
    while True:
        
        #extract shoe_list from inventory.txt. This is now a list of Shoe objects
        shoe_list = read_shoes_data()

        #request input
        menu_choice = input(f"""Please enter a selection from below by typing the number:

        1) add a shoe to list of shoes
        2) display a list of shoes
        3) restock the shoe with the lowest stock number
        4) search for a shoe
        5) display the shoe with the highest quantity
        6) display a list of shoes with the total value of the stock 
        7) exit    
        
        """)

        if menu_choice == "1":
            #give user opportunity to add a shoe
            capture_shoes(shoe_list)

            #display a table of all shoes
        elif menu_choice =="2":
            view_all(shoe_list)

            #give user opportunity to restock the lowest stocked shoe
        elif menu_choice == "3":
            re_stock(shoe_list)
            
            #give the opportunity to search for a shoe
        elif menu_choice == "4":
            search_shoe(shoe_list)

            #display shoe with highest quantity
        elif menu_choice == "5":
            highest_qty(shoe_list)

            #print a list of shoes with their total stock value
        elif menu_choice == "6":
            value_per_item(shoe_list)

            #exit
        elif menu_choice == "7":
            print("You have chosen to exit")
            return
            #error if incorrect input
        else:
            print("I am sorry there was an error. Please enter an integer between 1 and 7.\n")
            continue


main()