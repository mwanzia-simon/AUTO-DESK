try:
    file = open("../main.py", "r")

except FileNotFoundError:
    print("The file could not be found!")
else:
    print("File openned succesifully!")
    file.close()