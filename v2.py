


class Calculator :


    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        self.result = 0



    # add two number
    def add(self) :
        self.result = self.num1 + self.num2
        
    

    # subtract two number
    def subtract(self) :
        self.result = self.num1 - self.num2
        
    

    # multiply two number
    def multiply(self) :
        self.result = self.num1 * self.num2
        
    

    # divide to number
    def divide(self) :
        try :
            self.result = self.num1 / self.num2

        except ZeroDivisionError :
            print("❗Error : division by zero.❗")
        
    
    # show result
    def show_result(self, operation) :
        return (f"|>  {self.num1} {operation} {self.num2} = {self.result}")



 


def calculate(operation, num1, num2) :
    '''این تابع عملیات را از ورودی گرفته و 
    سپس آن را به یک رشته از متدهای کلاس ماشین حساب
    تبدیل می کند.
    بعد از تبدیل, متد عملیات را که تبدیل کرده
    بود, صدا زده و در نتیجه نتیجه را نمایش می دهد'''


    # Create Object
    calc = Calculator(num1, num2)

    
    # Changes
    if operation == "+" :
        calc.add()

    elif operation == "-" :
        calc.subtract()

    elif operation == "*" :
        calc.multiply()

    elif operation == "/" :
        calc.divide()

    else :
        print("❗Error : Invalid operation.❗")
        return



    # Show result
    print("----------------------------------")
    print(calc.show_result(operation))
    print("----------------------------------")





# Get inputs
def get_inputs() :

    allowed_operations = ["+", "-", "*", "/"]

    while True :

        operation = input("operation :  ")

        if operation not in allowed_operations :
            print("❗Invalid operation ❗")
            continue


        else :

            try :
                num1 = float(input("num1 :  "))
                num2 = float(input("num2 :  "))

            except ValueError :
                print("❗Inputs must be numbers ❗")
                continue
            
            else :
                return operation, num1, num2
            


# Calculate / Start
def start() :
    op, num1, num2 = get_inputs()
    calculate(op, num1, num2)

while True :
    start()