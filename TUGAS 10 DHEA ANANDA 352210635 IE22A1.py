list = [123, 456, 789, 321]
print("List of four three digit numbers:")
for item in list:
    print(item)
number = int(input("Enter a three digit number: "))
if number in list:
    position = list.index(number)
    print(f"The number {number} is found at position {position + 1} in the list.")
else:
    print("It's not in the list")