list = [5, 7, 3 ,"Abhi", 67, 23,"Reha", 21, 8, 5, 3]
print(type(list))
print(list)


#lists are not immutable they are mutable! we can modify it without creating/printing the new list
#in other words it will not return the new list it just modify the same existing list
list.remove("Abhi") #Remove the word from the list
list.remove("Reha")
# print(list.count(5)) #cout the words the only one thing these method can take only one arguments inside it
# list.sort(); #Sorting the list Ascending order mean small to largest
# list.pop()   #Remove the last element from the list
# list.insert(0, "Shreya") #Used for insert the element in list - take two argument the first is position and another one is value
# list.append("Rahu") #adding the value in the end of list
# list.reverse() #reverse the list elements
# list.clear() #remove or clear all the elements from the list
list.extend([5, 4, 77, 43, 2]) #Extend the list with these more values
print(list)
print(list.index(77)) #find the index of value in list
