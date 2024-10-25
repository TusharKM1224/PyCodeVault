from bs4 import BeautifulSoup
import requests
import time

'''with open("website/index.html","r") as html_file:
    content=html_file.read()
    soup =BeautifulSoup(content,'lxml')
    h1_tag = soup.findAll('h1') # find() finds the first occurence of the tag in the file , so to find all occurence of the tag in the  file you need to use findall()..
    for tags in h1_tag:
        print(tags.text) # Remember .text is not mentioned as prediction , but still you can use it for getting only the content of the tags..'''


print("Put some skill that you are not familiar with ")
unfamiliar_skill=input(">")
print("Filtering out  "+unfamiliar_skill)
def find_jobs():
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation= ").text

    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")

    for index,job in enumerate(jobs):
        job_published_date=job.find('span',class_="sim-posted").span.text
        if 'few' in job_published_date:
            company_name=job.find('h3',class_="joblist-comp-name").text.replace(" ","")
            skills=job.find('span',class_="srp-skills").text
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f"post/{index}.txt",'w') as fn:
                    
                    fn.write("Company Name : "+company_name.strip()+"\n")
                    fn.write("Skill req:  "+skills.strip()+"\n")
                    fn.write("More Info: "+more_info+"\n")
                print(f'File Saved : {index}.txt')
                    
if __name__ =='__main__':
    while True:
        find_jobs()
        time_wait=10
        print("Waiting"+str(time_wait)+" minutes...")
        time.sleep(time_wait*60)
        
       
        
        
    

       
            

    
    
    
 