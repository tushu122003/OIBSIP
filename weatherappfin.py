import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
import requests
from datetime import datetime, timedelta
#import android    {for intrgration to android}

class MyApp(tk.Frame):
    def __init__(self, root):
        super().__init__(root, bg='#DABFA4')
        self.root = root
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        # Load the search image
        search_image = Image.open('oasisinfobyte/search_bar.jpg')  
        self.search_photo = ImageTk.PhotoImage(search_image)
        search_label = tk.Label(self.main_frame, image=self.search_photo, bd=0)
        search_label.place(x=90, y=20)
        # Create a text entry field for search
        self.textfield = tk.Entry(self.main_frame, justify="center", width=17, font=("poppins", 22, "bold"), bg='#F0E7D8',bd=0)
        self.textfield.place(x=100, y=26.5)
        self.textfield.focus()
        # Load the search icon
        search_icon = Image.open('oasisinfobyte/searchicon.jpg')  # Update the path to your searchicon.jpg image
        self.search = ImageTk.PhotoImage(search_icon)
        # Create a button for search
        search_button = tk.Button(self.main_frame, image=self.search, borderwidth=0, cursor="hand2", command=self.search_weather)
        search_button.place(x=390, y=20)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #incase of andriod integration to get gps
        Locat_icon = Image.open('oasisinfobyte/location-icon.png')  
        self.locate = ImageTk.PhotoImage(Locat_icon)
        # Create a button for Gps location
        location_button = tk.Button(self.main_frame, image=self.locate, borderwidth=0, bg='sienna', cursor="hand2")#add command=self.get_gps
        location_button.place(x=475, y=19)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # left box
        box_image = Image.open('oasisinfobyte/box.jpg')  
        self.box_photo = ImageTk.PhotoImage(box_image)
        box_label = tk.Label(self.main_frame, image=self.box_photo, bd=0)
        box_label.place(x=20, y=100)
        #right box
        box1_image = Image.open('oasisinfobyte/box1.png')  
        self.box1_photo = ImageTk.PhotoImage(box1_image)
        box1_label = tk.Label(self.main_frame, image=self.box1_photo, bd=0)
        box1_label.place(x=230, y=100)
        # Permanent labels for weather information in box 1
        currentweather_label = tk.Label(self.main_frame, text="Current Weather", font=("poppins", 12, "bold"), fg='black',bg='#8A6F5C')
        currentweather_label.place(x=30, y=110)        
        description_label = tk.Label(self.main_frame, text="Description :", font=("Arial", 9),bg='#8A6F5C')
        description_label.place(x=30, y=150)
        temperature_label = tk.Label(self.main_frame, text="Temperature :",  font=("Arial", 9),bg='#8A6F5C')
        temperature_label.place(x=30, y=185)
        humidity_label = tk.Label(self.main_frame, text="Humidity :", font=("Arial", 9),bg='#8A6F5C')
        humidity_label.place(x=30, y=220)
        wind_speed_label = tk.Label(self.main_frame, text="Wind Speed :", font=("Arial", 9),bg='#8A6F5C')
        wind_speed_label.place(x=30, y=255)
        # Empty labels below the permanent labels to show weather information
        self.description_info = tk.Label(self.main_frame, text="", font=("Arial", 9),bg='#8A6F5C')
        self.description_info.place(x=120, y=150)
        self.temperature_info = tk.Label(self.main_frame, text="", font=("Arial", 9),bg='#8A6F5C')
        self.temperature_info.place(x=120, y=185)
        self.humidity_info = tk.Label(self.main_frame, text="", font=("Arial", 9),bg='#8A6F5C')
        self.humidity_info.place(x=120, y=220)
        self.wind_speed_info = tk.Label(self.main_frame, text="", font=("Arial", 9),bg='#8A6F5C')
        self.wind_speed_info.place(x=120, y=255)
        #BOTTOM BOX
        frame = tk.Frame(self.main_frame, width=550, height=330, bg="#F0E7D8")
        frame.pack(side=tk.BOTTOM)
        forecastat3_label = tk.Label(self.main_frame, text="Weather at every hour:", font=("poppins", 12, "bold"), fg='black',bg='#F0E7D8')
        forecastat3_label.place(x=30, y=325)        
        # BoTTOM BOXES(a)(hourly forecast)
        box2a_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box2a_photo = ImageTk.PhotoImage(box2a_image)
        box2a_label = tk.Label(self.main_frame, image=self.box2a_photo, bd=0, bg='sienna')
        box2a_label.place(x=20, y=350)
        box3a_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box3a_photo = ImageTk.PhotoImage(box3a_image)
        box3a_label = tk.Label(self.main_frame, image=self.box3a_photo, bd=0, bg='sienna')
        box3a_label.place(x=125, y=350)
        box4a_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box4a_photo = ImageTk.PhotoImage(box4a_image)
        box4a_label = tk.Label(self.main_frame, image=self.box4a_photo, bd=0, bg='sienna')
        box4a_label.place(x=230, y=350)
        box5a_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box5a_photo = ImageTk.PhotoImage(box5a_image)
        box5a_label = tk.Label(self.main_frame, image=self.box5a_photo, bd=0, bg='sienna')
        box5a_label.place(x=336, y=350)
        box6a_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box6a_photo = ImageTk.PhotoImage(box6a_image)
        box6a_label = tk.Label(self.main_frame, image=self.box6a_photo, bd=0, bg='sienna')
        box6a_label.place(x=440, y=350)
        forecastdaily_label = tk.Label(self.main_frame, text="Daily Weather:", font=("poppins", 12, "bold"), fg='black',bg='#F0E7D8')
        forecastdaily_label.place(x=30, y=480)
        # BoTTOM BOXES(b)(daily forecast)
        box2b_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box2b_photo = ImageTk.PhotoImage(box2b_image)
        box2b_label = tk.Label(self.main_frame, image=self.box2b_photo, bd=0, bg='#F0E7D8')
        box2b_label.place(x=20, y=500)
        box3b_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box3b_photo = ImageTk.PhotoImage(box3b_image)
        box3b_label = tk.Label(self.main_frame, image=self.box3b_photo, bd=0, bg='#F0E7D8')
        box3b_label.place(x=125, y=500)
        box4b_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box4b_photo = ImageTk.PhotoImage(box4b_image)
        box4b_label = tk.Label(self.main_frame, image=self.box4b_photo, bd=0, bg='#F0E7D8')
        box4b_label.place(x=230, y=500)
        box5b_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box5b_photo = ImageTk.PhotoImage(box5b_image)
        box5b_label = tk.Label(self.main_frame, image=self.box5b_photo, bd=0, bg='#F0E7D8')
        box5b_label.place(x=336, y=500)
        box6b_image = Image.open('oasisinfobyte/box2.jpg')  
        self.box6b_photo = ImageTk.PhotoImage(box6b_image)
        box6b_label = tk.Label(self.main_frame, image=self.box6b_photo, bd=0, bg='#F0E7D8')
        box6b_label.place(x=440, y=500)
    # Creating labels for weather information in each 1-hour interval

        #Right box for todays weather
        cellzero = tk.Frame(self.main_frame, width=300, height=201, bg="#8A6F5C")
        cellzero.place(x=230,y=100)
        self.day1=tk.Label(cellzero,font='poppins 18 bold', bg="#8A6F5C",fg="#fff")
        self.day1.place(x=175,y=2)
        self.zerothimage=tk.Label(cellzero,image="", bg="#8A6F5C")
        self.zerothimage.place(x=25,y=30)

        # Labels for day 1 forecast information
        self.day1_description_label = tk.Label(cellzero, text="", font=("Arial", 12,'bold'), bg='#8A6F5C')
        self.day1_description_label.place(x=176, y=130)

        self.day1_temperature_max_label = tk.Label(cellzero, text="", font=("Arial", 12,'bold'), bg='#8A6F5C')
        self.day1_temperature_max_label.place(x=176, y=150)

        self.day1_temperature_min_label = tk.Label(cellzero, text="", font=("Arial", 12,'bold'), bg='#8A6F5C')
        self.day1_temperature_min_label.place(x=175, y=170)
        #bottom cells(a)
        cellone = tk.Frame(self.main_frame, width=88, height=125, bg="#8A6F5C")
        cellone.place(x=20,y=350)
        self.interval1=tk.Label(cellone,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.interval1.place(x=8,y=5)
        self.first_hr_image=tk.Label(cellone, bg="#8A6F5C")
        self.first_hr_image.place(x=15,y=26)        
    
        celltwo = tk.Frame(self.main_frame, width=88, height=125, bg="#8A6F5C")
        celltwo.place(x=125, y=350)
        self.interval2=tk.Label(celltwo,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.interval2.place(x=8,y=5)
        self.second_hr_image=tk.Label(celltwo, bg="#8A6F5C")
        self.second_hr_image.place(x=15,y=26)

        cellthree = tk.Frame(self.main_frame, width=88, height=125, bg="#8A6F5C")
        cellthree.place(x=230, y=350)
        self.interval3=tk.Label(cellthree,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.interval3.place(x=8,y=5)
        self.third_hr_image=tk.Label(cellthree, bg="#8A6F5C")
        self.third_hr_image.place(x=15,y=26)

        cellfour = tk.Frame(self.main_frame, width=88, height=125, bg="#8A6F5C")
        cellfour.place(x=336, y=350)
        self.interval4=tk.Label(cellfour,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.interval4.place(x=8,y=5)
        self.fourth_hr_image=tk.Label(cellfour, bg="#8A6F5C")
        self.fourth_hr_image.place(x=15,y=26)

        cellfive = tk.Frame(self.main_frame, width=88, height=125, bg="#8A6F5C")
        cellfive.place(x=440, y=350)
        self.interval5=tk.Label(cellfive,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.interval5.place(x=8,y=5)
        self.fifth_hr_image=tk.Label(cellfive, bg="#8A6F5C")
        self.fifth_hr_image.place(x=15,y=26)
                #bottom cells(b)
        cellone_b = tk.Frame(self.main_frame, width=88, height=130, bg="#8A6F5C")
        cellone_b.place(x=20,y=503)
        self.day2=tk.Label(cellone_b,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.day2.place(x=8,y=1)
        self.day2_image=tk.Label(cellone_b,bg="#8A6F5C")
        self.day2_image.place(x=18,y=20)

        celltwo_b = tk.Frame(self.main_frame, width=88, height=130, bg="#8A6F5C")
        celltwo_b.place(x=125, y=503)
        self.day3=tk.Label(celltwo_b,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.day3.place(x=8,y=1)
        self.day3_image=tk.Label(celltwo_b, bg="#8A6F5C")
        self.day3_image.place(x=16,y=20)

        cellthree_b = tk.Frame(self.main_frame, width=88, height=130, bg="#8A6F5C")
        cellthree_b.place(x=230, y=503)
        self.day4=tk.Label(cellthree_b,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.day4.place(x=8,y=1)
        self.day4_image=tk.Label(cellthree_b,bg="#8A6F5C")
        self.day4_image.place(x=18,y=20)


        cellfour_b = tk.Frame(self.main_frame, width=88, height=130, bg="#8A6F5C")
        cellfour_b.place(x=336, y=503)
        self.day5=tk.Label(cellfour_b,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.day5.place(x=8,y=1)
        self.day5_image=tk.Label(cellfour_b, bg="#8A6F5C")
        self.day5_image.place(x=18,y=20)

        cellfive_b = tk.Frame(self.main_frame, width=88, height=130, bg="#8A6F5C")
        cellfive_b.place(x=440, y=503)
        self.day6=tk.Label(cellfive_b,font='poppins 12', bg="#8A6F5C",fg="#fff")
        self.day6.place(x=8,y=1)
        self.day6_image=tk.Label(cellfive_b, bg="#8A6F5C")
        self.day6_image.place(x=18,y=20)

        
# Creating labels for weather information in each 1-hour interval
        for i in range(1, 6):
            description_info = tk.Label(self.main_frame, text="", font=("Arial", 9), bg='#8A6F5C')
            setattr(self, f"description_info_{i}", description_info)
            description_info.place(x=22 + (i - 1) * 105, y=440)

            temperature_info = tk.Label(self.main_frame, text="", font=("Arial", 9), bg='#8A6F5C')
            setattr(self, f"temperature_info_{i}", temperature_info)
            temperature_info.place(x=22 + (i - 1) * 105, y=455)
             


# Creating labels for daily weather information starting from day 2 to day 6
        for i in range(2, 7):
            day_description_info = tk.Label(self.main_frame, text="", font=("Arial", 9), bg='#8A6F5C')
            setattr(self, f"daydescription_info_{i}", day_description_info)
            day_description_info.place(x=20 + (i - 2) * 105, y=582)

            day_temperature_max_info = tk.Label(self.main_frame, text="", font=("Arial", 9), bg='#8A6F5C')
            setattr(self, f"daytemperaturemax_info_{i}", day_temperature_max_info)
            day_temperature_max_info.place(x=20 + (i - 2) * 105, y=597)

            day_temperature_min_info = tk.Label(self.main_frame, text="", font=("Arial", 9), bg='#8A6F5C')
            setattr(self, f"daytemperaturemin_info_{i}", day_temperature_min_info)
            day_temperature_min_info.place(x=20 + (i - 2) * 105, y=613)



        # Set application icon
        image_icon = Image.open("oasisinfobyte/logo_Weather.jpg")
        image_icon = ImageTk.PhotoImage(image_icon)
        root.iconphoto(False, image_icon)
        # Display date and time
        self.current_date_time_label = tk.Label(self.main_frame, text="", font=("Arial", 18,'bold'),bg='#DABFA4')
        self.current_date_time_label.place(x=16, y=16)
        self.current_date_label = tk.Label(self.main_frame, text="", font=("Arial", 10,'bold'),bg='#DABFA4')
        self.current_date_label.place(x=16, y=50)
        self.update_date_time()
        
    def update_date_time(self):
        # Get the current date and time
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M")
 
        # Update the labels
        self.current_date_time_label.config(text=current_time)
        self.current_date_label.config(text=current_date)
        # Schedule the update after 1 second
        self.main_frame.after(1000, self.update_date_time)

    def get_current_hour(self):
        now = datetime.now()
        return now.hour

    # Function to fetch weather data using GPS coordinates
    def get_weather(self, latitude, longitude):
        api_key = "b456f58f670ab84137e5d09fc69e70c6"  # Replace with your API key from OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&exclude=hourly&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data["weather"][0]["main"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            # Update the weather information labels
            self.description_info.config(text=weather_description)
            self.temperature_info.config(text=f"{temperature}°C")
            self.humidity_info.config(text=f"{humidity}%")
            self.wind_speed_info.config(text=f"{wind_speed} m/s")

            #days
            first=datetime.now()
            self.day1.config(text=first.strftime("%A"))

            first=datetime.now()
            self.day1.config(text=first.strftime("%A"))

            second=first+timedelta(days=1)
            self.day2.config(text=second.strftime("%A"))
            third=first+timedelta(days=2)
            self.day3.config(text=third.strftime("%A"))
            fourth=first+timedelta(days=3)
            self.day4.config(text=fourth.strftime("%A"))
            fifth=first+timedelta(days=4)
            self.day5.config(text=fifth.strftime("%A"))
            sixth=first+timedelta(days=5)
            self.day6.config(text=sixth.strftime("%A"))
            #1hr interval
            second = first + timedelta(hours=1)
            self.interval1.config(text=second.strftime("%H:%M"))

            third = second + timedelta(hours=1)
            self.interval2.config(text=third.strftime("%H:%M"))

            fourth = third + timedelta(hours=1)
            self.interval3.config(text=fourth.strftime("%H:%M"))

            fifth = fourth + timedelta(hours=1)
            self.interval4.config(text=fifth.strftime("%H:%M"))

            sixth = fifth + timedelta(hours=1)
            self.interval5.config(text=sixth.strftime("%H:%M"))

        else:
            messagebox.showerror("Error", "Failed to fetch weather information. Please try again.")

    def get_weather_forecast(self, latitude, longitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto"

    # Weather code description dictionary
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Drizzle - Light intensity",
            52: "Drizzle",
            53: "Drizzle - Moderate intensity",
            55: "Drizzle - Heavy intensity",
            56: "Freezing drizzle - Light intensity",
            57: "Freezing drizzle",
            61: "Rain - Slight intensity",
            62: "Rain",
            63: "Rain - Moderate intensity",
            65: "Rain - Heavy intensity",
            66: "Freezing rain - Light intensity",
            67: "Freezing rain",
            71: "Snow fall - Slight intensity",
            72: "Snow fall",
            73: "Snow fall - Moderate intensity",
            75: "Snow fall - Heavy intensity",
            77: "Snow grains",
            80: "Rain showers - Slight intensity",
            81: "Rain showers",
            82: "Rain showers - Violent intensity",
            85: "Snow showers - Slight intensity",
            86: "Snow showers - Heavy intensity",
            95: "Thunderstorm - Slight intensity",
            96: "Thunderstorm with slight hail",
            97: "Thunderstorm with hail",
            99: "Thunderstorm with heavy hail"
        }
        try:
            response = requests.get(url)
            data = response.json()

            if 'hourly' in data:
                hourly_forecasts = data['hourly']
                current_hour = self.get_current_hour()
                for i in range(1, min(6, len(hourly_forecasts['time']))):
                    time = hourly_forecasts['time'][i]
                    temperature = hourly_forecasts['temperature_2m'][i]
                    weather_code = hourly_forecasts['weather_code'][i]
                    weather_description = weather_codes.get(weather_code, "Unknown")

                #updata hours cell with weather image
                #hour 1
                    hr1_weather_code=hourly_forecasts['weather_code'][0]
                    hr1weather_image = Image.open(f"oasisinfobyte/{hr1_weather_code}s.png") 
                    self.hr1weather_photo = ImageTk.PhotoImage(hr1weather_image)
                    self.first_hr_image.config(image=self.hr1weather_photo) 
                #hour 2
                    hr2_weather_code=hourly_forecasts['weather_code'][1]
                    hr2weather_image = Image.open(f"oasisinfobyte/{hr2_weather_code}s.png") 
                    self.hr2weather_photo = ImageTk.PhotoImage(hr2weather_image)
                    self.second_hr_image.config(image=self.hr2weather_photo)
                #hour 3
                    hr3_weather_code=hourly_forecasts['weather_code'][2]
                    hr3weather_image = Image.open(f"oasisinfobyte/{hr3_weather_code}s.png") 
                    self.hr3weather_photo = ImageTk.PhotoImage(hr3weather_image)
                    self.third_hr_image.config(image=self.hr3weather_photo)
                #hour 4
                    hr4_weather_code=hourly_forecasts['weather_code'][3]
                    hr4weather_image = Image.open(f"oasisinfobyte/{hr4_weather_code}s.png") 
                    self.hr4weather_photo = ImageTk.PhotoImage(hr4weather_image)
                    self.fourth_hr_image.config(image=self.hr4weather_photo)
                #hour 5 
                    hr5_weather_code=hourly_forecasts['weather_code'][4]
                    hr5weather_image = Image.open(f"oasisinfobyte/{hr5_weather_code}s.png") 
                    self.hr5weather_photo = ImageTk.PhotoImage(hr5weather_image)
                    self.fifth_hr_image.config(image=self.hr5weather_photo)               
                # Update the labels with the forecast data
                    description_label = getattr(self, f"description_info_{i}")
                    temperature_label = getattr(self, f"temperature_info_{i}")
                    description_label.config(text=weather_description)
                    temperature_label.config(text=f"{temperature}°C")

            if 'daily' in data:
                daily_forecasts = data['daily']
            # Showcase day 1 data separately
                day1_weather_code = daily_forecasts['weather_code'][0]
                day1_temp_max = daily_forecasts['temperature_2m_max'][0]
                day1_temp_min = daily_forecasts['temperature_2m_min'][0]
                
                day1_weather_description = weather_codes.get(day1_weather_code, "Unknown")
            # Update the labels with day 1 forecast data
                day1weather_image = Image.open(f"oasisinfobyte/{day1_weather_code}.png")  
                self.day1weather_photo = ImageTk.PhotoImage(day1weather_image)
                self.zerothimage.config(image=self.day1weather_photo)      
                self.day1_description_label.config(text=day1_weather_description)
                self.day1_temperature_max_label.config(text=f"Max: {day1_temp_max}°C")
                self.day1_temperature_min_label.config(text=f" Min: {day1_temp_min}°C")
            #update cells with Weather images
            #day2
                day2_weather_code=daily_forecasts['weather_code'][1]
                day2weather_image = Image.open(f"oasisinfobyte/{day2_weather_code}s.png") 
                self.day2weather_photo = ImageTk.PhotoImage(day2weather_image)
                self.day2_image.config(image=self.day2weather_photo)            
            #day3
                day3_weather_code=daily_forecasts['weather_code'][2]
                day3weather_image = Image.open(f"oasisinfobyte/{day3_weather_code}s.png") 
                self.day3weather_photo = ImageTk.PhotoImage(day3weather_image)
                self.day3_image.config(image=self.day3weather_photo)
            #day4
                day4_weather_code=daily_forecasts['weather_code'][3]
                day4weather_image = Image.open(f"oasisinfobyte/{day4_weather_code}s.png") 
                self.day4weather_photo = ImageTk.PhotoImage(day4weather_image)
                self.day4_image.config(image=self.day4weather_photo)
            #day5
                day5_weather_code=daily_forecasts['weather_code'][4]
                day5weather_image = Image.open(f"oasisinfobyte/{day5_weather_code}s.png") 
                self.day5weather_photo = ImageTk.PhotoImage(day5weather_image)
                self.day5_image.config(image=self.day5weather_photo)
            #day6
                day6_weather_code=daily_forecasts['weather_code'][5]
                day6weather_image = Image.open(f"oasisinfobyte/{day6_weather_code}s.png") 
                self.day6weather_photo = ImageTk.PhotoImage(day6weather_image)
                self.day6_image.config(image=self.day6weather_photo)
            # Loop through daily forecasts starting from day 2
                for i in range(2, min(7, len(daily_forecasts['time']))):
                    day_weather_code = daily_forecasts['weather_code'][i - 1]  # Adjust index to start from day 2
                    day_temp_max = daily_forecasts['temperature_2m_max'][i - 1]  # Adjust index to start from day 2
                    day_temp_min = daily_forecasts['temperature_2m_min'][i - 1]  # Adjust index to start from day 2
                    day_weather_description = weather_codes.get(day_weather_code, "Unknown")
                    
                # Update the labels with the forecast data for each day
                    day_description_label = getattr(self, f"daydescription_info_{i}")
                    day_temperature_max_label = getattr(self, f"daytemperaturemax_info_{i}")
                    day_temperature_min_label = getattr(self, f"daytemperaturemin_info_{i}")
                    day_description_label.config(text=day_weather_description)
                    day_temperature_max_label.config(text=f"Max: {day_temp_max}°C")
                    day_temperature_min_label.config(text=f" Min: {day_temp_min}°C")

        except Exception as e:
            print("Error fetching weather data:", e)

# Function to get GPS coordinates using gps or Ip address for android integration of app 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    '''def get_gps(self):
        try:
            droid = android.Android()
            droid.startLocating()
            event = droid.eventWaitFor('location', 10000).result

            if event['name'] == "location":
                try:
                    latitude = event['data']['gps']['latitude']
                    longitude = event['data']['gps']['longitude']
                except KeyError:
                    latitude = event['data']['network']['latitude']
                    longitude = event['data']['network']['longitude']
                finally:
                    droid.stopLocating()
                    self.get_weather(latitude, longitude)
                    self.get_weather_forecast(latitude, longitude)
        except android.AndroidException as e:
            messagebox.showerror("Error", f"Failed to get GPS coordinates: {str(e)}")
            return None, None
            '''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # Function to search weather using text entry
    def search_weather(self):
        location = self.textfield.get()
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(location)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            self.get_weather(latitude, longitude)
            self.get_weather_forecast(latitude, longitude)
        else:
            messagebox.showerror("Error", "Location not found. Please try again.")

root = tk.Tk()
root.title("GPS Weather App")
root.geometry('550x650')
root.resizable(width=False, height=False)

# Create an instance of MyApp
app = MyApp(root)

# Start the GUI event loop
root.mainloop()
