while True:
    print("Welcome to the Pattern Generator and Number Analyzer.. ")
    print("1.Generator Pattern")
    print("2.Analyzer a Range of Numbers")
    print("3.Exit")
    print()
    num = int(input("Enter the Your choise:"))

    match num:
        case 1:
            sub=int(input("Enter the of rows for the pattern:"))

            for i in range(1,sub+1):
                for j in range(i):
                    print("*",end=" ")
                print()
        case 2:
            num1 = int(input("Enter the Strat of range:"))
            num2 = int(input("Enter the End of range:"))
            total=0

            for i in range(num1,num2+1):
                if i%2==0:
                    print("Even Number:",i)
                else:
                    print("Odd Number:",i)
                
                total +=i
            print(f"Sum of all number form {num1} to {num2} is:",total)

        case 3:
            print("Exiting the program.Goodbye!")
            break
        case _:
            print("Invalid Choise.. Please Enter the 1,2,3")