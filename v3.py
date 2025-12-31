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
       self.__history = self.__load_history()    # Load History File
        


    # History Section Meno
    def history_meno(self) :
        '''منوی بخش تاریخچه'''

        print("\n\n==== History Meno =====================")
        print("  1. Show All \n  2. Show Last \n  3. Delete All \n")
        history_meno = input(" >>>  ")


        if history_meno == "1" :
            self.__show_all_history()



    # Automatic saving new record in history
    def auto_save_history(self, operation, num1, num2, result) :
        '''این متد با کنار هم گذاشتن
        چندین متد, ورودی های یک عملیات را 
        به صورت خودکار در فایل تاریخچه ذخیره
        می کند'''

        self.__add_to_history(self.__build_record(operation, num1, num2, result))



    # Load History File
    def __load_history(self) :
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
    def __save_history(self) :
        '''این تابع تاریخچه جدید 
        را به فایل تاریخچه اضافه می کند'''

        with open("history.json", "w", encoding="utf-8") as file :
            json.dump(self.__history, file, ensure_ascii=False, indent=4)



    # Structuring
    def __build_record(self, operation, num1, num2, result) :
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
    def __add_to_history(self, record) :
        '''.این تابع ابتدا فایل تاریخچه را لود کرده
         سپس عملیات انجام و ساختاردهی شده را
         که از ورودی می گیرد, در فایل تاریخچه
         دخیره می کند'''
        
        # Add and save
        self.__history.append(record)

        self.__save_history()






    # Show all records in history
    def __show_all_history(self) :
        '''همه عملیات داخل تاریخچه را شماره بندی کرده
         می دهد
        |به متد |فرمت بندی برای نمایش 
        می دهد تا برای نمایش آماده کند و در
        نتیجه آن را نمایش می دهد'''

        print("\n\n======================================================================")
        print("============================ History =================================\n")
        for index, record in enumerate (self.__history, start=1) :
            print("\n", self.display_formatting(index, record))

        print("======================================================================\n\n")

    

    # Formatting history ot show
    def display_formatting(self, index, record) :
        '''باز کردن تاریخچه و فرمت بندی و همچنین
        شماره بندی'''

        return f"{index}|> {record['num1']} {record['operation']} {record['num2']} = {record['result']}"





      








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



    # Show result
    print("----------------------------------")
    # print(calc.show_result(record))
    print("----------------------------------")


    # save in history
    history.auto_save_history(operation, num1, num2, calc.result)







# =============================
# ======== Min Meno ===========
# =============================
def min_meno() :
    '''منو اصلی'''

    print("\n\n\n======================= Say & Solve ====================\n")

    while True :
        print("| 1. Calculator \n| 2. History \n| 3. Exit \n")
        user_choose = input("| >>>  ")

        if user_choose == "1" :
            op, num1, num2 = get_inputs()
            connections(op, num1, num2)

        elif user_choose == "2" :
            HistoryManager().history_meno()
        
        elif user_choose == "3" :
            break





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
min_meno()