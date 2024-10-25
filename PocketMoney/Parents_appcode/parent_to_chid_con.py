import sys
import json
sys.path.append("E:\\Projects(Python)\\New Projectfiles\\PocketMoney")
from connector import connector


class Parent_connector:
    def __init__(self):
        self.connector_obj=connector()
        pass
    def setup_timer(self,Time,amount,Pemail,autopaysatus):
        self.openFile=open("My_localParent_DB/"+Pemail+".json",'r')
        data=json.load(self.openFile);
        is_successfull=self.connector_obj.setup_autopayscheduler(Time,data['RefernceID'],amount,autopaysatus,Pemail)
        if is_successfull:
            return True
        else:
            return False
        
        
        
  