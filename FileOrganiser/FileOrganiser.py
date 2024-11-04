import os
import shutil
import json
import time
import sys
class FileOrganiser :
    
    # check response of the User , whether to Organise the current Directory or other Directory
    def __init__(self,userResponse) :
        self.Default_Schema="DefaultNamingSchema.json"
        self.CustomSchema="CustomNamingSchema.json"
        self.CustomFolderkey="CustomParentFolder"
        self.DefaultFolderkey="ParentFolder"
        self.loading_animation(50,"Please wait , Getting things Ready for you!!")
        # to organise in the current directory
        if userResponse=="y" or userResponse=="Y":
            #checking whether this program already aranged
            already_organised=self.check_already_organised()
            #print(already_organised)
            
            if not already_organised:
                # if not organised then create one
                parentFolderName=input('''\nPlease provide me with a folder name where I can organise your files,\n
                Else if you want to use default name then Press \'n\' : ''')
                if parentFolderName !="n" and  parentFolderName !="N":
                    # User's choice for Parent Folder name
                    # if user created a Custom name
                    CustomFoldername=self.create_Update_dictionary(parentFolderName+"/",self.CustomFolderkey)
                    self.loading_animation(20)
                    
                    #print(CustomFoldername)
                    if not CustomFoldername:
                        print(f"Unable to create custom parent folder name :{parentFolderName}")
                        
                    else:
                        print(f"Custom Parent Folder name :{CustomFoldername[self.CustomFolderkey]} created...")
                        # calling Organised method with Custom Naming Schema
                        self.Organise_file(CustomFoldername)
                        
                else:
                    # Setting Default Name Schema
                    defaultNameSchema=self.create_Update_dictionary()
                    #calling Organised method with Default Naming Schema
                    self.Organise_file(defaultNameSchema)
            else:
                # of already organised 
                print("It seems you have already used our service please wait")
                self.loading_animation(35,"Getting Info : ")
                #print(already_organised)
                # calling Organised method with already created Naming Schema
                self.Organise_file(already_organised)
        else:
            # to organise in other directory
            print("Organise other Directory")
    def loading_animation(self,t=50,statement="Loading"):
        loadingAnim="|/-\\|"
        for i in range(t):
            time.sleep(0.1)
            sys.stdout.write( "\r"+statement+loadingAnim[i%len(loadingAnim)])
            sys.stdout.flush()
    def separate_Files_Folders(self,listOfallItems):
        listOfFiles=[]
        listOfFolders=[]
        for item in listOfallItems:
            if os.path.isfile(item):
                listOfFiles.append(item)
            elif os.path.isdir(item):
                listOfFolders.append(item)
            else:
                continue
        return listOfFolders,listOfFiles
    def get_file_extension(self,listOfFiles):
        allFileExtension=set()
        for file in listOfFiles:
           allFileExtension.add(os.path.splitext(file)[1])#
        
        return allFileExtension
    def create_filestructure(self,extensions,followednamingSchema):
        folderStructure={}
        for ext in extensions:
            for name in followednamingSchema:
                if ext==name:
                    folderStructure[ext]=followednamingSchema[name]
        
        return folderStructure
    def UserCustomize(self,FileExtension,oldnamingSchema):
        newToNamingSchema=[ ext for ext in FileExtension if ext not in oldnamingSchema]
        counter=1
        Custom=False
        userchoice1=input("Do you want to see all the Default Name of the folders ? (y/n):")
        if userchoice1 =='y' or userchoice1 =='Y':
            for key in oldnamingSchema:
                print(f"For File Extention {key} : {oldnamingSchema[key]}")        
            userchoice2=input("Would like to Change the Default Folder Name (y/n): ")
            if userchoice2 =="y" or userchoice2 =="Y":
                
                noOfCustomization=int(input("Enter the number of Files You want to Customize : "))
                for i in oldnamingSchema:
                    print(f"Available keys : {i}")
                print(" Follow the above list of file extension as key to customize(i.e if you want change for Python file to other name , then your key would be \'.py\' )")
                while noOfCustomization>0:
                    keyname=input(f"Enter the {counter} key : ")
                    if keyname ==self.CustomFolderkey or keyname == self.DefaultFolderkey:
                        print("Warning: You cannot Change Parent Folder name....")
                        
                    elif keyname not in oldnamingSchema:
                        print(f"Entered key i.e {keyname} does not exists")
                    else:
                        customfoldername=input(f"Enter the Folder name for {keyname} : ")
                        flag=self.renaming_folder(oldnamingSchema[keyname],customfoldername,oldnamingSchema)
                        if flag:
                            print("Folder renamed Successfully ..")
                        
                        oldnamingSchema[keyname]=customfoldername
                        
                        noOfCustomization-=1
                        counter+=1
                Custom=True
                
            else:
                print("Fine, using Default Naming Schema ")
                
                
        else:
            print("Fine, using Default Naming Schema ")
            
        
        if len(newToNamingSchema)!=0:
            print(f"oh! it seems there are some {len(newToNamingSchema)} new unknown files")
            print("Please suggest some folder name for them :")
            for item in newToNamingSchema:
                newfoldername=input(f"Enter New Folder name for {item} : ")
                oldnamingSchema[item]=newfoldername
            print(" Thank you for your customization , for future organisation this Custom Naming Schema will be followed ! ")
            Custom=True
            
            self.loading_animation(20,"Updating the Naming Schema : ")
            return oldnamingSchema, Custom
        else:
            return oldnamingSchema, Custom
        
    def renaming_folder(self,source,destination,Schema):
        if self.CustomFolderkey in Schema:
            parentFolder=Schema[self.CustomFolderkey]
            #filename=self.CustomSchema
        else:
            parentFolder=Schema[self.DefaultFolderkey]
            #filename=self.Default_Schema
            
        
        if os.path.isdir(parentFolder+source):
            os.rename(parentFolder+source,parentFolder+destination)
            return True
        else:
            return False
        
        
        
            
        
        
        
       
            
        
                
                
        
    
    
    
    def Organise_file(self,followedNamingScheme):
        #print(followedNamingScheme)
        # first check all files present
        os.system("cls")
        listOfAllItems=os.listdir()
        if self.CustomSchema in listOfAllItems and "FileOrganiser.exe" in listOfAllItems:
            listOfAllItems.remove(self.CustomSchema)
            listOfAllItems.remove("FileOrganiser.exe")
           # print("1")
        elif self.Default_Schema in listOfAllItems and "FileOrganiser.exe" in listOfAllItems:
            listOfAllItems.remove(self.Default_Schema)
            listOfAllItems.remove("FileOrganiser.exe")
           # print("2")
        
        
        #print(listOfAllItems)
            
        
        #separate files and folders
        listOfFolders,listOfFiles=self.separate_Files_Folders(listOfAllItems)
        # get all extensions of the files
        FileExtension=self.get_file_extension(listOfFiles)
        # setting user customization
        followedNamingScheme ,flag=self.UserCustomize(FileExtension,followedNamingScheme)
        if flag :
            if self.CustomFolderkey not in followedNamingScheme:
                followedNamingScheme[self.CustomFolderkey]=followedNamingScheme.pop("ParentFolder")
                
                    
                os.remove(self.Default_Schema)
                with open(self.CustomSchema,"w") as j:
                    json.dump(followedNamingScheme,j,indent=4)
            else:
                os.remove(self.CustomSchema)
                with open(self.CustomSchema,"w") as j:
                    json.dump(followedNamingScheme,j,indent=4)
                
                
        print("Creating folder structure")
        self.loading_animation(10,"Creating : ")            
        # create a file structure
        folderStructure=self.create_filestructure(FileExtension,followedNamingScheme)
        # checking whether the Naming Schema is custom or default
        if self.CustomFolderkey in followedNamingScheme:
            parentFolder=followedNamingScheme[self.CustomFolderkey]
            filename=self.CustomSchema
        else:
            parentFolder=followedNamingScheme[self.DefaultFolderkey]
            filename=self.Default_Schema
        
        #print(parentFolder)
        #print(filename)
        
        
        # check whether user did
        # check whether the parentfolder is there or not in the Directory        
        if parentFolder.split("/")[0] not in listOfFolders:
            # if parent folder is not present than create a new Schema or Don't proceed further
            print('''oh! I did not find the parent folder .
                    Suggestion : TO CREATE A NEW NAMING SCHEMA AND ORGANISE IT AGAIN!!''')
            userchoice=input("Do you agree with the above Suggestion if yes press \'y\' or for no press \'n\' : ")
            
            if userchoice=="y" or userchoice=="Y":
                # if user  agrees with the Suggestion than , Del old Naming Schema and Creating new one    
                os.remove(filename)
                self.__init__(userchoice)
            else:
                # if User does not agrees to the Suggestion 
                print("I apologize ! Couldn't Organise your Directory . Exiting ...")
                
        else:
            os.system("cls")
            # if parent file is there in the Directory , perform the required function
            print("Moving Log : ")
            # get all folder available folders inside parent folder
            foldersAlreadyExists=os.listdir(parentFolder)
           
            flag=False
            # iterating on folder structure 
            for key in folderStructure:
                time.sleep(1)
                # checking whether the Folder already exits ,
                if folderStructure[key] in foldersAlreadyExists:
                    # if yes , then directly move 
                    
                    sysResponse,restfiles=self.moveFiles(destination=parentFolder+folderStructure[key],files=[file for file in listOfFiles if key == os.path.splitext(file)[1] ])
                else:
                    #os.makedirs()
                    # if not there then create one and move
                    print("Entered file not found! Creating one! ")
                    os.makedirs(parentFolder+folderStructure[key])
                    sysResponse,restfiles=self.moveFiles(destination=parentFolder+folderStructure[key],files=[file for file in listOfFiles if key == os.path.splitext(file)[1] ])
                # check whether all files ave moved Successfully or not
                if sysResponse:
                    # if yes 
                    print(f"All {key} files transfered successfully")
                    flag=True
                else:
                    # if no then show how many files didnot move
                    print(f"oh! no {restfiles} {key} Files unable to transfer")
                    
            if flag:
                print("ALL files Transferred Successfully")
            else:
                print("NO files")
                    
                    
                    
                
    def moveFiles(self,destination,files):
        
        #print(files)
        #print(destination)
        res=files[:]
        for file in files:
            source=file
            shutil.move(source,destination)
            res.remove(file)
        
        if len(res)>0:
            return False,len(res)
        else:
            return True,None
        
        
            
        
            
        
    
    
   
    def  create_Update_dictionary(self,customFolder=None,key=None):
        default_dic={
                ".py":"Python Files",
                ".ipynb": "Jupyter Python Files",
                ".java":"Java Files",
                ".cpp":"C++ Files",
                ".c":"C Files",
                ".html":"Html Files",
                ".css" : "Css Files",
                "ParentFolder":"OrganisedFolder/"
            }
        
        try:
            
            if customFolder!=None and key!=None:
                # Updating Custom Naming Schema
                Custom_dic=default_dic
                #setting custom folder name :
                del Custom_dic["ParentFolder"]
                Custom_dic[key]=customFolder
                # removing old files dictionary
                listOfFiles=os.listdir()
                for file in listOfFiles:
                    if file==self.CustomSchema:
                        os.remove(self.CustomSchema)
                    elif file==self.Default_Schema:
                        os.remove(self.Default_Schema)
                    else:
                        continue
                
                with open(self.CustomSchema,"w") as JSon:
                    json.dump(Custom_dic,JSon,indent=4)
                
                #creating parent folder
                os.mkdir(Custom_dic[key])
                
                
                return Custom_dic
                
            else:
                listOfFiles=os.listdir()
                for file in listOfFiles:
                    if file==self.CustomSchema:
                        os.remove(self.CustomSchema)
                        
                    elif file==self.Default_Schema:
                        os.remove(self.Default_Schema)
                    else:
                        continue
                # creating default naming schema File
                with open(self.Default_Schema,"w") as j:
                    json.dump(default_dic , j,indent=4)
                os.mkdir(default_dic["ParentFolder"])
                return default_dic
        except FileNotFoundError:
            print("Somewent wrong ! ")
        except FileExistsError:
            print("File Exist already!!")
            
            
    def check_already_organised(self):
        listDir=os.listdir()
        for dir in listDir:
            if dir==self.Default_Schema:
                with open(self.Default_Schema,"r") as J:
                    content=json.load(J)
                return content
            elif dir ==self.CustomSchema:
                with open(self.CustomSchema,"r") as J:
                    content=json.load(J)
                return content 
           
        
              


def welcome_message():
    print("Welcome to My File Organizer!")
    print("Created by Tushar")
    print("This application will organize only the current directory.")
    print("Stay tuned for updates to organize other directories.")

def motivational_quote():
    quote = "“The secret of getting ahead is getting started.” - Mark Twain"
    print(f"\nHere's a quote to inspire you:\n{quote}")

def main():
    os.system("cls")
    welcome_message()
    motivational_quote()
    FileOrganiser("y")

if __name__ == "__main__":
    main()
 
     
