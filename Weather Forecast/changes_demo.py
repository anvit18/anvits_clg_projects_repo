from tkinter import *
#for co-ordinates
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
#for timezone
from timezonefinder import TimezoneFinder
from datetime import datetime
from datetime import timedelta
#for timezone calculation
import pytz
import requests
from PIL import Image, ImageTk

root=Tk()

def searchcity():
    try: 
        city=search_entry.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        time_zone_obj=TimezoneFinder()
        result=time_zone_obj.timezone_at(lng=location.longitude, lat=location.latitude)
        curr_location=pytz.timezone(result)
        local_time=datetime.now(curr_location)
        curr_time=local_time.strftime("%I:%M %p")
        curr_date=f"{datetime.now(curr_location).day}/{datetime.now(curr_location).month}/{datetime.now(curr_location).year}"
        clock.config(text=curr_time)
        #name.config(text="TIME:")
        time_zone.config(text=result)
        print(f"City Name is: {city}")
        #firstdayimage=json_data['daily'][0]['weather'][0]['icon']
        #print(firstdayimage)
            #api for weather
        api_base_url="https://api.openweathermap.org/data/2.5/weather?"
        api_key = '696058fd4fb54ca5dacc654f0110d019'
        url=api_base_url + "appid=" + api_key + "&q=" + city
        json_data = requests.get(url).json()
        details = json_data['weather'][0]['description']
        temp_cel= int(json_data['main']['temp']-273.15)
        temp_faren = 1.8*temp_cel + 32
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind= json_data['wind']['speed']
        sunrise_time=datetime.utcfromtimestamp(json_data['sys']['sunrise']+json_data['timezone'])
        sunset_time=datetime.utcfromtimestamp(json_data['sys']['sunset']+json_data['timezone'])
        sunrise_time_.config(text=f"{sunrise_time}")
        sunset_time_.config(text=f"{sunset_time}")
        temp_label_.config(text=f"{temp_cel}°C | {temp_faren}°F")
        #feels_like.config(text=f"feels: {temp} °C")
        wind_.config(text=f"{wind} m/s") 
        detail_.config(text=f"{details}")
        humidity_.config(text=f"{humidity} %")
        pressure_.config(text=f"{pressure} hPa")
        date_label.config(text=curr_date)
        

        #new window stuff
        
    
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry, Please enter a proper city name.")

def open():
    w2=Toplevel()
    w2.title("History of the cities")
    w2.geometry("900x500")

    city=search_entry.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    api_key = '696058fd4fb54ca5dacc654f0110d019'
    api2_base_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&exclude=hourly&appid={api_key}"
    json2_data = requests.get(api2_base_url).json()
    humidityy=json2_data['current']['humidity']
    print(humidityy)
    print(api2_base_url)
    


    #set first
    first = datetime.now()
    #set other days
    
    #firstdayimage = json2_data['daily']['daily']['weather'][0]['icon']
    #print(firstdayimage)
    #seconddayimage=json_data['weather'][0]['icon']
    #print(seconddayimage)
    #thirddayimage=json_data['weather'][0]['icon']
    #print(thirddayimage)
    #fourthdayimage=json_data['weather'][0]['icon']
    #print(fourthdayimage)
    photo1 = PhotoImage(file=f"Icons Weather/02d@2x.png")
    firstimage = Label(image=photo1)
    firstimage.place(x=100, y=20)

    #day1
    day1=Label(w2, text=first.strftime("%A"))
    day1.place(x=100,y=50)

    #day2
    second=first+timedelta(days=1)
    day2=Label(w2, text=second.strftime("%A"))
    day2.place(x=100, y=70)

    #other days
    third=first+timedelta(days=2)
    day3=Label(w2, text=third.strftime("%A"))
    day3.place(x=100, y=90)

    fourth=first+timedelta(days=3)
    day4=Label(w2, text=fourth.strftime("%A"))
    day4.place(x=100, y=110)

    fifth=first+timedelta(days=4)
    day5=Label(w2, text=fifth.strftime("%A"))
    day5.place(x=100, y=130)

    sixth=first+timedelta(days=5)
    day6=Label(w2, text=sixth.strftime("%A"))
    day6.place(x=100, y=150)

    seventh=first+timedelta(days=6)
    day7=Label(w2, text=seventh.strftime("%A"))
    day7.place(x=100, y=170)



root.title("Weather App")
root.geometry("900x500")
root.maxsize(900,500)
root.minsize(900,500)


#search box
photo=PhotoImage(file="search.png")
search_label=Label(image=photo)
search_label.place(x=20,y=20)

#entry form
search_entry=StringVar()
search_box=Entry(root, justify="center",width=17,font= "clarendon 25 bold",bg="#404040",border=0,fg="white",textvariable=search_entry)
search_box.place(x=50,y=40)
search_box.focus()

#search image
searchi=PhotoImage(file="searchi.png")
buttonsearch=Button(image=searchi,borderwidth=0,cursor="hand2",bg="#404040",command=searchcity)
buttonsearch.place(x=400,y=34)


root.bind('<Return>', lambda event : searchcity())

#weather logo
w_logo=PhotoImage(file="weather_image.png")
weather_logo=Label(image=w_logo,borderwidth=15)
weather_logo.place(x=130,y=100)


#sunrise sunset
w_sunrise=PhotoImage(file="#FF5669_box.png")
weather_sunrise=Label(image=w_sunrise,borderwidth=15)
weather_sunrise.place(x=350,y=220)

#box
box=PhotoImage(file="box bottom.png")
box_image=Label(image=box)
box_image.pack(side=BOTTOM)

#labels
name1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
name1.place(x=120,y=400)

name2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
name2.place(x=267,y=400)

name3=Label(root,text="DETAILS",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
name3.place(x=438,y=400)


name4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
name4.place(x=650,y=400)

sunr=Label(root,text="SUNRISE",font=("Helvetica",13,'bold'),fg="white",bg="#FF5669")
sunr.place(x=570,y=255)

suns=Label(root,text="SUNSET",font=("Helvetica",13,'bold'),fg="white",bg="#FF5669")
suns.place(x=570,y=320)



#adding dot dot
temp_label_=Label(text="...",font="arial 40 bold",fg="red")
temp_label_.place(x=495,y=150)

clock=Label(font="stencil 35 bold")
clock.place(x=680,y=7)
date_label=Label(font="stencil 20 bold")
date_label.place(x=720,y=55)

b=Label(text="Timezone : ",font="verdana 11 bold")
b.place(x=70,y=90)
time_zone=Label(justify="center",font="verdana 11 bold")
time_zone.place(x=165,y=90)


#b=Label(text="...",font="arial 70 bold")
#b.place(x=400,y=250)

wind_=Label(text="...",font="arial 18 bold", bg="#1ab5ef")
wind_.place(x=100,y=430)

humidity_=Label(text="...",font="arial 18 bold", bg="#1ab5ef")
humidity_.place(x=280,y=430)

detail_=Label(text="...",font="arial 18 bold", bg="#1ab5ef")
detail_.place(x=432,y=430)

pressure_=Label(text="...",font="arial 18 bold", bg="#1ab5ef")
pressure_.place(x=670,y=430)

sunrise_time_=Label(font="arial 13 bold", bg="#FF5669")
sunrise_time_.place(x=538,y=276)

sunset_time_=Label(font="arial 13 bold", bg="#FF5669")
sunset_time_.place(x=538,y=340)

btnopen=Button(root,text="CLICK TO VIEW HISTORY", command=open, bg="red")
btnopen.place(x=50,y=300)

















 



root.mainloop()