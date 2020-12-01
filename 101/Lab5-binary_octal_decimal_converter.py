#   Ishaan Lahoti
#  ​CSCI 101 – Section G
#   Python Lab 5
#   References: None
#   Time: 30 minutes


def converter():
    option = 0
    convstring = ""
    output = ""
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Enter an option:")
    print("1. Binary-Decimal Conversion")
    print("2. Decimal-Binary Conversion")
    print("3. Octal-Decimal Conversion")
    print("4. Decimal-Octal Conversion")
    print("5. Quit")
    try:
        option = int(input("OPTION> "))
    except ValueError:
        print("ERROR: Please choose from [1-5]")
        return "ERROR"
    if option == 1:
        convstring = input("BINARY-STR> ")
        try:
            temp = int(convstring)
        except ValueError:
            print(f"ERROR: Input {convstring} is NOT a binary number.")
            return "ERROR"
        i = len(convstring) - 1
        deci = 0
        for x in convstring:
            if 1 >= int(x) >= 0:
                deci += int(x) * pow(2, i)
                i -= 1
            else:
                print(f"ERROR: Input {convstring} is NOT a binary number.")
                return "ERROR"
        output = str(deci)
    elif option == 2:
        convstring = input("DECIMAL-STR> ")
        binary = ""
        try:
            temp = int(convstring)
        except ValueError:
            print(f"ERROR: Input {convstring} is NOT a decimal number.")
            return "ERROR"
        tempnum = int(convstring)
        while tempnum != 0:
            binary += str(tempnum % 2)
            tempnum = int(tempnum / 2)
        output = binary[::-1]
    elif option == 3:
        convstring = input("OCTAL-STR> ")
        try:
            temp = int(convstring)
        except ValueError:
            print(f"ERROR: Input {convstring} is NOT an octal number.")
            return "ERROR"
        i = len(convstring) - 1
        deci = 0
        for x in convstring:
            if 8 > int(x) >= 0:
                deci += int(x) * pow(8, i)
                i -= 1
            else:
                print(f"ERROR: Input {convstring} is NOT an octal number.")
                return "ERROR"
        output = str(deci)
    elif option == 4:
        convstring = input("DECIMAL-STR> ")
        try:
            temp = int(convstring)
        except ValueError:
            print(f"ERROR: Input {convstring} is NOT a decimal number.")
            return "ERROR"
        octal = ""
        tempnum = int(convstring)
        while tempnum != 0:
            octal += str(tempnum % 8)
            tempnum = int(tempnum / 8)
        output = octal[::-1]
    elif option == 5:
        return "Goodbye!"
    else:
        print("ERROR: Please choose from [1-5]")
        return "ERROR"
    return output


print("Welcome to the Binary-Octal-Decimal Converter")
keepgoing = True
while keepgoing:
    result = converter()
    print(f"OUTPUT {result}")
    if result == "Goodbye!":
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        break
    print("Would you like to continue (y/n)?")
    cont = input("CONTINUE> ")
    if cont[0] == "N" or cont[0] == "n":
        keepgoing = False
        print("OUTPUT Goodbye!")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    else:
        continue





