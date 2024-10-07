numbers = ["1,2,3,4,5,6,7,8,9,10"]
users = input("If you want to delete the numbers? ")

if users == "YES":
    numbers.clear()
elif users == "NO":
    print(numbers)