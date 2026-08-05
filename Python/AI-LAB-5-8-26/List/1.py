#Nested Lists

aboutme = [
    ['Mudit'], #name
    ["00129802024"], #roll Number 
    ['VIPS'] #My College
]

# List Concatenation
List1 = [1,3,5,7]
List2 = [2,4,6,8]
List3 = List1 + List2
print(List3)
print(" ")

#MemberShip
List4 = [1,2,3,4,5]
if 1 in List4:
    print("Found")
if 6 not in List4:
    print("Doesnt Exist")
print(" ")

#Iteration
List5 = [1,2,3,4,5,6,7,8,9,10]
print(" ")
print("List Iteration")
[print(num, end=" ") for num in List5]
print ("")
#Indexing 
print("Indexing")
for index, num in enumerate(List5):
    print(index , num)

print ("")
#Slicing
print("Slicing")
print(List5[1::2])

