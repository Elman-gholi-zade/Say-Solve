# تابع بخش مخفی
def hide() :
    print()
    print("Hello   !!!")






while True :
    # بخش انتخاب عملیات
    num1, operations, num2 = input("Enter :  ").split()

    num1 = float(num1)
    num2 = float(num2)

    print( )

    #  عملیات جمع
    
    if operations == "+" :
        print( )
        result = num1 + num2            
        print("-------------------------")
        print(f"{num1} + {num2} = {result} ")
        print("-------------------------")
        print()
        print()


    # بخش عملیات تفریق
    elif operations == "-" :

        result = num1 - num2
        print("-------------------------")
        print(f"{num1} - {num2} = {result} ")
        print("-------------------------")
        print(" ")
        print(" ")


    # بخش عملیات ضرب
    elif operations == "*" :

        result = num1 * num2
        print("-------------------------")
        print(f"{num1} * {num2} = {result} ")
        print("-------------------------")
        print(" ")
        print(" ")

    # بخش عملیات تقسیم
    elif operations == "/" :

        result = num1 / num2
        print("-------------------------")
        print(f"{num1} / {num2} = {result} ")
        print("-------------------------")
        print(" ")
        print(" ")


    # بخش مخفی
    elif operations == 1 :
        hide()



    # خروج
    elif operations == "e" :
        break




    else :
        print()
        print("Warring ! ")
        print()



        