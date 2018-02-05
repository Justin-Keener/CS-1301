"""
    Function Name: remove_duplicates
    Parameters: aList
    Return value: The modified list.
    Description: Write a function that takes in a list. Return a new list that has removed all of
    the duplicates from the first list. The modified list should have the unique elements in
    the same order as the original list. If there are no duplicates, then return the original list.
    If the original list is empty return an empty list.
"""
def remove_duplicates(oldList):
    new_list = []
    for item in oldList:
        if item not in new_list:
            new_list.append(item)
    print(new_list)
remove_duplicates([10,"cat",5.2,"hello", "cat", "Hello",0])
"""
    Function Name: common_elements
    Parameters: list1 and list2
    Return value: True if the two lists have at least one common element. False if they are
    different.
    Description: Write a function that takes in two lists. If the two lists have at least one
    common element, return True. If the two lists are completely different, return False. You
    can assume that none of the lists will be empty.
"""
def common_elements(list1,list2):
    for item_in_list1 in list1:
        if item_in_list1 in list2: # Compares items in list 1 with items in list 2
            return True
        elif item_in_list1 not in list2:
            return False
    
print(common_elements([1,2,3,4],[6,7,8,9,10]))
print(common_elements(["goodbye",88,True,"yellow"],["orange",False,"red","goodbye",0]))

"""
    Function Name: flatten_list
    Parameters: list1
    Return value: A list that contains the elements of the list passed in and the elements of
    the nested lists.
    Description: Write a function that takes a list and returns a new list. If any of the
    elements in the list are also lists, the returned list should have the individual elements of
    that nested list. You can assume that the nested list will not contain any elements that
    are also lists. If the original list is empty you can return an empty list.
    Hint: Try using the type() function.
"""

def flatten_list(list1):
    newlist = []
    for items in list1:
        if type(items) != list: 
            newlist.append(items)
        else:
            for i in items:
                newlist.append(i)
    return newlist

print(flatten_list([8, 9, [0, True, "ok"], False]))

"""
    Function Name: make_odd_even
    Parameters: list1
    Return Value: The modified list.
    Description: Write a function that takes a list and returns a new list. You can assume
    that the list passed in will only contain integers. If the elements of the list are even, add
    them to the new list. If the elements of the list are odd, make them even by adding 1
    and then add that new number to the list. If the original list is empty you can return an
    empty list. You may assume the integer 0 is even.
"""

def make_odd_even(oldList):
    newList = []
    for items in oldList:
        if items % 2 == 0:
            newList.append(items) 
        elif items % 2 == 1:
            new_items = items + 1
            newList.append(new_items)
    return newList
print(make_odd_even([2,43,23,34,20,88,7]))

"""
    Function Name: unique_lists
    Parameters: list1, list2
    Return Value: The modified list1.
    Description: Write a function that takes in two lists. If an element in list2 is not in list1,
    append that element to list1. If an element in list2 is already in list1, remove that
    element from list1. Return the updated list1.
"""

def unique_lists(list1,list2):
    for items in list2:
        if items not in list1:
            list1.append(items)
        elif items in list1:
            list1.remove(items)
    return list1

print(unique_lists([6,"butterfly","waffle",19],[True,"shirt",8,"waffle",6,"computer"]))
print(unique_lists(["water", "sand", "beach", 14],[False, "earring", "smile", 17]))

"""
    Function Name: process_string
    Parameters: aStr, aNum (int)
    Return value: a list of ints

    Description: Write a function that accepts a string of characters, filters out all non-
    number characters from the string, and returns a list of the numbers in the string that

    are a factor of aNum. NOTE: You can also ignore all zeroes (0) in the string, as 0 is not
    a factor of any number.
"""
def process_string(aStr,aNum):
    new_string = ""
    newList = []
    for items in aStr:
        if items in "123456789":
            new_string += items     # if there are numbers, then place them into new string
    for items in new_string:
        if aNum % int(items) == 0:  # converts the string numbers into integers to determine if they're a factor of aNum
            newList.append(int(items)) # places those numbers into a list
    return newList

print(process_string("jahfig234thdajg0gri9t2832488radga", 12))

"""
    Function name: find_family
    Parameters: names_list (a list of strings); surname (string)
    Return value: a list containing the first names of all the people that have surname AND
    do not have middle names.
    Description: Write a function that takes in a list of names and a specific surname to
    search for. Return a list of the UNIQUE first names of all the names in names_list that
    have surname AND do not have middle names. NOTE: Each name could have 0 or
    more middle names, but all names have a first and last name.
"""

def find_family(names_list,surname):
    newList = []
    for names in names_list:
        if surname in names:
            count = 0
            for element in names:
                if element == " ":
                    count += 1
                    if count <= 1:
                        newList.append(names)
            if count > 1:
                newList.remove(names)

    print(newList)

find_family(["Josh Washington", "Chris Hartley", "Sam Giddings", "Beth Washington", "Jessica Riley", "Ashley Brown",
"Hannah Washington", "Mike Munroe", "Matt Taylor", "Emily Davis"], "Washington")

find_family(["Esteban Julio Ricardo Montoya de la Rosa Ramirez", "Lina Ramirez", "Sebastian Alejandro Ramirez",
"Zack Martin", "Cody Martin", "Jonathan Romero", "Daniela Ramirez"],"Ramirez")

find_family(["John Roberts", "Anthony Kennedy", "Clarence Thomas", "Ruth Bader Ginsburg", 
"Stephen Breyer", "Samuel Alito", "Sonia Sotomayor", "Elena Kagan", "Neil Gorsuch"],"O'Connor")

"""
    Function name: add_next
    Parameters: aList (a list of integers)
    Return value: None
    Description: Overwrite each element in aList with its value added with the value of the
    next element in the list. The last element on the list (or if there is only one element in the
    list) should be added to itself.
"""

def add_next(aList):
    for position in range(len(aList)):
        if position < (len(aList)-1):
            aList[position] = aList[position] + aList[position + 1]
        else:
            aList[position] = aList[position] * 2
    print(aList)

things = [2,5,9]
add_next(things)