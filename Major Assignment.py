n1 = float(input("Please input a number: "))
n2 = float(input("Please input a number: "))
n3 = float(input("Please input a number: "))
n4 = float(input("Please input a number: "))
n5 = float(input("Please input a number: "))
n6 = float(input("Please input a number: "))
n7 = float(input("Please input a number: "))
n8 = float(input("Please input a number: "))
n9 = float(input("Please input a number: "))
n10 = float(input("Please input a number: "))
lyst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

mean = sum(lyst) / len(lyst)
print("The mean of this list is " + str(mean))

lyst.sort()
m1 = lyst[len(lyst) // 2]
m2 = lyst[len(lyst) // 2 - 1]
median = (m1 + m2) / 2
print("The median of this list is " + str(median))

frequency = {}
for i in lyst:
    frequency.setdefault(i, 0)
    frequency[i] += 1
frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("The mode of this list is " + str(mode))
