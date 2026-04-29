#list, mutable, ordered, have duplicate

sample_list = [1, "hello", True, 0.1, "hello"]

#append, adding a new item at the end of the list
sample_list.append("I am now just been added")
print(sample_list)

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
print(sample_tuple)

#count
index = sample_tuple.index(2)

print(index)

#functions
print(sum(sample_tuple))
