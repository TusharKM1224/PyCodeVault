import sys
sys.path.append("E:\\Projects(Python)\\New Projectfiles\\PocketMoney")
from connector import connector

class Child_connector:
    def __init__(self) :
        self.connector_obj=connector()
    def Email_verifier(self,email):
        self._email=email
        response=self.connector_obj._VerifyParentDB(self._email)
        #print(response)
        if response:
            return True
        else:
            return False
    def session_creater(self,child_email,parent_email):
        is_successfull=self.connector_obj.session_controller(child_email,parent_email)
        if is_successfull:
            return True
        else:
            return False
        
        
