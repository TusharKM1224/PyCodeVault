import json
from Otp_generator import Otp_generator
from tqdm import tqdm
import time


class Singin:
    def __init__(self):
        pass
         
    def create_User(self):
        clientName=input("Enter your name : ") # askng client's name
        clientEmail=input("Ente your Valid Email address (verficattion req): ") # asking client's email address
        clientPhoneNo=input("Enter your Contact number : ") # asking client's Phone no.
        clientage=input("Enter your age : ") # asking client's age
        clientcity=input("Enter Your city Name : ") # asking client's city name
        self.new_user_data={"name":clientName,
                       "email":clientEmail,
                       "Phone no":clientPhoneNo,
                       "age":clientage,
                       "city":clientcity
                       } # storing all details in a dictionary
        
        print("Verifying your Email Address .....") # verifying client's email address
        Otpsender=Otp_generator(self.new_user_data["email"]) # creating otp_generator object and passing client's email
        print("We have just sent an otp in register email address \n")
        otp=Otpsender.send_otp() # sending otp to client's email
        recieve_otp=input("Enter the otp : ") # Recieving user recieved otp
        if Otpsender.verify_otp(received_otp=recieve_otp,sent_otp=otp): # otp validation
            print("Email Verified ....")    # verified
        else:
            print("Invalid Otp !! Exiting.....")
            exit()# exit....
        print("Creating your account ....please wait ")
        
        self.delay() # setting delay
        create_user=open("My_localParent_DB/"+self.new_user_data["email"]+".json","w") #creating json file
        json.dump(self.new_user_data,create_user) # storing all details in json file
        
        # checking whether the file has been created successfully or not..
        create_user=open("My_localParent_DB/"+self.new_user_data["email"]+".json","r") # opening the json file in read mode
        data=json.load(create_user)# loading the content of the file in a variable
        create_user.close()
         
        if data: # checking whether content has been writen or not
            print("Congo! Your account has been created ...")
            return True
        else:
            return False
         
        
        
    def get_newClientEmail(self): # sending client's email
        return self.new_user_data["email"]
    def delay(self): #delay method
        total_iteration=100
        progressbar=tqdm(total=total_iteration)
        for i in range(total_iteration):
            time.sleep(0.02)
            progressbar.update(1)
        progressbar.close()
    

#testing area

       
        