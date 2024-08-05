def addition(number):
    result = sum(number)
    return result



def soustration(number):
    result = number[0]
    for num in number [1:]:
        result -= number
    return result



def multiplication(number):
    result = 1
    for num in number:
        result *= number
    return result



def division(number):
    result = number[0]
    try:
        for num in number[1:] :
            result /= number
    except ZeroDivisionError:
        result =  "error : dividion by zero"
        return result






def get_numbers():
    number_Str = input("enter number space by comma : ")
    number = [float(num) for num in number_Str.split(",")]
    return  number











def operation_Mathetique():

    while True:
        print("\n white operation do you")
        print("1. addiction?")
        print("2. soustraction")
        print("3. division")
        print("4. multiplication")
        print("5. exit")

        choice = input("enter your choice (1-5):")

        if choice == "1":
            number = get_numbers()
            result = addition(number)
            print(f" the somme of numbers is : {result}")
        elif choice == "2":
            number = get_numbers()
            result = soustration(number)
            print(f" the soustration  of numbers is :{result}")
        elif choice == "3":
            number = get_numbers()
            result = multiplication(number)
            print(f" the multiplicatione of numbers is :{result}")
        elif choice == "4":
            number = get_numbers()
            result = division(number)
            print(f" the division of numbers is :{result}")
        elif choice == "5":
            print("exiting the calculator....")
            break
        else:
            print("invalid option please try again ...")





if __name__=="__main__":
    operation_Mathetique()

