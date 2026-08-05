List1 = [1,2,4,5]
print("Orignal List")
print(List1)
print("")
#Adding in list
print("Adding 3 to 2nd index")
List1.insert(2,3)
print(List1)
print("")

#Appending
print("Appending List [6,7,8,9,10]")
List1.append([6,7,8,9,10])
print(List1)
print("")

#Extending
print("Extending with 'Mudit Dua' ")
List2 = ['Mudit Dua']
List1.extend(List2)
print(List1)
print("")

#Deleting
print("Deleting value 4")
List1.remove(4)
print(List1)