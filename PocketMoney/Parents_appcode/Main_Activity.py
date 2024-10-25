from Login_Activity import Login
from Dashboard_Activity import dashboard
from Sign_Activity import Singin
from tqdm import tqdm
import time


class Main_activity:
    __login_obj=None
    __sign_obj=None
    _clientEmail=None
    def __init__(self) :
        self.__login_obj=Login()
        self.__sign_obj=Singin()
        print("************POCKET MONEY*************")
        print("Select an Option : \n")
        print("1. Login \n2. Signup\t ")# setting choice for client to choose one of the option
        choice=int(input("Enter the your choice : "))
        if choice==1:  # 1. login
            print(" Login : ")
            self._clientEmail=input("Enter your Registered Email : ") # asking client to provide thier email address
            self.__login_obj=Login() # creating object of login activity
            is_successsfull=self.__login_obj.check_isRegistered(self._clientEmail)# getting a bool value from login activity
            print(is_successsfull)
            
               
            if is_successsfull or is_successsfull == int: # checking if the login was successfull or not
                print("Congrats! Redirecting to dashboard ...")
                self.delay() # creating a delay
                if is_successsfull==int:
                    self.move_to_dash(is_successsfull)
                else:
                    self.move_to_dash(is_successsfull)
                    
            else:
                print("Oops! ,Something went Wrong!") # if the login is unsuccessfull
                
                
        else: # 2. signup
            print(" Create account : Kindly fill the details accordingly !")
            # creating object of singup activity
            is_sign_successfull=self.__sign_obj.create_User() # creating new client's account
            if is_sign_successfull: # checking whether the creating has been created successfully or not
                   print(" Redirecting to dashboard ...")
                   self.delay() # creating a delay
                   self.move_to_dash(is_sign_successfull)# redirecting to dashboard activity
            else:
                    print("Oops! ,Something went Wrong!") # if the signin is unsuccessfull
                
                
            
    
    
    def delay(self): # delay function
        total_iteration=100
        
        progressbar=tqdm(total=total_iteration)
        for i in range(total_iteration):
            time.sleep(0.02)
            progressbar.update(1)
        progressbar.close()
    def move_to_dash(self,request_code):# method to redirect to dashboard
    
        if request_code!=int:
            
            print("Login")
            self._clientEmail=input("Enter your Registered Email : ") 
            is_successsfull=self.__login_obj.check_isRegistered(self._clientEmail)# getting a bool value from login activity   
            if is_successsfull: # checking if the login was successfull or not
                    print("Congrats! Redirecting to dashboard ...")
                    self.delay() # creating a delay
            else:
                    print("Oops! ,Something went Wrong!") # if the login is unsuccessfull
        else:
            pass
        dash=dashboard(email=self._clientEmail) #creating object of dashboard activity and passing the client email
         

main_obj=Main_activity() #calling main_activity
        
        
        