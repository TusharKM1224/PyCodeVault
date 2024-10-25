import json
import csv

from Parents_appcode.Otp_generator import Otp_generator

class server_driver:
    def __init__(self):
       
        pass
    def create_json_data(self,Cemail,Pemail,ref):
        try:
            self.sever_records_read=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\"+ref+".json","r")
            is_present=True
            self.sever_records_read.close()
        except:
            is_present=False
            
        if is_present:
            return False
        else:
            self.server_records_write=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\"+ref+".json","w")
            self.otp_gen_obj=Otp_generator(Pemail)
            print
            otp=self.otp_gen_obj.send_otp()
            recieved_otp=input("Enter the otp sent to your Gaurdian's Mail : ")
            is_successfull=self.otp_gen_obj.verify_otp(received_otp=recieved_otp,sent_otp=otp)
            if is_successfull:
                Sever_data={'ParentEmail':Pemail,'ChildEmail':Cemail,"ref":ref}
                json.dump(Sever_data,self.server_records_write)
                self.create_csv(ref)
                return True
            else:
                print("Server is not responding !! ")
    def create_csv(self,ref):
        column_name=['Date','SendFrom','SendTo','Amount','Time']
        with open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\Transaction_csv\\"+ref+".csv",'w',newline='')as file:
            writer=csv.DictWriter(file,fieldnames=column_name)
            writer.writeheader()
    def create_new_scheduler(self,timer,amount,referenceid):
       is_present=True
       timer=timer.replace(':','_')
       
       try:
           self.openToRead=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(timer)+".json",'r')
       except:
           is_present=False
       if is_present:
           #if timer already exist
            data=json.load(self.openToRead)
            self.openToWrite=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(timer)+".json",'w')
            
            data[referenceid]=amount
            json.dump(data,self.openToWrite)
            self.openToRead.close()
            self.openToWrite.close()
            self.openToRead=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(timer)+".json",'r')
            data=json.load(self.openToRead)
            if referenceid in data:
                return True
            else:
                return False
       else:
           # if timer do not exist 
            self.openToWrite=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(timer)+".json",'w')
            
            data={"garbage":"data",referenceid:amount}
            json.dump(data,self.openToWrite)
            self.openToWrite.close()
            self.openToRead=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(timer)+".json",'r')
            data=json.load(self.openToRead)
            if referenceid in data:
                return True
            else:
                return False     
    def modify_scheduler(self,oldtiimer,newtimer,oldamount,newamount,referenceid):
        oldtiimer=oldtiimer.replace(':','_')
        newtimer=newtimer.replace(':','_')
        print(oldtiimer)
        print(newtimer)
        
        is_present=True
        #remove old timer schedule
        try:
            self.fileopenToReadWrite=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(oldtiimer)+".json",'r')
        except:
            is_present=False
        if is_present:
            data=json.load(self.fileopenToReadWrite)
            if referenceid in data:
                del data[referenceid]
                self.fileopenToReadWrite=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(oldtiimer)+".json",'w')
                json.dump(data,self.fileopenToReadWrite)
                #self.fileopenToReadWrite.close()
            else:
                print("ReferenceId not found")
            # add new timer
            try: 
                self.fileopenToReadWrite=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(newtimer)+".json",'r')
                is_present=True
            except:
                is_present=False
           
            if is_present:
                # means the timer already exist!!
                data=json.load(self.fileopenToReadWrite)
                data[referenceid]=newamount
                self.fileopenToReadWrite=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(newtimer)+".json",'w')
                json.dump(data,self.fileopenToReadWrite)
                self.fileopenToReadWrite.close()
                self.fileopentoread=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(newtimer)+".json",'r')
                data=json.load(self.fileopentoread)
                if referenceid in data:
                    return True
                else:
                    return False
            else:
                self.fileopenToReadWrite=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(newtimer)+".json",'w')
                data={"garbage":"data",referenceid:newamount}
                json.dump(data,self.fileopenToReadWrite)
                self.fileopenToReadWrite.close()
                self.fileopen=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\My_localServer_DB\\server_schedule\\"+str(newtimer)+".json",'r')
                data=json.load(self.fileopen)
                if referenceid in data:
                    return True
                else:
                    return False
                
        else:
            print("old timer not found ")
            return False

    
                    
                    
                










                

                
                
            
        
               
      
        
        
        
            
            
        
        
        
            
            
        
            
            
             
            
       
        
        