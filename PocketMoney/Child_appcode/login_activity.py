from Otp_generator import Otp_generator
from signup_Activity import signup

class login:
    def __init__(self):
        self.sigup_obj=signup()
        
        
    def check_isregistered(self,email):
        self.__clientemail=email
        try:
            self._readFile=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Child_appcode\\My_localChild_DB\\"+self.__clientemail+".json","r")
            self.__ispresent=True
        except:
            self.__ispresent=False
        if self.__ispresent:
            if self.verification():
                return int
        else:
            print("ohnoo! It seems you have not registered yet! ")
            choice=input("Would you like to create one ? (Y/N) :")
            if choice =='y' or choice=='Y':
                if self.sigup_obj.createNewuser():
                    return True
                else:
                    return False
            else:
                return False
            
            
    def verification(self):
        self.otp_gebn_obj=Otp_generator(self.__clientemail)
        print(" We have sent you an otp at your registered Email ")
        otp=self.otp_gebn_obj.send_otp()
        recieved_otp=input(" Enter the otp : ")
        verified=self.otp_gebn_obj.verify_otp(received_otp=recieved_otp,sent_otp=otp)
        if verified:
            return True
        else:
            return False
        
        
    
        
        
            
            
        
        