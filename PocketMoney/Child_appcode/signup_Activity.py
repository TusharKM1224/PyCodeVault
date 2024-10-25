import json
from Otp_generator import Otp_generator
from child_to_parent_con import Child_connector





class signup:
    def __init__(self) :
        self.C_to_p_obj=Child_connector()
        pass
    def createNewuser(self):
        print("Welcome to Pocket Money Child app ...")
        print(" Let's us create your first account , Please the details accordingly!")
        Name=input("Enter your Name : ")
        phnone=input("Enter your phone number : ")
        email=input("Enter your Email ID (verfication req): ")
        GaurdianEmail=input("Enter Your gaurdian's Email(Verification req) : ") 
        age=input("Enter your age : ")
        city=input("Enter your City : ")
        is_successfull=self.C_to_p_obj.Email_verifier(GaurdianEmail)
        if is_successfull:
            print("Verification Successfull")
        else:
            print("Verification failed")
            
        
       
             
        response=self.verification(email)
        if response:
            print("Email verified")
            child_data={"name":Name,
                        "PhoneNo":phnone,
                        "email":email,
                        "GaurdianEmail":GaurdianEmail,
                        "age":age,
                        "city":city}
            
            file_write_json=open("My_localChild_DB/"+child_data["email"]+".json","w")
            json.dump(child_data,file_write_json)
            file_write_json.close()
            file_read_json=open("My_localChild_DB/"+child_data["email"]+".json","r")
            data=json.load(file_read_json)
            
            if data != None:
                return True
            else:
                return False
        else:
            print("Email not verified !")
    def verification(self,email):
        self.otp_gebn_obj=Otp_generator(email)
        print(" We have sent you an otp at your registered Email ")
        otp=self.otp_gebn_obj.send_otp()
        recieved_otp=input(" Enter the otp : ")
        verified=self.otp_gebn_obj.verify_otp(received_otp=recieved_otp,sent_otp=otp)
        if verified:
            return True
        else:
            return False

        
     
        
                