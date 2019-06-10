# groceries.py

#from pprint import pprint

#products is a list type. to determine the type of functions we can use with a list type,
#look at the course repository --> notes

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


products_count = len(products) #to find the len() function. look in course repository ->notes. Use this instead of hard coded number in case number of products change

#Step 1: Print the header of the desired goal.
#create function products_count and use len() function to count # of items in list

print("--------------")
print("THERE ARE "+ str(products_count) + " PRODUCTS:")
#another option for line above using string interpolation: print(f"THERE ARE {products_count} PRODUCTS:")
print("--------------")
# pprint(products)


#Step 2.b: Sort our list using the sorted function. See 2.a below 2.b. We did 2.a first

def sort_by_name(any_product): ##we need to define this function so that sorted knows what to do. 
                                ##important to note, this function alone doesn't do much. It needs us to tell it 
                                #to operate on the products list in order to produce a result that menas something
    return any_product["name"]

    #alternate: start with import operator --> replace sorted_products with sorted_products = sorted(products, key=operator.itemgetter("name"))

sorted_products = sorted(products, key=sort_by_name) #Sorted = Return a new list containing all items from the iterable in ascending order.

#Step 2: Use for loop to create list of each item in products list, with name and price
#helpful to look at each item in the list as a reference. see below:
#
#   "id":1, 
#   "name": "Chocolate Sandwich Cookies", 
#   "department": "snacks", 
#   "aisle": "cookies cakes", 
#   "price": 3.50

#each item is a type dictionary. use course repository -- notes to see functions we can use -- 
## we can use square products to reference attribute name

for p in sorted_products: #p is just used to reference. i.e. for each i in sum i = 1 to 100 
    price_usd = " (${0:.2f})".format(p["price"]) #formats number into a string
    print(" + " + p["name"] + price_usd)
    

#PART 2: DEPARTMENT COUNT

##Step 3: Create unique list of departments

departments = []
for p in products:
    if p["department"] not in departments: #use if statement to find out if it exists
        departments.append(p["department"]) 

#another techinque is to convert a list to a set, which will auto only include unqiue
#unique_departments = list(set(departments))


department_count = len(departments) #to find the len() function. look in course repository ->notes. Use this instead of hard coded number in case number of products change


print("--------------")
print("THERE ARE "+ str(department_count) + " DEPARTMENTS:")
print("--------------")

departments.sort() #sort list

for d in departments:
    department_count_func = [p for p in products if p["department"] == d] #the first p references what to return. So this means return p for each p in products if department = d
    department_count = len(department_count_func)
    if department_count > 1:
        label = "products"
    else:
        label = "product"
    
    print(d.title()+ " (" + str(department_count) + " " + label + ")") #print in title case

#Step 4: Count list of each department using filtering




#DESIRED GOAL
#--------------
#THERE ARE 20 PRODUCTS:
#--------------
# + All-Seasons Salt ($4.99)
# + Chocolate Fudge Layer Cake ($18.50)
# + Chocolate Sandwich Cookies ($3.50)
# + Cut Russet Potatoes Steam N' Mash ($4.25)
# + Dry Nose Oil ($21.99)
# + Fresh Scent Dishwasher Cleaner ($4.99)
# + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
# + Green Chile Anytime Sauce ($7.99)
# + Light Strawberry Blueberry Yogurt ($6.50)
# + Mint Chocolate Flavored Syrup ($4.50)
# + Overnight Diapers Size 6 ($25.50)
# + Peach Mango Juice ($1.99)
# + Pizza For One Suprema Frozen Pizza ($12.50)
# + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
# + Pure Coconut Water With Orange ($3.50)
# + Rendered Duck Fat ($9.99)
# + Robust Golden Unsweetened Oolong Tea ($2.49)
# + Saline Nasal Mist ($16.00)
# + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
# + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)


## PROFESSOR FINAL NOTES

### groceries.py
##
##from pprint import pprint
##
##def to_usd(my_price):
##    return "${0:,.2f}".format(my_price)
##
##products = [
##    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
##    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
##    #{"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
##    #{"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
##    #{"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
##    #{"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
##    #{"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
##    #{"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
##    #{"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
##    #{"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
##    #{"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
##    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
##    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
##    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
##    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
##    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
##    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
##    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
##    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
##    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
##] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
##
###pprint(products)
##
##products_count = len(products)
##
###print("THERE ARE 20 PRODUCTS:")
###> "one string" + "another string"
###print("THERE ARE " + str(products_count) + " PRODUCTS:")
##
##print("--------------")
##print(f"THERE ARE {products_count} PRODUCTS:")
##print("--------------")
##
### todo: sort the products
##
##for item in products:
##    #print(type(item))
##    #print(p["name"])
##    #print(item["name"])
##    #n = item["name"]
##    #price = item["price"]
##    #print(f"{item['name']} ... {item['price']}")
##
##    price_usd = to_usd(item['price'])
##    print(f"{item['name']} ... {price_usd}")