print("(a) List operations")
aboutme = [['Mudit'], ['00129802024'], ['VIPS']]
print("Nested List:", aboutme)
print("Name:", aboutme[0][0])
print("Length:", len(aboutme))

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
print("Concatenation:", l1 + l2)

l3 = [1, 2, 3, 4, 5]
print("1 in list:", 1 in l3)
print("6 not in list:", 6 not in l3)

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Iteration:", end=" ")
for num in l4:
    print(num, end=" ")
print()

print("Indexing:")
for i, num in enumerate(l4):
    print(i, num)

print("First element:", l4[0])
print("Last element:", l4[-1])
print("Slicing l4[1::2]:", l4[1::2])
print("Slicing l4[2:6]:", l4[2:6])

print()
print("(b) List methods")
a = [1, 2, 4, 5]
print("Original list:", a)

a.insert(2, 3)
print("After insert(2, 3):", a)

a.append([6, 7, 8, 9, 10])
print("After append([6, 7, 8, 9, 10]):", a)

a.extend(['Mudit Dua'])
print("After extend(['Mudit Dua']):", a)

a.remove(4)
print("After remove(4):", a)

a.pop()
print("After pop():", a)

del a[0]
print("After del a[0]:", a)