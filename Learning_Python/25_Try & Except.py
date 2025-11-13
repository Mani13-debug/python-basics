try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Value Entered")

print("")
print("")


try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Value Entered")