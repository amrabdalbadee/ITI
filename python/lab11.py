def main_window():
    print("1- Widthraw \n")
    print("2- Balance Inquiry \n")
    print("3- Fast cash \n")
    print("4- quit \n")
def fast_cash():
    print("1- 500$ \n")
    print("2- 1000$ \n")
    print("3- 5000$ \n")
    print("4- 10000$ \n")
    print("5- 50000$ \n")

pin = 1234
balance = 25000
flag = 1
print("Welcome to our bank \n")
x = int(input("Enter your 4-Digit pin number: "))
while (flag == 1):
    if x == pin:
        main_window()
        y = int(input("choose process: "))
        match y:
            case 1:
                w = int(input("Enter withdraw amount (multiple of 100): "))
                if (w % 100 == 0):
                    if balance >= w:
                        print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR \n")
                        balance -= w
                        print("Remaining Balance: ",balance,"$")
                        #main_window()
                    else:
                        print("invalid withdraw! \n")
                        #main_window()
                else:
                    print("invalid Amount! \n")
                    #main_window()
            case 2:
                print("your balance is ",balance,"$ \n")
                #main_window()
            case 3:
                fast_cash()
                l = int(input("Enter Amount: "))
                match l:
                    case 1 : ## if can be written before :
                        if (balance - 500 >= 0):
                            balance -= 500
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            print("Remaining Balance is: ",balance,"$")
                        else:
                            print("invalid withdrawl")
                    case 2:
                        if (balance - 1000 >= 0):
                            balance -= 1000
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            print("Remaining Balance is: ", balance, "$")
                        else:
                            print("invalid withdrawl")

                    case 3:
                        if (balance - 5000 >= 0):
                            balance -= 5000
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            print("Remaining Balance is: ", balance, "$")
                        else:
                            print("invalid withdrawl")
                    case 4:
                        if (balance - 10000 >= 0):
                            balance -= 10000
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            print("Remaining Balance is: ", balance, "$")
                        else:
                            print("invalid withdrawl")
                    case 5:
                        if (balance - 50000 >= 0):
                            balance -= 50000
                            print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                            print("Remaining Balance is: ", balance, "$")
                        else:
                            print("invalid withdrawl")
            case 4:
                print("BYE \n")
                flag = 0
            case _:
                print("invalid option, please enter a number again \n")
                #main_window()


    else:
        print("invalid pin \n")
        flag = 0

