def calc():
    #cont = True
    while True:
        print("What would you like to do: -, +, *, ^, /?")
        sign = input()
        if sign != '-':
                if sign != '+':
                        if sign != '*':
                                if sign != '^':
                                        if sign != '/':
                                                print("That is an invalid response!")
                                                continue
        print("What 2 numbers would you like to use?")
        print("Number 1: ")
        num = input()
        if num.isdigit() == False:
            print("That is an invalid response!")
            continue
        print("Number 2: ")
        numm = input()
        if numm.isdigit() == False:
            print("That is an invalid response!")
            continue
        num = int(num)
        numm = int(numm)
        if sign == '-':
                suban = num - numm
                print(str(num) + '-' + str(numm) + '=' + str(suban))
        elif sign == '+':
                addan = num + numm
                print(str(num) + '+' + str(numm) + '=' + str(addan))
        elif sign == '*':
                mulan = num * numm
                print(str(num) + '*' + str(numm) + '=' + str(mulan))
        elif sign == '^':
                expan = num ** numm
                print(str(num) + '^' + str(numm) + '=' + str(expan))
        elif sign == '/':
                expan = num / numm
                print(str(num) + '/' + str(numm) + '=' + str(expan))
        else:
                continue
        print("Do you want to continue: yes or no?")
        again = input()
        if again.lower() == 'yes':
                continue
        elif again.lower() == 'no':
                cont = False
                break
        else:
                print("That is an invalid response!")
                cont = False
                break



calc()
quit()
