import json


    


# ================================
# ===== Calculator Object ========
# ================================
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
            return
        
    

    # Ready to show
    def show_result(self, record) :
        '''این تابع داده های که تابع ساختاردهی 
        مرتب کرده بود را برای نمایش آماده می کند'''

        finally_result = f"|> {record["num1"]} {record["operation"]} {record["num2"]} = {record["result"]}"
        return finally_result








# =============================
# ===== History Object ========
# =============================
class HistoryManager :
  
    def __init__(self):
        pass
        


    # Load History File
    def load_history(self) :
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
    def save_history(self, history) :
        '''این تابع تاریخچه جدید 
        را به فایل تاریخچه اضافه می کند'''

        with open("history.json", "w", encoding="utf-8") as file :
            json.dump(history, file, ensure_ascii=False, indent=4)



    # Structuring
    def build_record(self, operation, num1, num2, result) :
        '''این تابع بخش های مختلف یک عملیات را
        ساختاردهی می کند'''

        new_history = {
            "num1" : num1,
            "num2" : num2,
            "operation" : operation,
            "result" : result
            }
        
        return new_history



    # Add and save new history
    def add_to_history(self, record) :
        '''.این تابع ابتدا فایل تاریخچه را لود کرده
         سپس عملیات انجام و ساختاردهی شده را
         که از ورودی می گیرد, در فایل تاریخچه
         دخیره می کند'''
        

        # load history file
        history = self.load_history()

        # Add and save
        history.append(record)

        self.save_history(history)







# =========================
# ====== Connections ======
# =========================
def connections(operation, num1, num2) :
    '''این تابع عملیات را از ورودی
    گرفته و اگر داخل دیکشنری عملیات ها باشد,
    متد مربوطه را صدا می زند'''

    # Create Objects
    calc = Calculator(num1, num2)

    history = HistoryManager()


    # Allowed operation dict
    operations = {
        "+" : calc.add,
        "-" : calc.subtract,
        "*" : calc.multiply,
        "/" : calc.divide
    }
    

    
    if operation not in operations :
        print("❗Error : Invalid operation.❗")
        return
        
    operations[operation]()

    record = history.build_record(operation, num1, num2, calc.result)


    # Show result
    print("----------------------------------")
    print(calc.show_result(record))
    print("----------------------------------")


    # save in history
    history.add_to_history(record)







# =============================
# ======= Get Inputs ==========
# =============================
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











# ========================
# ======== Run ===========
# ========================
while True :
    op, num1, num2 = get_inputs()
    connections(op, num1, num2)