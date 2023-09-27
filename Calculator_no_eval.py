while True:
    ip = input("Enter your expression (e.g. 2 * 3 or Q for Quit): ")
    exp = ip.split()
    if exp[0] == "Q":
        print("Off!")
        break
    elif len(exp) == 3:
        if exp[0].isnumeric() and exp[2].isnumeric():
            if exp[1] == "+":
                x = float(exp[0]) + float(exp[2])
                print(f'Answer = {x}')
            elif exp[1] == "-":
                x = float(exp[0]) - float(exp[2])
                print(f'Answer = {x}')
            elif exp[1] == "/":
                x = float(exp[0]) / float(exp[2])
                print(f'Answer = {x}')
            elif exp[1] == "*":
                x = float(exp[0]) * float(exp[2])
                print(f'Answer = {x}')
            else:
                print("Invalid! Please retry!")
        else:
            print("Invalid! Please retry!")
    else:
        print("Invalid! Please retry!")