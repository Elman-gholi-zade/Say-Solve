import json




def load_history() :
    '''این تابع فایل تاریخچه
    را لود می کند'''


    try :
        with open("history.json", "r", encoding="utf-8") as file :
            history = json.load(file)

    except FileNotFoundError :
        print("❗Error :  History file not found ❗")
        return
    
    else :
        return history
    


def save_history(history) :
    '''این تابع تاریخچه جدید 
    را به فایل تاریخچه اضافه می کند'''

    with open("history.json", "w", encoding="utf-8") as file :
        json.dump(history, file, ensure_ascii=False, indent=4)




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
        
    


    # Structuring
    def structuring(self, operation) :
        '''این تابع بخش های مختلف یک عملیات را
        ساختاردهی می کند'''

        new_history = {
            "num1" : self.num1,
            "num2" : self.num2,
            "operation" : operation,
            "result" : self.result
            }
        
        return new_history

    

    # Ready to show
    def show_result(self, history) :
        '''این تابع داده های که تابع ساختاردهی 
        مرتب کرده بود را برای نمایش آماده می کند'''

        finally_result = f"|> {history["num1"]} {history["operation"]} {history["num2"]} = {history["result"]}"
        return finally_result



    # Add and save new history
    def add_to_history(self, structured_operation) :
        '''.این تابع ابتدا فایل تاریخچه را لود کرده
         سپس عملیات انجام و ساختاردهی شده را
         که از ورودی می گیرد, در فایل تاریخچه
         دخیره می کند'''
        

        # load history file
        history = load_history()

        # Add and save
        history.append(structured_operation)

        save_history(history)


        



 


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
    print(calc.show_result(calc.structuring(operation)))
    print("----------------------------------")


    # save in history
    calc.add_to_history(calc.structuring(operation))



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