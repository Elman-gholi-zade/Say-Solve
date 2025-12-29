


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
        self.result = self.num1 / self.num2
        
    
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
    object = Calculator(num1, num2)

    
    # Changes
    if operation == "+" :
        object.add()

    elif operation == "-" :
        object.subtract()

    elif operation == "*" :
        object.multiply()

    elif operation == "/" :
        object.divide()



    # Show result
    print("----------------------------------")
    print(object.show_result(operation))
    print("----------------------------------")





# Get inputs
num1 = float(input("num1 :  "))
num2 = float(input("num2 :  "))
operation = input("operation :  ")



# Calculate / Start
calculate(operation, num1, num2)