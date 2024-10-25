import json
from tqdm import tqdm
import time
from parent_to_chid_con import Parent_connector

class dashboard :
    __clientEmail=""
    __Fileref_write=None
    __Fileref_read=None
    
    def __init__(self,email) :
        self.__clientEmail=email
        self.parent_connector_obj=Parent_connector()
        
        
        self.get_client_acc_detail() 
    def check_acc_linking(self):
        self.__Fileref_read=open("My_localParent_DB/"+self.__clientEmail+".json",'r')
        self.client_data=json.load(self.__Fileref_read)
        self.__Fileref_read.close()
        if "account_bal" in self.client_data:
            return True
        else:
            return False    
    def get_client_acc_detail(self):
        while 1:
            if self.check_acc_linking():
                
                self.Moving_to_Dashboard()
                print("entered successfully")
                break
            else:
                self.link_client_bank_acc()
        return
    def link_client_bank_acc(self):
        print("Oops! It seems you have not yet linked your bank account yet!")
        while 1:
            choice=input("Press Y to authorize to link your account : ")
            if choice=='y'or choice=="Y":
                print("Your authorization is acknowledged. Sit tight as we establish a link to your bank account.")
                self.delay(0.1)
                print("yay! , Your bank account has been linked successfully...")
                client_acc_bal=int(input("Enter your account balance here : "))
                self.client_data["account_bal"]=client_acc_bal
                self.__Fileref_write=open("My_localParent_DB/"+self.__clientEmail+".json",'w')
                json.dump(self.client_data,self.__Fileref_write)
                self.__Fileref_write.close()
                return 
            else:
                choice=input("Press any key to authorize again or press E to exit :")
                if choice == 'E' or choice=='e':
                    exit()      
            
    def delay(self,timer): # delay function
        total_iteration=100
        
        progressbar=tqdm(total=total_iteration)
        for i in range(total_iteration):
            time.sleep(timer)
            progressbar.update(1)
        progressbar.close()
    def Moving_to_Dashboard(self):
        self.__Fileref_readandwrite=open("My_localParent_DB/"+self.__clientEmail+".json",'r')
        data=json.load(self.__Fileref_readandwrite)
        if "RefernceID" not in data:
            print("Before proceeding further, please set up your child's app. ")
            print("exit....")
            exit()
        else:            
            while 1:
                print("=======================POCKETMONEY(PARENT APP)=======================")
                print(" MENU ")
                print("1. Setup/Modify auto-transaction \n 2. Get transaction statement \n 3. Get Your Child Spends ")
                choice=int(input("Enter your Choice : "))
                if choice == 1:
                    if "autopayStatus" in data :
                        # modifying timer
                        if data["autopayStatus"]:
                            print("Update your Auto pay Timer ")
                            data['Autopay_Timer']=input("Set your New Timer (at 24hrs format ) : ")
                            data['Transfer_Amount']=input("Please Enter the amount you want to transfer : ")
                            is_successfull=self.parent_connector_obj.setup_timer(data['Autopay_Timer'],data['Transfer_Amount'],self.__clientEmail,data['autopayStatus'])
                            if is_successfull:
                                print("Congrats! Timer and Amount has been updated...")
                                print("Moving to dashboard...")
                                self.__Fileref_write=open("My_localParent_DB/"+self.__clientEmail+".json",'w')
                                json.dump(data,self.__Fileref_write)
                                self.__Fileref_write.close()
                                continue
                        else:
                            print("error occured ")
                            exit()    
                    else:
                        #creating new timer
                        print("Oh it seems you have not yet setup your autopay Timer, Let's Do it now...  ")
                        data['autopayStatus']=False
                        data['Autopay_Timer']=input("Set your New Timer (at 24hrs format ) : ")
                        data['Transfer_Amount']=input("Please Enter the amount you want to transfer : ")
                        is_successfull=self.parent_connector_obj.setup_timer(data['Autopay_Timer'],data['Transfer_Amount'],self.__clientEmail,data['autopayStatus'])
                        if is_successfull:
                            data['autopayStatus']=True
                            print("Congrats! New Timer and Amount has been set...")
                            print("Moving to dashboard...")
                            self.__Fileref_write=open("My_localParent_DB/"+self.__clientEmail+".json",'w')
                            json.dump(data,self.__Fileref_write)
                            self.__Fileref_write.close()
                            continue
                        
                elif choice==2:
                    #get your transaction details
                    pass
                elif choice==3:
                    #get your child spends 
                    pass
                else:
                    exit()  
               
            
        
            
                
        
    
            