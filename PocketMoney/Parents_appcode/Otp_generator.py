import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


class Otp_generator:
    __clientEmail=""
    _recievedotp=""
    
    def __init__(self,email):
        self.__clientEmail=email
        
    def send_otp(self):
        otp=self.otp_generation()
        sender_email ="pocketmoneyv5@gmail.com"
        reciever_email=self.__clientEmail
        subject="One Time Password"
        body="The Otp is "+otp
        
        message=MIMEMultipart()
        message["From"] =sender_email
        message["To"] =reciever_email
        message["Subject"]=subject
        
        
        message.attach(MIMEText(body,"plain"))
        
        #smtpserver
        smtp_server ="smtp.gmail.com"
        smtp_port=587
        smtp_username ="acmpg2024@gmail.com"
        smtp_pwd="kmbf hdsx dvrm yiwk" 
        
        #connect to SMTP server
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(smtp_username,smtp_pwd)
        
        #send Email
        server.sendmail(sender_email,reciever_email,message.as_string())
        
        #close the server
        server.quit()
        print("Mail sent successfully ! ") 
        return otp
        
    def verify_otp(self,received_otp,sent_otp):
        
        if received_otp==sent_otp:
            return True
        else :
            return False    
        
        
    def otp_generation(self):
        otp=random.randint(1000,10000)
        return str(otp)
       
        
       
        
        
   
   
   
   
   
   
   
    
#testing area below

        
        
        
        



