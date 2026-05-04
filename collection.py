#list, mutable, ordered, have duplicate

sample_list = [1, "hello", True, 0.1, "hello"]

#append, adding a new item at the end of the list
sample_list.append("I am now just been added")

#change a value or item inside of a list
sample_list[1] = "hi"


#remove
# sample_list.pop(2)

#insert
sample_list.insert(2, "Nice")


#clear
sample_list.clear()


#tuple, ordered, immutable, have duplicates
sample_tuple = (10, 2, 2,2, 50, 60)

#count
index = sample_tuple.index(2)


#functions

#dictionary 
# happy - it signifies someone is joyful
# key, value : key-value pairs
# accessed using keys and not by index



# #dictionary methods
# sample_key = sample_dictionary.get("sample_key")

# #getting all the keys in a dictionary
# keys = sample_dictionary.keys()
# # print(f"The keys in your dictioary are: {keys}\n")

# #getting all the values in our dictionary
# values = sample_dictionary.values()
# # print(f"The values in your dictioary are:  {values}\n")

# #getting all items inside of dictionary
# items = sample_dictionary.items()
# print(f"The items in your dictioary are: {items}\n")

# for key, value in items:
#     print(f"{key} : {value}")

#Removing
# del sample_dictionary["value"]
# print(sample_dictionary)

name = "henry"
personal_details = {
    
    "name": "henry",
    "age" : 24,
    "school" : "MCC",
    "graduated" : False
    
}

#adding or updating

#list, square bracket, accesing items using index/numbers which starts from 0

#tuple, immutable, ordered
veggies = ("celery", "okra")


#dictionary curly braces
apple = {"price": 30}


#set
#unordered, no duplicates
grocery_list = {
    
    "fruits": {
        
        "apple" : 20,
        "mango" : 30,
        "papaya" : 50
        
        },
    
    "veggies": ["pechay", "cabbage", "carrots"]
}

fruits = grocery_list["fruits"]["apple"]
veggies = grocery_list["veggies"][0]
print(fruits)