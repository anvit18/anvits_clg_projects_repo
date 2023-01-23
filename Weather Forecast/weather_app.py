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
import calendar
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
            #api for weather
        api_base_url="https://api.openweathermap.org/data/2.5/weather?"
        api_key = '696058fd4fb54ca5dacc654f0110d019'
        url=api_base_url + "appid=" + api_key + "&q=" + city
        json_data = requests.get(url).json()
        #condition = json_data['weather'][0]['main']
        details = json_data['weather'][0]['description']
        temp_cel= int(json_data['main']['temp']-273.15)
        temp_faren = 1.8*temp_cel + 32
        temp_faren = round(temp_faren,1)
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
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry, Please enter a proper city name.")

def open():
    w2=Toplevel()
    w2.title("Know your week - Weather App")
    w2.geometry("900x500")
    w2.maxsize(900,500)
    w2.minsize(900,500)
    w2.configure(bg="black")

    #logo
    image_icon2=PhotoImage(file="Images/logo.png")
    w2.iconphoto(False,image_icon2)

    #frame 1
    frame1=Frame(w2,width=900,height=150,bg="#010082",highlightbackground="white",highlightthickness=3)
    frame1.pack(side=TOP)

    first = datetime.now()
    month = datetime.now().month
    year = datetime.now().year
    date_day = f"{datetime.now().day} {calendar.month_abbr[month]} {year}"

    day1=Label(frame1,text=f'''{first.strftime("%A")}, {date_day}''',font=("Helvetica",30,'bold'),fg="white",bg="#010082")
    day1.place(x=40,y=50)

    day1_day=Label(frame1,text=f'''Day   : \nNight :''',font=("Helvetica",12,'bold'),fg="white",bg="#010082")
    day1_day.place(x=750,y=50)

     #frame 2
    frame2=Frame(w2,width=120,height=200,bg="#010082",highlightbackground="white",highlightthickness=3)
    frame2.place(x=10,y=180)

    second=first+timedelta(days=1)

    day2=Label(frame2,text=second.strftime("%A"),font=("Helvetica",14,'bold'),fg="white",bg="#010082")
    day2.place(x=5,y=10)

    day2_day=Label(frame2,text=f'''Day   : \nNight :''',font=("Helvetica",10,'bold'),fg="white",bg="#010082")
    day2_day.place(x=2,y=150)
   
    #frame 3
    frame3=Frame(w2,width=120,height=200,bg="#010082",highlightbackground="white",highlightthickness=3)
    frame3.place(x=160,y=180)

    third = first + timedelta(days=2)
    
    day3=Label(frame3,text=third.strftime("%A"),font=("Helvetica",14,'bold'),fg="white",bg="#010082")
    day3.place(x=0,y=10)

    day3_day=Label(frame3,text=f'''Day   : \nNight :''',font=("Helvetica",10,'bold'),fg="white",bg="#010082")
    day3_day.place(x=0,y=150)

    #frame 4
    frame4=Frame(w2,width=120,height=200,bg="#010082",highlightbackground="white",highlightthickness=3)
    frame4.place(x=310,y=180)

    fourth = first + timedelta(days=3)

    day4=Label(frame4,text=fourth.strftime("%A"),font=("Helvetica",14,'bold'),fg="white",bg="#010082")
    day4.place(x=5,y=10)

    day4_day=Label(frame4,text=f'''Day   : \nNight :''',font=("Helvetica",10,'bold'),fg="white",bg="#010082")
    day4_day.place(x=2,y=150)

    #frame 5
    frame5=Frame(w2,width=120,height=200,bg="#010082",highlightbackground="white",highlightthickness=3)
    frame5.place(x=460,y=180)

    fifth = first + timedelta(days=4)

    day5=Label(frame5,text=fifth.strftime("%A"),font=("Helvetica",14,'bold'),fg="white",bg="#010082")
    day5.place(x=20,y=10)

    day5_day=Label(frame5,text=f'''Day   : \nNight :''',font=("Helvetica",10,'bold'),fg="white",bg="#010082")
    day5_day.place(x=2,y=150)

    #frame 6

    frame6=Frame(w2,width=120,height=200,bg="#010082",highlightbackground="white",highlightthickness=3)
    frame6.place(x=610,y=180)

    sixth = first + timedelta(days=5)

    day6=Label(frame6,text=sixth.strftime("%A"),font=("Helvetica",14,'bold'),fg="white",bg="#010082")
    day6.place(x=7,y=10)

    day6_day=Label(frame6,text=f'''Day   : \nNight :''',font=("Helvetica",10,'bold'),fg="white",bg="#010082")
    day6_day.place(x=1,y=150)
   #frame 7

    frame7=Frame(w2,width=120,height=200,bg="#010082",highlightbackground="white",highlightthickness=3)
    frame7.place(x=760,y=180)

    seventh = first + timedelta(days=6)

    day7=Label(frame7,text=seventh.strftime("%A"),font=("Helvetica",14,'bold'),fg="white",bg="#010082")
    day7.place(x=18,y=10)

    day7_day=Label(frame7,text=f'''Day   : \nNight :''',font=("Helvetica",10,'bold'),fg="white",bg="#010082")
    day7_day.place(x=2,y=150)
    
    notice = Label(w2, text="*P.S Demo icons placed, api integration will display day wise temp. and icon.", bg="orange", fg="black")
    notice.pack(side=BOTTOM, pady=10)
     
    btnclose=Button(w2,text="CLOSE", font="sansserifcollection 12 bold",command=w2.destroy,fg="white",bg="#010082")
    btnclose.pack(side=BOTTOM, pady=20)
    



root.title("Weather App")
root.geometry("900x500")
root.maxsize(900,500)
root.minsize(900,500)

#logo
image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)



#search box
photo=PhotoImage(file="Images/search.png")
search_label=Label(image=photo)
search_label.place(x=20,y=20)

#entry form
search_entry=StringVar()
search_box=Entry(root, justify="center",width=17,font= "clarendon 25 bold",bg="#404040",border=0,fg="white",textvariable=search_entry)
search_box.place(x=50,y=40)
search_box.focus()

#search image
searchi=PhotoImage(file="Images/searchi.png")
buttonsearch=Button(image=searchi,borderwidth=0,cursor="hand2",bg="#404040",command=searchcity)
buttonsearch.place(x=400,y=34)

#to enter button press
root.bind('<Return>', lambda event : searchcity())

#search box left image
left_image=PhotoImage(file="Images/search_box2.png")
weather_image=Label(image=left_image,borderwidth=15,bg="#404040")
weather_image.place(x=57,y=31)

#weather logo
w_logo=PhotoImage(file="Images/weather_image.png")
weather_logo=Label(image=w_logo,borderwidth=15)
weather_logo.place(x=130,y=100)


#sunrise sunset

sunrise=PhotoImage(file="Images/sunrise_img.png")
i_sunrise=Label(image=sunrise)
i_sunrise.place(x=550,y=250)

sunset=PhotoImage(file="Images/sunset_img.png")
i_sunset=Label(image=sunset)
i_sunset.place(x=750,y=250)

#box
box=PhotoImage(file="Images/box bottom.png")
box_image=Label(image=box)
box_image.pack(side=BOTTOM)

#labels
name1=Label(root,text="WIND",font=("Arial Black",15,'bold'),fg="white",bg="#010082")
name1.place(x=55,y=400)

name2=Label(root,text="HUMIDITY",font=("Arial Black",15,'bold'),fg="white",bg="#010082")
name2.place(x=250,y=400)

name3=Label(root,text="DETAILS",font=("Arial Black",15,'bold'),fg="white",bg="#010082")
name3.place(x=500,y=400)


name4=Label(root,text="PRESSURE",font=("Arial Black",15,'bold'),fg="white",bg="#010082")
name4.place(x=750,y=400)

#adding dot dot
temp_label_=Label(text="...",font="arial 47 bold",fg="#010082")
temp_label_.place(x=495,y=150)

clock=Label(font="stencil 35 bold")
clock.place(x=680,y=7)
date_label=Label(font="stencil 20 bold")
date_label.place(x=720,y=55)

b=Label(text="Timezone : ",font="sansserifcollection 11 bold")
b.place(x=70,y=90)
time_zone=Label(justify="center",font="sansserifcollection 13 bold")
time_zone.place(x=165,y=90)


#b=Label(text="...",font="arial 70 bold")
#b.place(x=400,y=250)

wind_=Label(text="...",font="arial 18 bold",fg="white" ,bg="#010082")
wind_.place(x=40,y=430)

humidity_=Label(text="...",font="arial 18 bold",fg="white", bg="#010082")
humidity_.place(x=270,y=430)

detail_=Label(text="...",font="arial 18 bold",fg="white", bg="#010082")
detail_.place(x=480,y=430)

pressure_=Label(text="...",font="arial 18 bold",fg="white", bg="#010082")
pressure_.place(x=750,y=430)

sunrise_time_=Label(font="arial 12 bold")
sunrise_time_.place(x=500,y=330)

sunset_time_=Label(font="arial 12 bold")
sunset_time_.place(x=700,y=330)

btnopen=Button(root,text="CLICK TO VIEW WEEK", font="sanserifcollection 12 bold", command=open, fg="white",bg="#010082")
btnopen.place(x=200,y=330)





root.mainloop()