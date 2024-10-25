import random
import string
import json
from Server_driver import server_driver


class connector :
    def __init__(self):
        pass
    def _VerifyParentDB(self,email):
        try:
            self.parent_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+email+".json","r")
            __ispresent=True
            self.parent_db.close()
        except:
            __ispresent=False
        
        #print(__ispresent)
        if __ispresent:
            
            return True
        else:
            return False
    def session_controller(self,child_email,parent_email):
        self.server_obj=server_driver()
        while 1:
            ref=self.reference_ID_creator()
            server_response=self.server_obj.create_json_data(child_email,parent_email,ref)
            if server_response:
                if self.setting_refID_toDB(child_email,parent_email,ref):
                    return True
                else:
                    return False
                break
            else:
                print("passing")
                pass
        
            
    def reference_ID_creator(self):
        alpha_numeric_letters=string.ascii_lowercase+string.digits
        res=[]
        ref=""
        for x in range(20):
            res.append(random.choice(alpha_numeric_letters))
        ref=''.join(res)
        return str(ref)
    def setting_refID_toDB(self, Cemail,Pemail,ref):
        self.parent_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+Pemail+".json",'r')
        data=json.load(self.parent_db)
        self.parent_db.close()
        data['RefernceID']=ref
        self.parent_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+Pemail+".json",'w')
        json.dump(data,self.parent_db)
        self.parent_db.close()
        ##########################################
        self.child_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Child_appcode\\My_localChild_DB\\"+Cemail+".json",'r')
        data=json.load(self.child_db)
        self.child_db.close()
        self.child_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Child_appcode\\My_localChild_DB\\"+Cemail+".json",'w')
        data['RefernceID']=ref
        json.dump(data,self.child_db)
        self.child_db.close()
        
        self.child_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Child_appcode\\My_localChild_DB\\"+Cemail+".json",'r')
        self.parent_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+Pemail+".json",'r') 
        childdata=json.load(self.child_db)
        parentdata=json.load(self.parent_db)
        
        if 'RefernceID' in childdata and 'RefernceID' in parentdata:
            return True
        else:
            return False
    def setup_autopayscheduler(self,time,referenceid,amount,autopaystatus,Pemail):
        self.server_obj=server_driver()
        if autopaystatus:
            #autopay is on!!
            self.parent_dbfile=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+Pemail+".json",'r')
            data=json.load(self.parent_dbfile)
            is_successfull=self.server_obj.modify_scheduler(data['Autopay_Timer'],time,data['Transfer_Amount'],amount,referenceid)
            if is_successfull:
                return True
            else:
                return False
        else:
            #autopay in off!!
            is_successfull=self.server_obj.create_new_scheduler(time,amount,referenceid)
            if is_successfull:
                return True
            else:
                return False
                
    def get_user_data(self,pemail,cemail):
        try:
            self.open_parent_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+pemail+".json",'r')
            self.open_child_db=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Child_appcode\\My_localChild_DB\\"+cemail+".json","r")
            is_present=True
        except:
            is_present=False
        if is_present:
            child_data=json.load(self.open_child_db)
            parent_data=json.load(self.open_parent_db)
            return child_data,parent_data
        else:
            return None
    def make_transaction(self,child_data,parent_data,cemail,pemail):
        print(child_data)
        print(parent_data)
        self.open_child_db_to_write=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Child_appcode\\My_localChild_DB\\"+cemail+".json","w")
        self.open_parent_db_to_write=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+pemail+".json",'w')
        json.dump(child_data,self.open_child_db_to_write)
        json.dump(parent_data,self.open_parent_db_to_write)
        self.open_parent_db_to_write.close()
        self.open_child_db_to_write.close()
        self.open_parent_db_to_read=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Parents_appcode\\My_localParent_DB\\"+pemail+".json",'r')
        self.open_child_db_to_read=open("E:\\Projects(Python)\\New Projectfiles\\PocketMoney\\Child_appcode\\My_localChild_DB\\"+cemail+".json","r")
        child_data=json.load(self.open_child_db_to_read)
        parent_data=json.load(self.open_parent_db_to_read)
        print(child_data)
        print(parent_data)
        if child_data !=None and parent_data !=None:
            return True
        else:
            return False
        
        
        
        
            
            
        
               
        
        
            

             
           



       