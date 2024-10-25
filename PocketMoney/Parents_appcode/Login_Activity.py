from Otp_generator import Otp_generator
from Sign_Activity import Singin


class Login:
    __clientemail_id=""
    _isPresent=True  
    set_flag=True
    DB_file=None
    __request_code=int
    def __init__(self) :
        pass   
    def check_isRegistered(self,email):
        self._isPresent=True
        
        self.__clientemail_id=email
       
        try:
         # if the below statment does not finds any file it will create an exception and this exception we change the boolean values  
            self.DB_file=open("My_localParent_DB/"+self.__clientemail_id+".json","r") # checking is local_db whether client is registered or not
        except:
            self._isPresent=False
        
        if self._isPresent: # if client is already having an account than
            otp_response=self.verification() 
            if otp_response:
                return self.__request_code 
            else:
                return False             
        else: # else if client don't  have any account
           print(" Ohnoo ! , It seems you don't have an account \n ")
           create_acc=input("Would you like to create a account ?? (y/n) : ") # creating prompt to ask whether client wants to create a new account
           if create_acc=='y'or create_acc=='Y':
               Singin_obj=Singin()# calling sign activity to register the new client
               is_created=Singin_obj.create_User()
               print(is_created)
               if is_created: # if the register is successfull than return true ; else return false
                    self.set_flag= True
                    return self.set_flag
               else:
                    self.set_flag= False           
           else:
                self.set_flag=False
           return self.set_flag
        
           
                                    
    def verification(self):
        Otpsender=Otp_generator(self.__clientemail_id) # creating object of class otp_generator
        print("We have just sent an otp in register email address \n")
        otp=Otpsender.send_otp() #sending otp to client's email
        recieve_otp=input("Enter the otp : ") # asking user to give the provided input
        if Otpsender.verify_otp(received_otp=recieve_otp,sent_otp=otp):# checking otp validation
           
            return True 
              
        else:
            
            return False
            
    
        
               
          
            
 #Testing area below           


            

            
            
            
            
    
        
        
        
         
    
  
    
    

    
  
        


