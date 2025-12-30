import json


    



class Calculator :


    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        self.result = 0



    # add two number
    def add(self) :
        '''عملیات جمع'''

        self.result = self.num1 + self.num2
        
    

    # subtract two number
    def subtract(self) :
        '''عملیات تفریق'''

        self.result = self.num1 - self.num2
        
    

    # multiply two number
    def multiply(self) :
        '''عملیات ضرب'''

        self.result = self.num1 * self.num2
        
    

    # divide to number
    def divide(self) :
        '''عملیات تقسیم'''

        try :
            self.result = self.num1 / self.num2

        except ZeroDivisionError :
            print("❗Error : division by zero.❗")
        
    

    # Ready to show
    def show_result(self, history) :
        '''این تابع داده های که تابع ساختاردهی 
        مرتب کرده بود را برای نمایش آماده می کند'''

        finally_result = f"|> {history["num1"]} {history["operation"]} {history["num2"]} = {history["result"]}"
        return finally_result









class HistoryManager(Calculator) :
  
       
    # Load History File
    def load_history() :
        '''این تابع فایل تاریخچه
        را لود می کند'''


        try :
            with open("history.json", "r", encoding="utf-8") as file :
                history = json.load(file)

        except FileNotFoundError :
            print("❗Error :  History file not found ❗")
            return []
        
        except json.decoder.JSONDecodeError :
            print("❗Error :  History file not found ❗")
            return []    
        
        else :
            return history

    

    # Save History File
    def save_history(history) :
        '''این تابع تاریخچه جدید 
        را به فایل تاریخچه اضافه می کند'''

        with open("history.json", "w", encoding="utf-8") as file :
            json.dump(history, file, ensure_ascii=False, indent=4)



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



    # Add and save new history
    def add_to_history(self, structured_operation) :
        '''.این تابع ابتدا فایل تاریخچه را لود کرده
         سپس عملیات انجام و ساختاردهی شده را
         که از ورودی می گیرد, در فایل تاریخچه
         دخیره می کند'''
        

        # load history file
        history = HistoryManager.load_history()

        # Add and save
        history.append(structured_operation)

        HistoryManager.save_history(history)








def connections(operation, num1, num2) :
    '''این تابع عملیات را از ورودی
    گرفته و اگر داخل دیکشنری عملیات ها باشد,
    متد مربوطه را صدا می زند'''

    # Create Objects
    calc = Calculator(num1, num2)

    history = HistoryManager(num1, num2)


    # Allowed operation dict
    operations = {
        "+" : calc.add,
        "-" : calc.subtract,
        "*" : calc.multiply,
        "/" : calc.divide
    }
    

    
    if operation in operation :
        operations[operation]()
        
    else :
        print("❗Error : Invalid operation.❗")
        return



    # Show result
    print("----------------------------------")
    print(calc.show_result(history.structuring(operation)))
    print("----------------------------------")


    # save in history
    history.add_to_history(history.structuring(operation))



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
    connections(op, num1, num2)


while True :
    start()