import customtkinter
import requests
import datetime
from api_token import openweather_api_key

window = customtkinter.CTk()
window.title('WeaMeteo')
window.geometry('600x600')
window.resizable(True, True)
window.iconbitmap("icon.ico")

def btn_event_get_cityname():
    city_name = city_entry.get()
    if city_name != '':
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={openweather_api_key}&units=metric&lang=ru')
        if r.status_code == 200:
            accepted_data = r.json()
            city = accepted_data['name']
            temperature = accepted_data['main']['temp']
            feel_temp = accepted_data['main']['feels_like']
            weather = accepted_data['weather'][0]['description']
            wind_speed = accepted_data['wind']['speed']
            pressure = accepted_data['main']['pressure']
            humidity = accepted_data['main']['humidity']
            timezone = accepted_data['timezone']
            crnt_timezone = 10800
            timeform = '%d-%m-%Y %H:%M'
            timeshift = timezone - crnt_timezone
            crnt_time = datetime.datetime.now() + datetime.timedelta(seconds=timeshift)
            label_3.configure(text=city, font=customtkinter.CTkFont(size=26), anchor='center')
            label_4.configure(text=f"{int(temperature)} C°", font=customtkinter.CTkFont(size=32))
            label_5.configure(text=f"Ощущается как {int(feel_temp)} C°", font=customtkinter.CTkFont(size=24))
            label_6.configure(text=weather.capitalize(), font=customtkinter.CTkFont(size=24))
            label_7.configure(text=f"Скорость ветра {wind_speed} м/с", font=customtkinter.CTkFont(size=24))
            label_8.configure(text=f"Атмосферное давление {pressure} мм рт.ст.", font=customtkinter.CTkFont(size=24))
            label_9.configure(text=f"Влажность {humidity}%", font=customtkinter.CTkFont(size=24))
            label_10.configure(text=f"Местное время: {crnt_time.strftime(timeform)}", font=customtkinter.CTkFont(size=24))
        else:
            label_3.configure(text='Город не найден', font=customtkinter.CTkFont(size=20))
            label_4.configure(text='Н/Д', font=customtkinter.CTkFont(size=32))

        frame_1.pack_forget()
        frame_2.pack(pady=20, padx=20, fill="both", expand=True)


def button_back_1():
    frame_2.pack_forget()
    frame_1.pack(pady=20, padx=20, fill="both", expand=True)
    city_entry.delete(0, customtkinter.END)
    label_3.configure(text='')
    label_4.configure(text='')
    label_5.configure(text='')
    label_6.configure(text='')
    label_7.configure(text='')
    label_8.configure(text='')
    label_9.configure(text='')
    label_10.configure(text='')

def change_appearance(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

frame_1 = customtkinter.CTkFrame(master=window)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text='WeaMeteo', font=customtkinter.CTkFont(size=26, weight="bold"), justify=customtkinter.LEFT)
label_1.pack(pady=(10,30), padx=0)

label_2 = customtkinter.CTkLabel(master=frame_1, text='Введите полное название города', font=customtkinter.CTkFont(size=16), justify=customtkinter.CENTER)
label_2.pack(pady=10, padx=0)

city_entry = customtkinter.CTkEntry(master=frame_1, width=300, height=40, placeholder_text="Название города", justify =customtkinter.CENTER, font=customtkinter.CTkFont(size=16))
city_entry.pack(pady=10, padx=0)

button_1 = customtkinter.CTkButton(master=frame_1, width= 300, height=40, text='Получить данные',font=customtkinter.CTkFont(size=16), command=btn_event_get_cityname)
button_1.pack(pady=10, padx=0)

frame_2 = customtkinter.CTkFrame(master=window)

label_3 = customtkinter.CTkLabel(master=frame_2, text='', justify=customtkinter.CENTER)
label_3.pack(pady=(10, 15), padx=0)

label_4 = customtkinter.CTkLabel(master=frame_2, text='', justify=customtkinter.CENTER)
label_4.pack(pady=(0, 15), padx=0)

label_5 = customtkinter.CTkLabel(master=frame_2, text='',  justify=customtkinter.CENTER)
label_5.pack(pady=0, padx=0)

label_6 = customtkinter.CTkLabel(master=frame_2, text='', justify=customtkinter.CENTER)
label_6.pack(pady=0, padx=0)

label_7 = customtkinter.CTkLabel(master=frame_2, text='', justify=customtkinter.CENTER)
label_7.pack(pady=0, padx=0)

label_8 = customtkinter.CTkLabel(master=frame_2, text='', justify=customtkinter.CENTER)
label_8.pack(pady=0, padx=0)

label_9 = customtkinter.CTkLabel(master=frame_2, text='', justify=customtkinter.CENTER)
label_9.pack(pady=0, padx=0)

label_10 = customtkinter.CTkLabel(master=frame_2, text='', justify=customtkinter.CENTER)
label_10.pack(pady=0, padx=0)

button_2 = customtkinter.CTkButton(master=frame_2, width=300, height=40, text='Назад', font=customtkinter.CTkFont(size=18), command=button_back_1)
button_2.pack(pady=(45, 0), padx=0)

change_theme_menu = customtkinter.CTkOptionMenu(master=frame_1, values=["System", "Dark", "Light"], command=change_appearance)
change_theme_menu.set("System")
change_theme_menu.pack(pady=(270, 0), padx=0)

window.mainloop()