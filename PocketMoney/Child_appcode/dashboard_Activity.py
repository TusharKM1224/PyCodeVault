import json
from tqdm import tqdm
import time
from child_to_parent_con import Child_connector


class dashboard :
    __child_email=""
    def __init__(self) :
        self.__childConnector_obj=Child_connector()
        pass
    def get_clientEmail(self,email):
        self.__child_email=email
        self.create_child_wallet()
    def create_child_wallet(self):
        print("creating your wallet ...")
        self.__openfileToRead=open("My_localChild_DB/"+self.__child_email+".json","r")
        data=json.load(self.__openfileToRead)
        self.__openfileToRead.close()
        self.__openfileToWrite=open("My_localChild_DB/"+self.__child_email+".json","w")
        data["Wallet"]=0.0
        json.dump(data,self.__openfileToWrite)
        self.__openfileToWrite.close()
        self.delay(0.1)
        while 1:
            choice=input("To connect parent app press Y : ")
            if choice=='y' or choice=="Y":
                print("Please wait while we connect your parent app...")
                self.create_session_with_parent()
                self.delay(0.1)
                break
            else:
                choice=input("Press any key to reauthenticate or E to exit :")
                if choice=='e'or choice=='E':
                    exit()
                else:
                    pass   
        
    def create_session_with_parent(self):
        self.__openfileToRead=open("My_localChild_DB/"+self.__child_email+".json","r")
        data=json.load(self.__openfileToRead)
        is_successfull=self.__childConnector_obj.session_creater(data['email'],data['GaurdianEmail'])
        if is_successfull:
            return True
        else:
            return False
        
        
    def delay(self,timer): # delay function
        total_iteration=100
        
        progressbar=tqdm(total=total_iteration)
        for i in range(total_iteration):
            time.sleep(timer)
            progressbar.update(1)
        progressbar.close()
       
        
        
        


#testing area below


        