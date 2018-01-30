""" Fruitful functions and conditionals """

""" 
    Function name (1): is_in_stock
    Parameters: item(str), quantity(int)
    Return Value: True, false, or None (None Type)

    Description: Write a function that determines whether or not the parameter item is in stock. If so, you also need
    to check that there are enough of that item in stock to fulfill your order (specified by the parameter
    quantity). Return True if these conditions are met, False otherwise. Return None if the item is not
    in the table.
"""
def is_in_stock(item, quantity):
    if item == "avocado":
        if quantity > 0:
            return False
        else:
            return True
    elif item == "toothpaste":
        if quantity <= 5:
            return True
        else:
            return False
    elif item == "popcorn":
        if quantity <= 10:
            return True
        else:
            return False
    elif item == "bottled water":
        if quantity <= 8:
            return True
        else:
            return False
    elif item == "phone charger":
        if quantity <= 1:
            return True
        else:
            return False
    else:
        return None

print(is_in_stock("avocado", 3))
print(is_in_stock("bottled water", 1))
print(is_in_stock("popcorn", 100))
print(is_in_stock("potato chips",5),"\n")


"""
    Function name (2): can_afford
    Parameters: item(str), quantity(int), wallet(int)
    Return Values: True or False or None (None Type)

    Description: Write a function that determines whether or not you can afford the parameter item, given the number
    of that item you would like to buy (specified by parameter quantity), the amount of money you have
    (specified by parameter wallet), and the item’s current price value in the table. You do not need to
    consider whether there are enough of the item in stock for this function. Return True if you can afford
    this item, False otherwise. Return None if the item is not in the table.
"""

def can_afford(item, quantity, wallet):
    if item == "avocado":
        if wallet >= quantity*1:
            return True
        else:
            return False
    elif item == "phone charger":
        if wallet <= quantity*12:
            return False
        else:
            return True
    elif item == "popcorn":
        if wallet >= quantity*1:
            return True
        else:
            return False
    elif item == "toothpaste":
        if wallet >= quantity*2.75:
            return True
        else:
            return False
    elif item == "bottle water":
        if wallet >= quantity*4:
            return True
        else:
            return False
    else:
        return None

print(can_afford("avocado", 500, 5))
print(can_afford("phone charger", 10, 500))
print(can_afford("mouthwash", 1, 20),"\n")


"""
   Function name (3): is_on_sale
    Parameters: item (str)
    Return value: True or False (bool) or None (NoneType)
    Description: Write a function that determines whether or not the parameter item is on sale, according to the list
    price and current price values for the item in the table. You do not need to consider whether the item
    is in stock for this function. Return True if it is on sale, False otherwise. Return None if the item is not
    in the table.

"""
def is_on_sale(item):
    if item == "avocado":
        avo_current_price = 1
        avo_list_price = 1.50
        if avo_current_price < avo_list_price:
            return True 
        else:
            return False
    elif item == "toothpaste":
        toothp_current_price = 2.75
        toothp_list_price = 2.75
        if toothp_current_price < toothp_list_price:
            return True 
        else:
            return False
    elif item == "popcorn":
        popcorn_current_price = 1
        popcorn_list_price = 1
        if popcorn_current_price < popcorn_list_price:
            return True 
        else:
            return False
    elif item == "bottled water":
        bw_current_price = 4
        bw_list_price = 5.50
        if bw_current_price < bw_list_price:
            return True 
        else:
            return False
    elif item == "phone charger":
        phch_current_price = 12
        phch_list_price = 15
        if phch_current_price < phch_list_price:
            return True 
        else:
            return False
    else:
        return None

print(is_on_sale("phone charger"))
print(is_on_sale("toothpaste"))
print(is_on_sale("chocolate bar"),"\n")


"""    Part 2: Concert Listing  """

""""
    Function name (1): is_single_cheaper
    Parameters: artistName(str)
    Return value: boolean
    Description: Write a function that takes in the name of one of the artists from the chart. Decide whether or not it
    would be cheaper to buy a single ticket, or to get the group ticket price and divide it amongst 10
    people. If it’s cheaper for single tickets, then return True, and if not, then return False. If the artist is not valid,
    return None.
 """
# global variables for the functions below

tswift_single_tickets = 275
tswift_group_tickets = int(3000/10)
adele_single_tickets = 152
adele_group_tickets = int(1500/10)
zbb_single_tickets = 25
zbb_group_tickets = int(200/10)
    
def is_single_cheaper(artistName):
    if artistName == "Taylor Swift":
        if tswift_single_tickets < tswift_group_tickets:
            return True
        else:
            return False
    elif artistName == "Adele":
        if adele_single_tickets < adele_group_tickets:
            return True
        else:
            return False
    elif artistName == "Zac Brown Band":
        if zbb_single_tickets < zbb_group_tickets:
            return True
        else:
            return False
    else:
        return None
print(is_single_cheaper("Taylor Swift"))
print(is_single_cheaper("Chainsmokers"),"\n")

"""
    Function name (2): best_price
    Parameters: artistName(str)
    Return value: representing the best price the user would pay to attend the artist’s concert (int)
    Description: Write a function that takes in the name of one of the artists from the chart. Using the
    is_single_cheaper function, determine whether a single ticket or group ticket would be the cheapest,
    and then return the price of the ticket as an integer. If the group option ends up being the cheapest,
    do not return the full price for the group, but the price once it is divided by 10 people. If the artist is
    not valid, return None.
"""
def best_price(artistName):
    if artistName == "Taylor Swift":
        if is_single_cheaper(artistName) == True:
            return tswift_single_tickets
        else:
            return tswift_group_tickets
    elif artistName == "Adele":
        if is_single_cheaper(artistName) == True:
            return adele_single_tickets
        else:
            return adele_group_tickets
    elif artistName == "Zac Brown Band":
        if is_single_cheaper(artistName) == True:
            return zbb_single_tickets
        else:
            return zbb_group_tickets
    else:
        return None

print(best_price("Taylor Swift"))
print(best_price("Avicii"),"\n")

""" 
    Function name (3): all_three
    Parameters: None
    Return value: representing how much it would cost to attend all three concerts (int)
    Description: Write a function that uses the best_price function to determine the best prices of each
    of the concerts, sums them all up, and returns the total cost.
"""

def all_three():
    print("The best price for the Taylor Swift concert is ", best_price("Taylor Swift"))
    print("The best price for the Adele Concert is ", best_price("Adele"))
    print("The best price for the Zac Brown Band is ", best_price("Zac Brown Band"))
    
    total_cost = best_price("Taylor Swift") + best_price("Adele") + best_price("Zac Brown Band")

    return total_cost

print("The total cost is ", all_three(),"\n")

""""
    Function name (4): cheapest_concert
    Parameters: None
    Return value: representing the name of the artist with the cheapest concert (str)
    Description: Write a function that uses the best_price function to determine the best prices of each
    of the concerts, and then returns the name of the artist with the cheapest concert. You may not
    use any built in Python functions.
"""
def cheapest_concert():
    if best_price("Taylor Swift") < best_price("Adele"):
        return "Taylor Swift has the cheapest tickets"
    if best_price("Adele") < best_price("Zac Brown Band"):
        return "Adele has the cheapest tickets"
    if best_price("Zac Brown Band") < best_price("Taylor Swift"):
        return "Zac Brown Band has the cheapest tickets"

print(cheapest_concert(),"for",best_price("Zac Brown Band"),"dollars","\n")

""" 
    Function name (5): add_two
    Parameters: artist1 (str), artist2 (str)
    Return value: representing the cost to go to both concerts (int)
    Description: Write a function that takes in two artists from the table above, and calculates how much
    it would cost to attend both concerts based on their best prices. Return the total cost.
"""
def add_two(artist1, artist2):
    if artist1 == "Taylor Swift" and artist2 == "Adele":
        cost_concert1 = best_price("Taylor Swift") + best_price("Adele")
        return cost_concert1
    elif artist1 == "Taylor Swift" and artist2 == "Zac Brown Band":
        cost_concert2 = best_price("Taylor Swift") + best_price("Zac Brown Band")
        return cost_concert2
    elif artist1 == "Zac Brown Band" and artist2 == "Adele":
        cost_concert3 = best_price("Zac Brown Band") + best_price("Adele")
        return cost_concert3
    elif artist1 == "Zac Brown Band" and artist2 == "Taylor Swift":
        cost_concert4 = best_price("Zac Brown Band") + best_price("Taylor Swift")
        return cost_concert4
    elif artist1 == "Adele" and artist2 == "Taylor Swift":
        cost_concert5 = best_price("Adele") + best_price("Taylor Swift")
        return cost_concert5 
    elif artist1 == "Adele" and artist2 == "Zac Brown Band":
        cost_concert6 = best_price("Adele") + best_price("Zac Brown Band")
        return cost_concert6
print(add_two("Zac Brown Band","Adele"),"\n")

"""
    Function name (6): can_afford_concerts
    Parameters: money(int)
    Return value: None
    Description: Write a function that will be using some of the functions that you have written above.
    Based on the money passed in, determine if you can go to all three concerts, only two concerts, or
    only the cheapest concert. If you can go to all three, print “I can go to all three!”, if you can only go
    to two of any combination, (Taylor Swift and Adele, Adele and Zac Brown Band, etc), then print “I
    can only go to two!”, and if you can only go to one concert, print a statement in the format of “I can
    only go to one.”. If there is not enough money for any of those options, then print out a statement
    that says “Dang it, I can’t go to any concert.”. Note: It’s very important that you print out your answer
    EXACTLY as it’s formatted in the instructions.
"""
def can_afford_concerts(money):
    if money < 20:
        return "Dang. I can't go to any concert"
    elif money >= 20 and money < 150:
        return "I can only go to one concert."
    elif money >= 150 and money < 275:
        return "I can go to any of the two concerts."
    else:
        return "I can choose to go to any of the three concerts."

print(can_afford_concerts(5))
print(can_afford_concerts(24))
print(can_afford_concerts(220))
print(can_afford_concerts(355),"\n")

""" Part 3: Miscellaneous """

"""" 
    Function name: what_can_you_do
    Parameters: age(int)
    Return value: None
    Description: Write a function that takes in the age of the user and prints out all the activities they are
    able to do based on the table below. If they can’t do any of those activities, print out “Sorry, you’re
    not old enough for any of these”.
"""

def what_can_you_do (age):
    if age < 18:
        return "Sorry, you're not old enough for any of these"
    elif age >= 18 or age < 21:
        return "You can vote."
    elif age >= 21 or  age < 65:
        return "You can vote and drink."
    else:
        return "You can vote, drink, and retire"

print(what_can_you_do(5))
print(what_can_you_do(68),"\n")

"""" Function name: pass_or_fail
    Parameters: current_grade (int), final_weight (float), final_score (int)
    Return value: final letter grade A, B, C, D, or F (str)
    Description: Write a function that will take your current grade in a class, the weight of the final exam
    as a decimal between 0 and 1, and the score you got on the final exam to determine what letter grade
    you’ll receive using the following formula:
    final_grade = current_grade ∗ (1 − final_weight) + final_score ∗ final_weight
    Use the following ranges for letter grades:
    • A: 90-100
    • B: 80-89.9999
    • C: 70-79.9999
    • D: 60-69.9999
    • F: 0-59.9999
"""

def pass_or_fail(current_grade, final_weight, final_score):
    float(final_weight)
    final_grade = current_grade * (1 - final_weight) + final_score * final_weight
    print(final_grade)
    if final_grade >= 90.0:
        return "A"
    elif final_grade < 90.0 and final_grade >= 80:
        return "B"
    elif final_grade < 80.0 and final_grade >= 70:
        return "C"
    elif final_grade < 70.0 and final_grade >= 60:
        return "D"
    else:
        return "F"
    
print(pass_or_fail(90, .15, 75))
print(pass_or_fail(60, .3, 100),"\n")