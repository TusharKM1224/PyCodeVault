import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

def Email_sender(receiver_emails):

    sender_email = "example.com"
    receiver_email = receiver_emails
    password = "############"
    subject = " Job Opportunity Inquiry"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

   
    body = '''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Job Inquiry</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f7f7f7;
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 600px;
                margin: auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            h1 {
                color: #333;
            }

            p {
                color: #666;
            }

            .cta-button {
                display: inline-block;
                background-color: #007bff;
                color: #fff;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
            }

            .cta-button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Dear Hiring Manager,</h1>
            <p> I am reaching out to you for any opportunity to contribute to your team and learn
                from experienced professionals in the industry.</p>
            <p>Throughout my academic career, I have developed a strong foundation in relevant skills like in technical : python ,java,android framework and non technical : Problem solving , Emotional Intelligence, Adaptability. I am eager to apply my knowledge and skills to real-world projects and make meaningful
                contributions to your organization.</p>
            <p>I have attached my resume for your review. I would be grateful for the opportunity to discuss how my
                background, skills, and enthusiasm align with the needs of your team. Please feel free to reach out to me at
                Ph-7896285206 or via email at tusharmazumder011@gmail.com.</p>
            <p>Thank you for considering my application. I look forward to the possibility of working with you.</p>
            <p>Best regards,<br>Tushar Kanti Mazumder</p>
            <a href="#" class="cta-button">Download Resume</a>
        </div>
    </body>

    </html>





    '''
    message.attach(MIMEText(body, "html"))


    text = message.as_string()

   
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


df=pd.read_csv("Companydetails.csv")
df=df.dropna()

    
company_email=list(df['Email'])
print(company_email)
donelist=[]
count=0

'''
for i in company_email:
    if i!="linkedin":
        print("Sending...")
        Email_sender(i)
        print("Sent!!")
        donelist.append(i)
        company_email.pop()
        count+=1
        print(count)
        print(i)
    else:
        pass




'''

'''excluded_company=["reachus@wipro.com","komal.bathla@hcl.com"]
for i in excluded_company:
    print("Sending...")
    Email_sender(i)
    print("Sent!!")
'''

Email_sender("Admin@sorimtechnologies.com")


