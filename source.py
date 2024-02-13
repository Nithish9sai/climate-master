from tkinter import *
import datetime
import time
import requests
import tkinter.messagebox


currentTime = datetime.datetime.now()
root = Tk()
HEIGHT = 600
WIDTH = 600
root.geometry("1000x600")
root.title('Climate Master')
root.iconbitmap(r'cloud.ico')

def format_response(weather):
    try:
        area = weather['name']
        lon = weather['coord']['lon']
        lat = weather['coord']['lat']
        weather_desc = weather['weather'][0]['description']
        humidity = weather['main']['humidity']
        temp = weather['main']['temp']
        speed = weather['wind']['speed']
        sunrise = time.ctime(weather['sys']['sunrise'])
        sunset = time.ctime(weather['sys']['sunset'])
        windir = weather['wind']['deg']
        final_string = 'Name=%s\nLongitude=%s°\nLatitude=%s° \nClimate=%s\nHumidity=%s%%\nTemperature(°C)=%s\nWind Speed(m/s)=%s\nSunrise=%s\nSunset=%s\nWind Direction=%s°'%(area,lon,lat,weather_desc,humidity,temp,speed,sunrise,sunset,windir)
    except:
        final_string ='Oops something went wrong, Please try later'

    return final_string
def getweather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=cd2ff7d211bfde3c102b8b20362d5ed9'.format(city)
    response = requests.get(url)
    weather = response.json()

    output_label['text']=format_response(weather)

baground_img= PhotoImage(file = 'mountains.png')
baground_label=Label(root, image=baground_img)
baground_label.place(relwidth=1, relheight=1)

if currentTime.hour < 12:
    wel_msg = Label(root, text='Hey there! Good Morning', relief='solid', font=('Times New Roman', 15, 'bold'), bg='#1aff1a')
elif 12 <= currentTime.hour < 16:
    wel_msg = Label(root, text='Hey there! Good Afternoon', relief='solid', font=('Times New Roman', 15, 'bold'), bg='#ffff00')
elif 16 <= currentTime.hour < 19:
    wel_msg = Label(root, text='Hey there! Good Evening', relief='solid', font=('Times New Roman', 15,'bold'), bg='#ff8533')
else:
    wel_msg = Label(root, text='Hey there! Good Night', relief='solid', font=('Times New Roman', 15, 'bold'), bg='#66e0ff')

wel_msg.pack(fill=BOTH, padx=2, pady=2)

Data_Ent_msg=Label(root, text='City Name/Zip code', font=("Times New Roman",15),bg='#FAE7E7')
Data_Ent_msg.place(relx=0.17, rely=0.2)

entry_1=Entry(root, font=15)
entry_1.place(relx=0.17, rely=0.3, relwidth=0.65, relheight=0.1)

button_1=Button(root, text='Get Report', bg='#ff8c66', font=(12), command=lambda: getweather(entry_1.get()))
button_1.place(relx=0.65, rely=0.2)

lower_frame = Frame(root,bg='#800040',bd=10)
lower_frame.place(relx=0.5,rely=0.43,relwidth=0.66, relheight=0.5, anchor='n')

output_label = Label(lower_frame,bg='#fff0e6',font=('Courier',15))
output_label.place(relheight=1,relwidth=1)

tkinter.messagebox.showinfo('Request','Please Read the Instructions carefully from usage.txt before you use This Software')

answer = tkinter.messagebox.askquestion('Terms and Conditions','Do you accept The terms and conditions ')
if answer == 'no':
    root.destroy()
root.mainloop()
