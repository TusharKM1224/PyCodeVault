from signup_Activity import signup
from login_activity import login
from dashboard_Activity import dashboard
from tqdm import tqdm
import time
class Main_activity:
    def __init__(self) :
        self.__login_obj=login()
        self.__signup_obj=signup()
        self.__dash_obj=dashboard()
        print("=================ChildPocketMoney=================")
        print("Choose an option: \n 1 login \n 2. Signup \n")
        choice=int(input("Enter the your choice : "))
        if choice == 1:
            self.login()
        else:
            self.signup()
    def login(self):
        self.__clientEmail=input("Enter your Registered email : ")
        is_successfull=self.__login_obj.check_isregistered(self.__clientEmail)
        if is_successfull == True or is_successfull==int :
            if is_successfull ==int :
                print("Redirecting you to DashBoard...")
                self.delay(0.01)
                self.move_to_dash(is_successfull)
            else:
                print(" Moving to back Login ....")
                self.delay(0.1)
                self.move_to_dash(is_successfull)
        else:
            print("Something went Worng!")
    def signup(self):
        is_successfull=self.__signup_obj.createNewuser()
        if is_successfull:
            print(" Moving to back Login ....")
            self.delay(0.1)
            self.move_to_dash(is_successfull)
        else:
            print("something went wrong!")
    def move_to_dash(self,response):
        if response!=int:
            print("Welcome back to login ")
            email=input("Enter your registered email")
            respone=self.__login_obj.check_isregistered(email)
            if response:
                print("Redirecting you to DashBoard...")
                self.delay(0.01)
                self.__dash_obj.get_clientEmail(email)
            else:
                print("Something went Wrong!!")
        else:
            self.__dash_obj.get_clientEmail(self.__clientEmail)
        
    def delay(self,timer): # delay function
        total_iteration=100
        
        progressbar=tqdm(total=total_iteration)
        for i in range(total_iteration):
            time.sleep(timer)
            progressbar.update(1)
        progressbar.close()
       
        
            
        
        
        



obj=Main_activity()

    
    
        