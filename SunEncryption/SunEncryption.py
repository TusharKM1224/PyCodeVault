from pysolar.solar import get_altitude, get_azimuth
import datetime
import pytz
import string
import random
import json
import math
import ephem
import zlib

def compress_key(key):
    original_string = key

    # Compress the string
    compressed_data = zlib.compress(original_string.encode())

    print(f"Compressed data: {compressed_data}")
    print(f"Compressed size: {len(compressed_data)} bytes")

def decompress_key(key):
    decompressed_data = zlib.decompress(key).decode()

    print(f"Decompressed string: {decompressed_data}")
    print(f"Is decompressed string the same as original? {decompressed_data == original_string}")
        

    

def get_moon_Elevation_Azimuth(Year,Month,Date,Hour,Minute,Sec,lat,lng):
    # Define your location (latitude and longitude)
    latitude = lat  # Example: San Francisco, CA
    longitude = lng

    # Define the custom date and time
    custom_date = datetime.datetime(Year,Month, Date, Hour, Minute, Sec) 

    # Specify the timezone using pytz (replace with your desired timezone)
    timezone = pytz.timezone(pytz.country_timezones['IN'][0])

    # Make the custom date and time timezone-aware
    localized_date = timezone.localize(custom_date)

    # Set up observer's location
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)
    observer.date = localized_date

    # Create a Moon object
    moon = ephem.Moon()

    # Compute the moon's position for the observer's location and time
    moon.compute(observer)

    # Get the moon's altitude and azimuth in degrees
    moon_altitude = moon.alt * 180 / ephem.pi  # Convert from radians to degrees
    moon_azimuth = moon.az * 180 / ephem.pi # Convert from radians to degrees
    mode='Night'
    #print(f"Moon Altitude: {moon_altitude:.2f} degrees")
    #print(f"Moon Azimuth: {moon_azimuth:.2f} degrees")

    return moon_altitude,moon_azimuth,mode
    #print(f"Moon Altitude: {moon_altitude:.2f} degrees")
    #print(f"Moon Azimuth: {moon_azimuth:.2f} degrees")


def get_Elevation_Azimuth(Year,Month,Date,Hour,Minute,Sec,lat,lng,country_code='IN',mode='Day'):
    # Example coordinates
    if mode !='Day':
        return get_moon_Elevation_Azimuth(Year,Month,Date,Hour,Minute,Sec,lat,lng)
    else:
        
        latitude = lat 
        longitude = lng

        # Current time in UTC (make timezone-aware using pytz)
        timezone = pytz.timezone(pytz.country_timezones['IN'][0])  
        local_time = datetime.datetime.now() 
        #print(local_time) # Get current local time
        custom_date = datetime.datetime(Year,Month, Date, Hour, Minute, Sec) 
        localized_time = timezone.localize(custom_date)  # Make it timezone-aware

        # Calculate solar position
        elevation = get_altitude(latitude, longitude, localized_time)
        azimuth = get_azimuth(latitude, longitude, localized_time)
        if elevation >0:
            mode='Day'
            #print(f"Sun Altitude: {elevation:.2f} degrees")
            #print(f"Sun Azimuth: {azimuth:.2f} degrees")
            return azimuth , elevation,mode
        else:
            return get_moon_Elevation_Azimuth(Year,Month,Date,Hour,Minute,Sec,lat,lng)
            
       

        #print(f"Solar Elevation: {elevation:.2f} degrees")
        #print(f"Solar Azimuth: {azimuth:.2f} degrees")
        
       

def xor_shift_encrypt(message, key, shift_value):
    encrypted = ''.join([chr((ord(char) ^ key) << shift_value) for char in message])
    return encrypted
def xor_shift_decrypt(encrypted_message, key, shift_value):
    decrypted = ''.join([chr((ord(char) >> shift_value) ^ key) for char in encrypted_message])
    return decrypted

def get_date_time_latlng():
    date=str(datetime.datetime.now())
    date_time=date.split()
    date=date_time[0].split("-")
    time=date_time[1].split(":")
    #lat lng
    lat=random.uniform(-90,90)
    lng=random.uniform(-180,180)
    #print(date_time)
    date_time={"date":date,"time":time,"latitude":lat,"longitude":lng}
    return date_time


# Key encryption
def xor_key_encrypt(message, key):
    ascii_pwd=[]
    upper_case_letter=list(string.ascii_uppercase)
    lower_case_letter=list(string.ascii_lowercase)
    for i in message:
        ascii_words=[]
        for j in i:
            #converting words to ascii state
            #print(ord(j))
            ascii_words.append(int(ord(j)*int(key)))
            #print("\n")
        ascii_pwd.append(ascii_words)
        #print(ascii_pwd)

    ascii_word=[]
    for i in ascii_pwd:
        
        for j in i:
            while int(j)>0:
                #print(j)
                digit=int(j%10)
                ascii_word.append(upper_case_letter[digit])
                j=j//10
            ascii_word.append('d%')
        ascii_word.append('AbC%')
        #print(ascii_word)

    #2nd layer encryption
    encryption_form="".join(ascii_word)
    encryption_form=encryption_form+chr(len(message))
    #print(encryption_form)
    return encryption_form


# key decryption
def xor_key_decrypt(encrypted_message, key):
    upper_case_letter=list(string.ascii_uppercase)
    lower_case_letter=list(string.ascii_lowercase)
    text=encrypted_message
    text=text.split('AbC%') 
    text.pop()
    i=0
    correct_word_order=[]
    while i<len(text):
        word=text[i].split('d%')
        word.pop()
       # print(word)
        correct_letter_order=[]
        for o in word:
            temp_text=[]
            temp1_text=""
            for j in reversed(range(len(o))):
                
                temp_text.append(o[j])
                temp1_text="".join(temp_text)
            correct_letter_order.append(temp1_text)
    
  
        i+=1 
        correct_word_order.append(correct_letter_order)
    
    ascii_num1=[]
    for a in correct_word_order:
        ascii_num=[]
        for d in a:
            #print(d)
            temp_num=[]
            temp1_num=""
            for k in d:
                #print(k)
                if k in upper_case_letter:
                   #print(lower_case_letter.index(k))
                   temp_num.append(upper_case_letter.index(k))
                   temp1_num="".join(map(str,temp_num))
                   #print(temp1_num)
            ascii_num.append(int(int(temp1_num)//int (key)))
        ascii_num1.append(ascii_num)
    final_list=[]
    for v in ascii_num1:
        temp_word=[]
        final_text=""
       
        for y in v:
            character=chr(y)
            temp_word.append(character)
            final_text="".join(temp_word)
        final_list.append(final_text)
    #print(final_list)

    text="".join(final_list)
    return text

def encrpt_key(date_time_latlng):
    date_time_text=json.dumps(date_time_latlng)
    #print(date_time_text)
    #date_time_dict=json.loads(date_time_text)
    secret_key=xor_key_encrypt(date_time_text,len(date_time_text))
    return secret_key
def decrypt_key(secretkey):
    #key=encrpt_key(secretkey)
    key=secretkey
    value=xor_key_decrypt(key,ord(key[-1]))
    value=json.loads(value)
    
    return value
    

    # encyption text
def encrytion_text(message):
    try:
        pwd=message
        pwd=pwd.split()
        ascii_pwd=[]
        encrytion_form=""
        date_time_latlng=get_date_time_latlng() # returns  Dictionary
        date=date_time_latlng["date"] #Current Date
        time=date_time_latlng["time"]# Current TIme 
        lat=date_time_latlng["latitude"] # Random latitude
        lng=date_time_latlng["longitude"] # Random logitude
        
        
        lower_case_letter=list(string.ascii_lowercase)
        #Getting Sun's position
        secret_value_key,secret_shift_value,mode =get_Elevation_Azimuth(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),math.ceil(float(time[2])),lat,lng)
        date_time_latlng['mode']=mode
        #!----1st layer encryption ----!
        #converting sentence into ascii state...
        for i in pwd:
            ascii_words=[]
            for j in i:
                #converting words to ascii state
                #print(ord(j))
                ascii_words.append(int(ord(j)*int(secret_value_key)))
                #print("\n")
            ascii_pwd.append(ascii_words)
            #print(ascii_pwd)
        ascii_word=[]
        for i in ascii_pwd:
            
            for j in i:
                while int(j)>0:
                    #print(j)
                    digit=int(j%10)
                    ascii_word.append(lower_case_letter[digit])
                    j=j//10
                ascii_word.append('D%')
            ascii_word.append('aBc%')
        encrytion_form="".join(ascii_word)    
        #!-----End of 1st layer encryption -----!
        #!-----2nd layer encrytion ------!
        encrypted_message=xor_shift_encrypt(encrytion_form,int(secret_value_key),1)
        #!-----End of 2nd layer encrption ------!
        Secret_key=encrpt_key(date_time_latlng)
        #print(date)
        #print(time)
        #print(lat)
        #print(lng)
        
        
    except Exception:
        print("Something went wrong!") 
        return None 
    else:
        return encrypted_message , Secret_key       
  


def decryption_text(message,Skey):
    try:
        text=message
        date_time_latlng=decrypt_key(Skey)
        #print("------")
        #print(date_time_latlng)
        date=date_time_latlng["date"] #Current Date
        time=date_time_latlng["time"]# Current TIme 
        lat=date_time_latlng["latitude"] # Random latitude
        lng=date_time_latlng["longitude"] # Random logitude
        mode=date_time_latlng["mode"]#mode
    
        
        secret_value,secret_shift_value,mode=get_Elevation_Azimuth(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),math.ceil(float(time[2])),lat,lng,mode=mode)
        lower_case_letter=list(string.ascii_lowercase)
        ascii_word=[]
        #print(int(secret_value))
        #print(text)
        text=xor_shift_decrypt(text,int(secret_value),1)
        text=text.split('aBc%') 
        text.pop()
        i=0
        correct_word_order=[]
        while i<len(text):
            word=text[i].split('D%')
            word.pop()
        # print(word)
            correct_letter_order=[]
            for o in word:
                temp_text=[]
                temp1_text=""
                for j in reversed(range(len(o))):
                    
                    temp_text.append(o[j])
                    temp1_text="".join(temp_text)
                correct_letter_order.append(temp1_text)
            i+=1 
            correct_word_order.append(correct_letter_order)
        
        ascii_num1=[]
        for a in correct_word_order:
            ascii_num=[]
            for d in a:
                #print(d)
                temp_num=[]
                temp1_num=""
                for k in d:
                    #print(k)
                    if k in lower_case_letter:
                        #print(lower_case_letter.index(k))
                        temp_num.append(lower_case_letter.index(k))
                        temp1_num="".join(map(str,temp_num))
                ascii_num.append(int(int(temp1_num)/int (secret_value)))
            ascii_num1.append(ascii_num)
        final_list=[]
        for v in ascii_num1:
            temp_word=[]
            final_text=""
        
            for y in v:
                character=chr(y)
                temp_word.append(character)
                final_text="".join(temp_word)
            final_list.append(final_text)
        #print(final_list)

        text=" ".join(final_list)
        
    except Exception:
        print("Something went worng!")
        return None 
    else:
        return text     
   
if encrytion_text("I am a boy")==None:
    print("something is wrong")
else:
    text, key =encrytion_text("I am a boy")


#print(text)
#print(key)
if decryption_text(text,key)==None:
    print("something is wrong")
else:
    actualtext= decryption_text(text,key)
print(actualtext)

#compress_key(key)


            
    
            
            
            
            
    
    
                   
    
    
    
    
            
    
                     
            



    
    
