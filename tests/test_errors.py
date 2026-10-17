try:
    file = open("missing_file.txt", "r")

except FileNotFoundError:
    print("The file could not be found!")
else:
    print("File openned succesifully!")
    file.close()