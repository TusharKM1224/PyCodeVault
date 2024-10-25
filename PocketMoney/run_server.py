import json
import time
from datetime import datetime
import csv
from connector import connector


class run_server:
    def __init__(self):
        self.connector_obj=connector()
    def run_server(self):
            while True:
                current_time=time.strftime("%H:%M:%S") 
                current_time=current_time.replace(":","_")
                print(current_time.replace(":","_"))
            
                count=0
                try:
                    self.open_server_routine=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(current_time)+".json",'r')
                    is_present=True
                    print(is_present)
                except:
                    is_present=False
                print(is_present)
                
                if is_present:
                    try:
                        routine_data=json.load(self.open_server_routine)
                    except:
                        print("Error occured")
                        exit()
                    no_keys=len(routine_data)
                    if no_keys>1:
                        for referenceID in routine_data:
                            count+=1
                            print
                            if count>1:
                                try:
                                    self.open_server_records=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\"+str(referenceID)+".json","r")
                                    is_ref_present=True
                                except:
                                    is_ref_present=False
                                if is_ref_present:
                                    referenceID_data=json.load(self.open_server_records)
                                    parentEmail=referenceID_data["ParentEmail"]
                                    childEmail=referenceID_data["ChildEmail"]
                                    print(parentEmail,childEmail)
                                    child_data,parent_data=self.connector_obj.get_user_data(parentEmail,childEmail)
                                    print(child_data)
                                    print(parent_data)
                                    parent_acc_bal=parent_data['account_bal']
                                    parent_acc_bal-=int(routine_data[referenceID])
                                    print(parent_acc_bal)
                                    parent_data['account_bal']=parent_acc_bal
                                    child_data["Wallet"]=int(routine_data[referenceID])
                                    
                                    is_successfull=self.connector_obj.make_transaction(child_data,parent_data,childEmail,parentEmail)
                                    if is_successfull:
                                        current_date=datetime.now().date()
                                        Parent_name=parent_data["name"]
                                        Child_name=child_data["name"]
                                        amount=int(routine_data[referenceID])
                                        transaction_time=current_time
                                        transaction_row=[current_date,Parent_name,Child_name,amount,transaction_time]
                                        with open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\Transaction_csv\\"+referenceID+".csv",mode='a',newline='') as csvfile:
                                            writer=csv.writer(csvfile)
                                            
                                            writer.writerow(transaction_row)
                                    else:
                                        print('picapoo')
                                        
                                        
                                        
                                    
                                    
                                    
                                else:
                                    print("error")
                            else:
                                print("iiiii")
                    else:
                        print("issue")
                else: 
                    print("error.....")
                time.sleep(1)

server_driver_obj=run_server()
server_driver_obj.run_server()
        